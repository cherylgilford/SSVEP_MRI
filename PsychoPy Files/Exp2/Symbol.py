#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.2),
    on Sat Jan  7 09:57:39 2023
"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.2.2'
expName = 'Session2_Symbol'  # from the Builder filename that created this script
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
    'session': '001',
}
# --- Show participant info dialog --
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/cherylgilford/Desktop/Session2_Symbol.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename) # CHANGE PATH ACCORDINGLY
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=(1024, 768), fullscr=True, screen=0,
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color=[0.5544, 0.5544, 0.5544], colorSpace='rgb',
    blendMode='avg', useFBO=True,
    units='height')
win.mouseVisible = False
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# --- Setup input devices ---
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# --- Initialize components for Routine "welcome" ---
WelcomeInstructions = visual.TextStim(win=win, name='WelcomeInstructions',
    text='Welcome to the experiment session.\n\nIt is important that you keep still as possible when the scanning is underway.\n\nThe session will take about 17 minutes to complete.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0,
    color='black', colorSpace='rgb', opacity=None,
    languageStyle='LTR', flipHoriz=True,
    depth=0.0);
PreScanning = visual.TextStim(win=win, name='PreScanning',
    text='Please wait for the MRI pre-scanning session to complete.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0,
    color='black', colorSpace='rgb', opacity=None,
    languageStyle='LTR', flipHoriz=True,
    depth=-1.0);
key_resp_1 = keyboard.Keyboard()

# --- Initialize components for Routine "wait" ---
key_resp_2 = keyboard.Keyboard()
volumes = visual.TextStim(win=win, name='volumes',
    text='Discarding the first 5 volumes.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0,
    color='black', colorSpace='rgb', opacity=None,
    languageStyle='LTR', flipHoriz=True,
    depth=-1.0);

# --- Initialize components for Routine "experiment" ---
key_resp_3 = keyboard.Keyboard()
# Run 'Begin Experiment' code from code


fixation = visual.ShapeStim(
    win=win, name='fixation', vertices='cross',
    size=(0.1, 0.1),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='white',
    opacity=None, depth=-2.0, interpolate=True)
