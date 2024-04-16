
# fMRI pipeline used in this project:

# Packages and software

BIDSKIT was used to convert the DICOM files to NIfTIs which were sorted according to the Brain Imaging Data Structure (BIDS) standard:

* [BIDSKIT v2022.10.13](https://github.com/jmtyszka/bidskit)

We use singularity containers for all processes in this pipeline:

* [Singularity v3.10.0](https://sylabs.io/docs/)

A FreeSurfer license is required by Singularity, which can be obtained from here https://surfer.nmr.mgh.harvard.edu/registration.html.

fMRIprep was used to process the recorded structural and functional images: 

* [fMRIprep v22.0.2](https://fmriprep.org/en/stable/)

FSL single-level and group-level analysis was used to apply the General Linear Model (GLM):

* [FSL v6.0](https://fsl.fmrib.ox.ac.uk/fsl/fslwiki)

# Processes

## Convert DICOMs to BIDS

We use BIDSKIT to concert fMRI data to BIDS format based on the experimental design. The following commands was used to do so: 

bidskit --no-sessions
bidskit --no-sessions --overwrite --complex --recon --multiecho --no-anon --bind-fmaps 
## Preprocess data

A Singularity container for fMRIprep was set up using the following command (replace the path accordingly): 

singularity build --sandbox /home/cheryl/Desktop/BIDS_Processing/sandbox/fmriprep-22.0.2.simg docker://nipreps/fmriprep:22.0.2 

We preprocess the fMRI data using the fMRIprep toolbox within a singularity container. Here is an example of how we call fMRIprep using the standard flags for our pipeline (replace the path to the freesurfer license file with your own):

singularity run --cleanenv sandbox/fmriprep-22.0.2.simg BIDS_Structured Output participant --participant-label 01 --fs-license-file /home/cfarr05/freesurfer_license.txt --output-spaces T1w MNI152NLin2009cAsym --verbose --notrack --ignore slicetiming --use-aroma --error-on-aroma-warnings --md-only-boilerplate --stop-on-first-crash 

Note, fMRIprep is technically nondeterministic; there is slight computational variability that results in slightly different reconstructions each time fMRIprep is run. For this reason, we try to maintain a standard of sharing subject-level preprocessed data as well as raw BIDS data.
fMRIprep includes standard fMRI preprocessing, and with the --use-aroma flag, it also runs "soft" artifact correction and generates the confounds used as nuisance regressors in first-level modelling. -- cleanenv is needed to ensure that Singularity uses the software libraries that come packaged in the container and not the ones on the host syste. See fMRIprep documentation for more information about the arguments (https://fmriprep.org/en/stable/usage.html). 

## First level analyses
We use FSL to run the first and second level GLM. The model is fit using FSL’s [FEAT tool](https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/FEAT/UserGuide).
There are event regressors per each contrast specified in the study-specific contrast file. Six contrast where utilised in our experiment which corresponded to the six different stimulation frequencies. The events.tsv files is located inside the BIDS directory specifying the onset and duration for every condition (fixation period, stimulation period, rest period) in the experiment.
The design for the experiment is calculated from those event files, along with nuisance regressors. Each event regressor is convolved with a double-gamma HRF, and a high-pass filter is applied to both the data and the model.
Motion correction is applied using FSL’s [MCFLIRT FMRIB’s Linear Registration Tool](https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/MCFLIRT). BET brain extraction is also applied to create a brain mask from the mean volume in the fMRI data. 5mm spatial smoothing is applied to each volume on the fMRI data separately. FILM prewhitening was used to make the statistics valid and maximally efficient. FSL’s GLM runs the first-level model. The current default is to run the model in MNI space, though this can be changed in your fmriprep command. See more information about FEAT on https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/FEAT/UserGuide.
The standard outputs of an FSL analysis are created in the output directory, including parameter estimates (pe.nii.gz), contrast estimates (con.nii.gz), and residuals. For exploring significance at the run level, the con*zstat.nii.gz are the most useful files.
## Second level analyses

Subject-level or second-level modelling combines the GLMs across runs, per subject.
The subject-level scripts will take the data from first level analyses and do operations on them; namely, we use the copes (beta estimates) and varcopes (variance estimates) using FSL's fixed-effects flow. 
