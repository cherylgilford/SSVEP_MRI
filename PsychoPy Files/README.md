\- Contact person  
  
Cheryl Gilford  
cheryl.gilford@um.edu.mt  
  
## Overview  
  
- \Project name:   
  
- \[Year(s) that the project ran: 2022 - 2023 ]  
  
- \[Brief overview of the project] 
  
functional magnetic resonance imaging (fMRI) was used to localise the
steady-state visual evoked potential (SSVEP) in the brain which is
generated when a subject focuses on a repetitive visual flickering
stimulus. Through the tasks shown in this experiment the magnitude and
location of the SSVEPs across the whole scalp where analysed when
subjects where shown different stimuli properties, including stimuli
with a varied colour, shape and texture.  
  
- \[Stimuli and independent variables]   
  
3 different coloured stimuli, 2 different symbol stimuli and 2 different
textured stimuli were presented to the participants at different
flickering frequencies. The 3 coloured stimuli included a black-white
flickering stimulus, a green-blue flickering stimulus and a green-red
flickering stimulus. The 2 symbol stimuli included a power on/off symbol
stimulus and a ‘Turn On’ text stimulus. The 2 textured stimuli included
a checkerboard stimulus and a random dot map stimulus. Each stimulus was
shown at the following stimulation frequencies: 7.5 Hz, 10 Hz, 15 Hz, 20
Hz, 24 Hz, 30 Hz. Each stimulus flickering at a particular frequency was
shown twice.  
  
- \[Quality assessment of the data]  
  