image_1_part_2 = visual.ImageStim(
    win=win,
    name='image_1_part_2',
    image='/Users/cherylgilford/Desktop/PowerOnWhite.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.12, 0.12),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0) # CHANGE PATH ACCORDINGLY
image = visual.ImageStim(
    win=win,
    name='image',
    image='/Users/cherylgilford/Desktop/PowerOnBlack.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.12, 0.12),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0) # CHANGE PATH ACCORDINGLY
rest = visual.TextStim(win=win, name='rest',
    text='Rest',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0,
    color='black', colorSpace='rgb', opacity=None,
    languageStyle='LTR', flipHoriz=True,
    depth=-4.0);

# --- Initialize components for Routine "experiment2" ---
key_resp_4 = keyboard.Keyboard()
# Run 'Begin Experiment' code from code_2


fixation_2 = visual.ShapeStim(
    win=win, name='fixation_2', vertices='cross',
    size=(0.1, 0.1),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='white',
    opacity=None, depth=-2.0, interpolate=True)
image_2_part_2 = visual.ImageStim(
    win=win,
    name='image_2_part_2',
    image='/Users/cherylgilford/Desktop/TurnOnWhite.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.12, 0.12),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=True, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0) # CHANGE PATH ACCORDINGLY
image_2 = visual.ImageStim(
    win=win,
    name='image_2',
    image='/Users/cherylgilford/Desktop/TurnOnBlack.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.12, 0.12),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=True, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0) # CHANGE PATH ACCORDINGLY
rest_2 = visual.TextStim(win=win, name='rest_2',
    text='Rest',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0,
    color='black', colorSpace='rgb', opacity=None,
    languageStyle='LTR', flipHoriz=True,
    depth=-5.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine

# --- Prepare to start Routine "welcome" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
key_resp_1.keys = []
key_resp_1.rt = []
_key_resp_1_allKeys = []
# keep track of which components have finished
welcomeComponents = [WelcomeInstructions, PreScanning, key_resp_1]
for thisComponent in welcomeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1
keyNo = 0
EndTrial = False

# --- Run Routine "welcome" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *WelcomeInstructions* updates
    if WelcomeInstructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        WelcomeInstructions.frameNStart = frameN  # exact frame index
        WelcomeInstructions.tStart = t  # local t and not account for scr refresh
        WelcomeInstructions.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(WelcomeInstructions, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'WelcomeInstructions.started')
        WelcomeInstructions.setAutoDraw(True)
    if WelcomeInstructions.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > WelcomeInstructions.tStartRefresh + 30.0-frameTolerance:
            # keep track of stop time/frame for later
            WelcomeInstructions.tStop = t  # not accounting for scr refresh
            WelcomeInstructions.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'WelcomeInstructions.stopped')
            WelcomeInstructions.setAutoDraw(False)
    
    # *PreScanning* updates
    if PreScanning.status == NOT_STARTED and tThisFlip >= 30.0-frameTolerance:
        # keep track of start time/frame for later
        PreScanning.frameNStart = frameN  # exact frame index
        PreScanning.tStart = t  # local t and not account for scr refresh
        PreScanning.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(PreScanning, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'PreScanning.started')
        PreScanning.setAutoDraw(True)
    
    # *key_resp_1* updates
    waitOnFlip = False
    if key_resp_1.status == NOT_STARTED and tThisFlip >= 30.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_1.frameNStart = frameN  # exact frame index
        key_resp_1.tStart = t  # local t and not account for scr refresh
        key_resp_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_1, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp_1.started')
        key_resp_1.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_1.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_1.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_1.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_1.getKeys(keyList=['s'], waitRelease=False)
        _key_resp_1_allKeys.extend(theseKeys)
        if 's' in theseKeys:
            keyNo += 1
        if len(_key_resp_1_allKeys):
            key_resp_1.keys = [key.name for key in _key_resp_1_allKeys]  # storing all keys
            key_resp_1.rt = [key.rt for key in _key_resp_1_allKeys]
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in welcomeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "welcome" ---
for thisComponent in welcomeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_1.keys in ['', [], None]:  # No response was made
    key_resp_1.keys = None
thisExp.addData('key_resp_1.keys',key_resp_1.keys)
if key_resp_1.keys != None:  # we had a response
    thisExp.addData('key_resp_1.rt', key_resp_1.rt)
thisExp.nextEntry()
# the Routine "welcome" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_1 = data.TrialHandler(nReps=5.0, method='random',
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trials_1')
thisExp.addLoop(trials_1)  # add the loop to the experiment
thisTrial_1 = trials_1.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_1.rgb)
if thisTrial_1 != None:
    for paramName in thisTrial_1:
        exec('{} = thisTrial_1[paramName]'.format(paramName))
        
keyNo = 0
EndTrial = False

for thisTrial_1 in trials_1:
    currentLoop = trials_1
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_1.rgb)
    if thisTrial_1 != None:
        for paramName in thisTrial_1:
            exec('{} = thisTrial_1[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "wait" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    key_resp_2.keys = []
    key_resp_2.rt = []
    _key_resp_2_allKeys = []
    # keep track of which components have finished
    waitComponents = [key_resp_2, volumes]
    for thisComponent in waitComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "wait" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *key_resp_2* updates
        waitOnFlip = False
        if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_2.frameNStart = frameN  # exact frame index
            key_resp_2.tStart = t  # local t and not account for scr refresh
            key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_2.started')
            key_resp_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_2.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_2.getKeys(keyList=['s'], waitRelease=False)
            _key_resp_2_allKeys.extend(theseKeys)
            if 's' in theseKeys:
                keyNo += 1
            if len(_key_resp_2_allKeys):
                key_resp_2.keys = [key.name for key in _key_resp_2_allKeys]  # storing all keys
                key_resp_2.rt = [key.rt for key in _key_resp_2_allKeys]
                # a response ends the routine
                continueRoutine = False
        
        # *volumes* updates
        if volumes.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            volumes.frameNStart = frameN  # exact frame index
            volumes.tStart = t  # local t and not account for scr refresh
            volumes.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(volumes, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'volumes.started')
            volumes.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in waitComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "wait" ---
    for thisComponent in waitComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_2.keys in ['', [], None]:  # No response was made
        key_resp_2.keys = None
    thisExp.addData('key_resp_2.keys',key_resp_2.keys)
    if key_resp_2.keys != None:  # we had a response
        thisExp.addData('key_resp_2.rt', key_resp_2.rt)
    thisExp.nextEntry()
    # the Routine "wait" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 5.0 repeats of 'trials_1'


# set up handler to look after randomisation of conditions etc
trials_4 = data.TrialHandler(nReps=2.0, method='random',
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trials_4')
thisExp.addLoop(trials_4)  # add the loop to the experiment
thisTrial_4 = trials_4.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_4.rgb)
if thisTrial_4 != None:
    for paramName in thisTrial_4:
        exec('{} = thisTrial_4[paramName]'.format(paramName))

for thisTrial_4 in trials_4:
    currentLoop = trials_4
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_4.rgb)
    if thisTrial_4 != None:
        for paramName in thisTrial_4:
            exec('{} = thisTrial_4[paramName]'.format(paramName))
    
    trial_number = 0
    frame_seq = 0
    # set up handler to look after randomisation of conditions etc
    trials_2 = data.TrialHandler(nReps=6.0, method='random',
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='trials_2')
    thisExp.addLoop(trials_2)  # add the loop to the experiment
    thisTrial_2 = trials_2.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
    if thisTrial_2 != None:
        for paramName in thisTrial_2:
            exec('{} = thisTrial_2[paramName]'.format(paramName))
    
    for thisTrial_2 in trials_2:
        trial_number += 1
        currentLoop = trials_2
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
        if thisTrial_2 != None:
            for paramName in thisTrial_2:
                exec('{} = thisTrial_2[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "experiment" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        key_resp_3.keys = []
        key_resp_3.rt = []
        _key_resp_3_allKeys = []
        # Run 'Begin Routine' code from code
        keyNo = 0
        EndTrial = False
        
        fixation.setFillColor('black')
        # keep track of which components have finished
        experimentComponents = [key_resp_3, fixation, image_1_part_2, image, rest]
        for thisComponent in experimentComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "experiment" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *key_resp_3* updates
            waitOnFlip = False
            if key_resp_3.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_3.frameNStart = frameN  # exact frame index
                key_resp_3.tStart = t  # local t and not account for scr refresh
                key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_3.started')
                key_resp_3.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_3.status == STARTED:
                if bool(EndTrial == True):
                    # keep track of stop time/frame for later
                    key_resp_3.tStop = t  # not accounting for scr refresh
                    key_resp_3.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'key_resp_3.stopped')
                    key_resp_3.status = FINISHED
            if key_resp_3.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_3.getKeys(keyList=['s'], waitRelease=False)
                _key_resp_3_allKeys.extend(theseKeys)
                if 's' in theseKeys:
                    keyNo += 1
                if len(_key_resp_3_allKeys):
                    key_resp_3.keys = [key.name for key in _key_resp_3_allKeys]  # storing all keys
                    key_resp_3.rt = [key.rt for key in _key_resp_3_allKeys]
            
            # *fixation* updates
            if fixation.status == NOT_STARTED and keyNo == 1:
                # keep track of start time/frame for later
                fixation.frameNStart = frameN  # exact frame index
                fixation.tStart = t  # local t and not account for scr refresh
                fixation.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixation, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixation.started')
                fixation.setAutoDraw(True)
            if fixation.status == STARTED:
                if bool(keyNo == 11):
                    # keep track of stop time/frame for later
                    fixation.tStop = t  # not accounting for scr refresh
                    fixation.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'fixation.stopped')
                    fixation.setAutoDraw(False)
            
            # *image_1_part_2* updates
            if image_1_part_2.status == NOT_STARTED and keyNo == 11:
                # keep track of start time/frame for later
                image_1_part_2.frameNStart = frameN  # exact frame index
                image_1_part_2.tStart = t  # local t and not account for scr refresh
                image_1_part_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_1_part_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_1_part_2.started')
                image_1_part_2.setAutoDraw(True)
            if image_1_part_2.status == STARTED:
                if bool(keyNo == 26):
                    # keep track of stop time/frame for later
                    image_1_part_2.tStop = t  # not accounting for scr refresh
                    image_1_part_2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image_1_part_2.stopped')
                    image_1_part_2.setAutoDraw(False)
            
            # *image* updates
            if image.status == NOT_STARTED and keyNo == 11:
                # keep track of start time/frame for later
                image.frameNStart = frameN  # exact frame index
                image.tStart = t  # local t and not account for scr refresh
                image.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image.started')
                image.setAutoDraw(True)
            if image.status == STARTED:
                if bool(keyNo == 26):
                    # keep track of stop time/frame for later
                    image.tStop = t  # not accounting for scr refresh
                    image.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image.stopped')
                    image.setAutoDraw(False)
            if image.status == STARTED:  # only update if drawing
                if trial_number == 1:
                    frame_seq = (frameN % 8) >= 4
                elif trial_number == 2:
                    frame_seq = (frameN % 6) >= 3
                elif trial_number == 3:
                    frame_seq = (frameN % 4) >= 2
                if trial_number == 4:
                    frame_seq = (frameN % 3) >= 1.5
                elif trial_number == 5:
                    frame_seq = (frameN % 2.5) >= 1.25
                elif trial_number == 6:
                    frame_seq = (frameN % 2) >= 1
                image.setOpacity(frame_seq, log=False)
            
            # *rest* updates
            if rest.status == NOT_STARTED and keyNo == 26:
                # keep track of start time/frame for later
                rest.frameNStart = frameN  # exact frame index
                rest.tStart = t  # local t and not account for scr refresh
                rest.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(rest, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'rest.started')
                rest.setAutoDraw(True)
            if rest.status == STARTED:
                if bool(keyNo == 27):
                    # keep track of stop time/frame for later
                    rest.tStop = t  # not accounting for scr refresh
                    rest.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'rest.stopped')
                    rest.setAutoDraw(False)
                    EndTrial = True
                    
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in experimentComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "experiment" ---
        for thisComponent in experimentComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if key_resp_3.keys in ['', [], None]:  # No response was made
            key_resp_3.keys = None
        thisExp.addData('key_resp_3.keys',key_resp_3.keys)
        if key_resp_3.keys != None:  # we had a response
            thisExp.addData('key_resp_3.rt', key_resp_3.rt)
        thisExp.nextEntry()
        # the Routine "experiment" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 6.0 repeats of 'trials_2'
    trial_number = 0
    frame_seq = 0
    
    # set up handler to look after randomisation of conditions etc
    trials_3 = data.TrialHandler(nReps=6.0, method='random',
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='trials_3')
    thisExp.addLoop(trials_3)  # add the loop to the experiment
    thisTrial_3 = trials_3.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
    if thisTrial_3 != None:
        for paramName in thisTrial_3:
            exec('{} = thisTrial_3[paramName]'.format(paramName))
    
    for thisTrial_3 in trials_3:
        trial_number += 1
        currentLoop = trials_3
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
        if thisTrial_3 != None:
            for paramName in thisTrial_3:
                exec('{} = thisTrial_3[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "experiment2" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        key_resp_4.keys = []
        key_resp_4.rt = []
        _key_resp_4_allKeys = []
        # Run 'Begin Routine' code from code_2
        keyNo = 0
        EndTrial = False
        
        fixation_2.setFillColor('black')
        # keep track of which components have finished
        experiment2Components = [key_resp_4, fixation_2, image_2_part_2, image_2, rest_2]
        for thisComponent in experiment2Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "experiment2" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *key_resp_4* updates
            waitOnFlip = False
            if key_resp_4.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_4.frameNStart = frameN  # exact frame index
                key_resp_4.tStart = t  # local t and not account for scr refresh
                key_resp_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_4, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_4.started')
                key_resp_4.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_4.status == STARTED:
                if bool(EndTrial == True):
                    # keep track of stop time/frame for later
                    key_resp_4.tStop = t  # not accounting for scr refresh
                    key_resp_4.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'key_resp_4.stopped')
                    key_resp_4.status = FINISHED
            if key_resp_4.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_4.getKeys(keyList=['s'], waitRelease=False)
                _key_resp_4_allKeys.extend(theseKeys)
                if 's' in theseKeys:
                    keyNo += 1
                if len(_key_resp_4_allKeys):
                    key_resp_4.keys = [key.name for key in _key_resp_4_allKeys]  # storing all keys
                    key_resp_4.rt = [key.rt for key in _key_resp_4_allKeys]
            
            # *fixation_2* updates
            if fixation_2.status == NOT_STARTED and keyNo == 1:
                # keep track of start time/frame for later
                fixation_2.frameNStart = frameN  # exact frame index
                fixation_2.tStart = t  # local t and not account for scr refresh
                fixation_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixation_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixation_2.started')
                fixation_2.setAutoDraw(True)
            if fixation_2.status == STARTED:
                if bool(keyNo == 11):
                    # keep track of stop time/frame for later
                    fixation_2.tStop = t  # not accounting for scr refresh
                    fixation_2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'fixation_2.stopped')
                    fixation_2.setAutoDraw(False)
            
            # *image_2_part_2* updates
            if image_2_part_2.status == NOT_STARTED and keyNo == 11:
                # keep track of start time/frame for later
                image_2_part_2.frameNStart = frameN  # exact frame index
                image_2_part_2.tStart = t  # local t and not account for scr refresh
                image_2_part_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_2_part_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_2_part_2.started')
                image_2_part_2.setAutoDraw(True)
            if image_2_part_2.status == STARTED:
                if bool(keyNo == 26):
                    # keep track of stop time/frame for later
                    image_2_part_2.tStop = t  # not accounting for scr refresh
                    image_2_part_2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image_2_part_2.stopped')
                    image_2_part_2.setAutoDraw(False)
            
            # *image_2* updates
            if image_2.status == NOT_STARTED and keyNo == 11:
                # keep track of start time/frame for later
                image_2.frameNStart = frameN  # exact frame index
                image_2.tStart = t  # local t and not account for scr refresh
                image_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_2.started')
                image_2.setAutoDraw(True)
            if image_2.status == STARTED:
                if bool(keyNo == 26):
                    # keep track of stop time/frame for later
                    image_2.tStop = t  # not accounting for scr refresh
                    image_2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image_2.stopped')
                    image_2.setAutoDraw(False)
            if image_2.status == STARTED:  # only update if drawing
                if trial_number == 1:
                    frame_seq = (frameN % 8) >= 4
                elif trial_number == 2:
                    frame_seq = (frameN % 6) >= 3
                elif trial_number == 3:
                    frame_seq = (frameN % 4) >= 2
                if trial_number == 4:
                    frame_seq = (frameN % 3) >= 1.5
                elif trial_number == 5:
                    frame_seq = (frameN % 2.5) >= 1.25
                elif trial_number == 6:
                    frame_seq = (frameN % 2) >= 1
                image_2.setOpacity(frame_seq, log=False)
            
            # *rest_2* updates
            if rest_2.status == NOT_STARTED and keyNo == 26:
                # keep track of start time/frame for later
                rest_2.frameNStart = frameN  # exact frame index
                rest_2.tStart = t  # local t and not account for scr refresh
                rest_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(rest_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'rest_2.started')
                rest_2.setAutoDraw(True)
            if rest_2.status == STARTED:
                if bool(keyNo == 27):
                    # keep track of stop time/frame for later
                    rest_2.tStop = t  # not accounting for scr refresh
                    rest_2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'rest_2.stopped')
                    rest_2.setAutoDraw(False)
                    EndTrial = True
                    
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in experiment2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "experiment2" ---
        for thisComponent in experiment2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if key_resp_4.keys in ['', [], None]:  # No response was made
            key_resp_4.keys = None
        thisExp.addData('key_resp_4.keys',key_resp_4.keys)
        if key_resp_4.keys != None:  # we had a response
            thisExp.addData('key_resp_4.rt', key_resp_4.rt)
        thisExp.nextEntry()
        # the Routine "experiment2" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 6.0 repeats of 'trials_3'
    
    thisExp.nextEntry()
    
# completed 2.0 repeats of 'trials_4'


# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip()
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()