Prior to preprocessing the data using fMRIPrep
(https://fmriprep.org/en/stable/; Esteban et al., 2019), we generated
visual quality reports for the anatomical and functional images with
MRIQC (https://mriqc.readthedocs.io/en/latest/; Esteban et al., 2017).
Following inspection of these reports, data exclusions were implemented,
where the data for which the image quality metric (IQM) value differed
from the mean IQM of the API data by more than two standard deviations
were eliminated.  
  
\## Methods  
  
\### Subjects  
  
Participants were adults: 3 females, 3 males; age range: 22 - 28  
  
- \[Information about the recruitment procedure] 
  
Participants were recruited through advertising online and using posters
on the university campus. Any interested participants were required to
send an email to participate in this study.  
  
- \[Subject exclusion criteria] 
  
Participants had to have a good command of the English language since
the consent forms and information letters about the project were in
English. All participants had to have normal or corrected-to-normal
vision. Vision correction was achieved either via contact lenses or
MRI-compatible prescription glasses. All participants were screened for
MRI contraindications.  
  
\### Apparatus  
  
The stimuli were displayed on an MRI-compatible 60 Hz LCD monitor
(NordicNeuroLab, Norway) that was viewed through a mirror mounted on the
MRI scanner’s head coil, subtending a 12 degrees visual angle. Stimulus
presentation and response collection were controlled with custom code in
Python 3.11.1 (Python Software Foundation, https://www.python.org/) with
the PsychoPy toolbox v2022.2.2 (https://psychopy.org/index.html; Pierce
et al., 2019).  
  
The study was conducted at Mater Dei Hospital, Msida, Malta. Structural
and functional MR images were acquired on a 3T Siemens Magnetom Vida
scanner (Siemens, Germany), fitted with a 64-channel head coil.  
  
\### Initial setup  
  
Participants were instructed and briefly familiarised with the stimuli
and task, and completed safety and informed consent procedures.  
  
\### Task details and organisation  
  
The experiment was divided into three. The Python code for each of the
three experiments are located in the \`\`\`exp1\`\`\`,\`\`\` exp2\`\`\`
and \`\`\`exp3\`\`\` folders respectively. Additionally \`\`\`exp2\`\`\`
and \`\`\`exp3\`\`\` folders contain a \`\`\`Stimuli_Images\`\`\` folder
which contains the images of the stimuli used in that particular
experiment.  
  
Prior to starting Experiment 1, an extra session was performed during
which anatomical images of the brain and gradient-echo field maps were
recorded.  
  
Experiment 1 (\`\`\`exp1\`\`\` folder): This session opens up with a
welcome screen lasting 30 seconds, describing any important instructions
to the participant inside the scanner. Following this, a ‘pre-scanning
session’ was performed where five extra volumes were recorded to allow
for scanner stabilisation. This was directly followed by the stimuli
trials where the black-white stimulus, blue-green stimulus and red-green
stimulus were shown to the subject at each of the six different
frequencies (7.5 Hz, 10 Hz, 15 Hz, 20 Hz, 24 Hz and 30 Hz).  
  
Prior to every visual stimulus presentation at a particular frequency, a
fixation period was shown during which baseline fMRI data was recorded.
A rest period was also included after every visual stimulus
presentation. The fixation period, stimulation period and rest period,
together, made up a trial for every stimulus-frequency condition.  
  
Each trial started with a fixation period where subjects were instructed
to fixate on a black fixation cross at the centre of the screen for 15.2
s (10 volumes). The stimulus was then presented at the centre of the
screen for 22.8 s (15 volumes) followed by a 2.04 s rest period (two
volumes). A trial for each of the six frequencies per stimulus was
performed resulting in six trials per stimulus. Once the six trials per
coloured stimulus were performed, these were repeated once again in
order to have a total of two runs per coloured stimulus to obtain a
total of 12 trials for each stimulus colour (two trials for each
frequency).  
  
Experiment 2 (\`\`\`exp2\`\`\` folder): Following the welcome screen and
pre-scanning session, the same fixation period, stimulation period and
rest period trial sequence that was used in Experiment 1 was used in the
third session where the ‘Power On/Off’ and text stimuli were presented
to the subject. Six trials per stimulus were shown to the user (one
trial per frequency) and this was repeated twice for a total of two runs
to collect a total of 12 trials per stimulus, and hence two trials for
each frequency were recorded.  
  
Experiment 3 (\`\`\`exp3\`\`\` folder): Following the welcome screen and
pre-scanning session, the same trail sequence that consisted of a
fixation, stimulation, and rest period that was used in Experiments 1
and 2 was also utilised in this experimental session where the
checkerboard and random dot stimulus were shown to the participant. Six
trials per stimulus were shown to the user (one trial per frequency) and
this was repeated twice for a total of two runs to collect a total of 12
trials per stimulus, and hence two trials for each frequency were
recorded.  
  
\### Additional notes  
  
The session prior to Experiment 1 which included the recording of
anatomical images and gradient-field maps lasted 8 minutes. This was
directly followed by Experiment 1 which lasted 25 minutes where a total
of 977 volumes were recorded.  
  
During Experiment 2 and Experiment 3, 653 volumes were recorded
respectively and each session lasted 16 minutes.  
  
The whole MRI data recording experiment lasted for a total of 65 minutes
for each participant.  
  
  
—  
  
References:  
  
Esteban, O., Markiewicz, C. J., Blair, R. W., Moodie, C. A., Isik, A.
I., Erramuzpe, A., Kent, J. D., Goncalves, M., DuPre, E., Snyder, M.,
Oya, H., Ghosh, S. S., Wright, J., Durnez, J., Poldrack, R. A., &
Gorgolewski, K. J. (2019). fMRIPrep: A robust preprocessing pipeline for
functional MRI. Nature Methods, 16(1), Article 1.
<u><https://doi.org/10.1038/s41592-018-0235-4></u>  
Esteban, O., Birman, D., Schaer, M., Koyejo, O. O., Poldrack, R. A., &
Gorgolewski, K. J. (2017). MRIQC: Advancing the automatic prediction of
image quality in MRI from unseen sites. PLOS ONE, 12(9), e0184661.
<u><https://doi.org/10.1371/journal.pone.0184661></u>  
Peirce, J., Gray, J. R., Simpson, S., MacAskill, M., Höchenberger, R.,
Sogo, H., Kastman, E., & Lindeløv, J. K. (2019). PsychoPy2: Experiments
in behavior made easy. Behavior Research Methods, 51(1), 195–203.
<u><https://doi.org/10.3758/s13428-018-01193-y></u>  
  
