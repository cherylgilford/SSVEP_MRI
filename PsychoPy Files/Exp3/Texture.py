#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.2),
    on Wed Jan 18 14:42:38 2023
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
expName = 'Session3_Texture'  # from the Builder filename that created this script
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
    originPath='/Users/cherylgilford/Desktop/Session3_Texture.py',
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
    size=[1440, 900], fullscr=True, screen=0,
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
    text='Welcome to the experiment session.\n\nIt is important that syou keep still as possible when the scanning is underway.\n\nThe session will take about 17 minutes to complete.',
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

# --- Initialize components for Routine "texture_1" ---
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
    image='Stimuli/White.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.12, 0.12),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0) # CHANGE PATH ACCORDINGLY
image = visual.ImageStim(
    win=win,
    name='image',
    image='Stimuli/Texture_1.png', mask=None, anchor='center',
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
    depth=-5.0);

# --- Initialize components for Routine "texture_2" ---
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
    image='Stimuli/White.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.12, 0.12),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0) # CHANGE PATH ACCORDINGLY
image_2 = visual.ImageStim(
    win=win,
    name='image_2',
    image='Stimuli/Texture_2.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.12, 0.12),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0) # CHANGE PATH ACCORDINGLY
rest_2 = visual.TextStim(win=win, name='rest_2',
    text='Rest',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0,
    color='black', colorSpace='rgb', opacity=None,
    languageStyle='LTR', flipHoriz=True,
    depth=-5.0);

# --- Initialize components for Routine "texture_3" ---
key_resp_5 = keyboard.Keyboard()
# Run 'Begin Experiment' code from code_3


fixation_3 = visual.ShapeStim(
    win=win, name='fixation_3', vertices='cross',
    size=(0.1, 0.1),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='white',
    opacity=None, depth=-2.0, interpolate=True)
image_3_part_2 = visual.ImageStim(
    win=win,
    name='image_3_part_2',
    image='Stimuli/White.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.12, 0.12),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0) # CHANGE PATH ACCORDINGLY
image_3 = visual.ImageStim(
    win=win,
    name='image_3',
    image='Stimuli/Texture_3.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.12, 0.12),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0) # CHANGE PATH ACCORDINGLY
rest_3 = visual.TextStim(win=win, name='rest_3',
    text='Rest',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0,
    color='black', colorSpace='rgb', opacity=None,
    languageStyle='LTR', flipHoriz=True,
    depth=-5.0);

# --- Initialize components for Routine "texture_4" ---
key_resp_6 = keyboard.Keyboard()
# Run 'Begin Experiment' code from code_4


fixation_4 = visual.ShapeStim(
    win=win, name='fixation_4', vertices='cross',
    size=(0.1, 0.1),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='white',
    opacity=None, depth=-2.0, interpolate=True)
image_4_part_2 = visual.ImageStim(
    win=win,
    name='image_4_part_2',
    image='Stimuli/White.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.12, 0.12),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0) # CHANGE PATH ACCORDINGLY
image_4 = visual.ImageStim(
    win=win,
    name='image_4',
    image='Stimuli/Texture_4.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.12, 0.12),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0) # CHANGE PATH ACCORDINGLY
rest_4 = visual.TextStim(win=win, name='rest_4',
    text='Rest',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0,
    color='black', colorSpace='rgb', opacity=None,
    languageStyle='LTR', flipHoriz=True,
    depth=-5.0);

# --- Initialize components for Routine "texture_5" ---
key_resp_7 = keyboard.Keyboard()
# Run 'Begin Experiment' code from code_5


fixation_5 = visual.ShapeStim(
    win=win, name='fixation_5', vertices='cross',
    size=(0.1, 0.1),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='white',
    opacity=None, depth=-2.0, interpolate=True)
image_5_part_2 = visual.ImageStim(
    win=win,
    name='image_5_part_2',
    image='Stimuli/White.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.12, 0.12),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0) # CHANGE PATH ACCORDINGLY
image_5 = visual.ImageStim(
    win=win,
    name='image_5',
    image='Stimuli/Texture_5.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.12, 0.12),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0) # CHANGE PATH ACCORDINGLY
rest_5 = visual.TextStim(win=win, name='rest_5',
    text='Rest',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0,
    color='black', colorSpace='rgb', opacity=None,
    languageStyle='LTR', flipHoriz=True,
    depth=-5.0);

# --- Initialize components for Routine "texture_6" ---
key_resp_8 = keyboard.Keyboard()
# Run 'Begin Experiment' code from code_6


fixation_6 = visual.ShapeStim(
    win=win, name='fixation_6', vertices='cross',
    size=(0.1, 0.1),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='white',
    opacity=None, depth=-2.0, interpolate=True)
image_2_part = visual.ImageStim(
    win=win,
    name='image_2_part',
    image='Stimuli/White.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.12, 0.12),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0) # CHANGE PATH ACCORDINGLY
image_6 = visual.ImageStim(
    win=win,
    name='image_6',
    image='Stimuli/Texture_6.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.12, 0.12),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0) # CHANGE PATH ACCORDINGLY
rest_6 = visual.TextStim(win=win, name='rest_6',
    text='Rest',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0,
    color='black', colorSpace='rgb', opacity=None,
    languageStyle='LTR', flipHoriz=True,
    depth=-5.0);

# --- Initialize components for Routine "experiment2" ---
key_resp_9 = keyboard.Keyboard()
# Run 'Begin Experiment' code from code_7


fixation_7 = visual.ShapeStim(
    win=win, name='fixation_7', vertices='cross',
    size=(0.1, 0.1),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='white',
    opacity=None, depth=-2.0, interpolate=True)
image_7_part_2 = visual.ImageStim(
    win=win,
    name='image_7_part_2',
    image='Stimuli/Checkerboard_2.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.12, 0.12),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0) # CHANGE PATH ACCORDINGLY
image_7 = visual.ImageStim(
    win=win,
    name='image_7',
    image='Stimuli/Checkerboard_1.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.12, 0.12),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0) # CHANGE PATH ACCORDINGLY
rest_7 = visual.TextStim(win=win, name='rest_7',
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
    trials_1.addData('key_resp_2.keys',key_resp_2.keys)
    if key_resp_2.keys != None:  # we had a response
        trials_1.addData('key_resp_2.rt', key_resp_2.rt)
    # the Routine "wait" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 5.0 repeats of 'trials_1'


# set up handler to look after randomisation of conditions etc
trials_3 = data.TrialHandler(nReps=2.0, method='random',
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
    currentLoop = trials_3
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
    if thisTrial_3 != None:
        for paramName in thisTrial_3:
            exec('{} = thisTrial_3[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "texture_1" ---
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
    texture_1Components = [key_resp_3, fixation, image_1_part_2, image, rest]
    for thisComponent in texture_1Components:
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
    
    # --- Run Routine "texture_1" ---
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
            image.setOpacity((frameN % 8) >= 4, log=False)
        
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
        for thisComponent in texture_1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "texture_1" ---
    for thisComponent in texture_1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_3.keys in ['', [], None]:  # No response was made
        key_resp_3.keys = None
    trials_3.addData('key_resp_3.keys',key_resp_3.keys)
    if key_resp_3.keys != None:  # we had a response
        trials_3.addData('key_resp_3.rt', key_resp_3.rt)
    # the Routine "texture_1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "texture_2" ---
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
    texture_2Components = [key_resp_4, fixation_2, image_2_part_2, image_2, rest_2]
    for thisComponent in texture_2Components:
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
    
    # --- Run Routine "texture_2" ---
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
            image_2.setOpacity((frameN % 6) >= 3, log=False)
        
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
        for thisComponent in texture_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "texture_2" ---
    for thisComponent in texture_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_4.keys in ['', [], None]:  # No response was made
        key_resp_4.keys = None
    trials_3.addData('key_resp_4.keys',key_resp_4.keys)
    if key_resp_4.keys != None:  # we had a response
        trials_3.addData('key_resp_4.rt', key_resp_4.rt)
    # the Routine "texture_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "texture_3" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    key_resp_5.keys = []
    key_resp_5.rt = []
    _key_resp_5_allKeys = []
    # Run 'Begin Routine' code from code_3
    keyNo = 0
    EndTrial = False
    
    fixation_3.setFillColor('black')
    # keep track of which components have finished
    texture_3Components = [key_resp_5, fixation_3, image_3_part_2, image_3, rest_3]
    for thisComponent in texture_3Components:
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
    
    # --- Run Routine "texture_3" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *key_resp_5* updates
        waitOnFlip = False
        if key_resp_5.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_5.frameNStart = frameN  # exact frame index
            key_resp_5.tStart = t  # local t and not account for scr refresh
            key_resp_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_5.started')
            key_resp_5.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_5.status == STARTED:
            if bool(EndTrial == True):
                # keep track of stop time/frame for later
                key_resp_5.tStop = t  # not accounting for scr refresh
                key_resp_5.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_5.stopped')
                key_resp_5.status = FINISHED
        if key_resp_5.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_5.getKeys(keyList=['s'], waitRelease=False)
            _key_resp_5_allKeys.extend(theseKeys)
            if 's' in theseKeys:
                keyNo += 1
            if len(_key_resp_5_allKeys):
                key_resp_5.keys = [key.name for key in _key_resp_5_allKeys]  # storing all keys
                key_resp_5.rt = [key.rt for key in _key_resp_5_allKeys]
        
        # *fixation_3* updates
        if fixation_3.status == NOT_STARTED and keyNo == 1:
            # keep track of start time/frame for later
            fixation_3.frameNStart = frameN  # exact frame index
            fixation_3.tStart = t  # local t and not account for scr refresh
            fixation_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'fixation_3.started')
            fixation_3.setAutoDraw(True)
        if fixation_3.status == STARTED:
            if bool(keyNo == 11):
                # keep track of stop time/frame for later
                fixation_3.tStop = t  # not accounting for scr refresh
                fixation_3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixation_3.stopped')
                fixation_3.setAutoDraw(False)
        
        # *image_3_part_2* updates
        if image_3_part_2.status == NOT_STARTED and keyNo == 11:
            # keep track of start time/frame for later
            image_3_part_2.frameNStart = frameN  # exact frame index
            image_3_part_2.tStart = t  # local t and not account for scr refresh
            image_3_part_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_3_part_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image_3_part_2.started')
            image_3_part_2.setAutoDraw(True)
        if image_3_part_2.status == STARTED:
            if bool(keyNo == 26):
                # keep track of stop time/frame for later
                image_3_part_2.tStop = t  # not accounting for scr refresh
                image_3_part_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_3_part_2.stopped')
                image_3_part_2.setAutoDraw(False)
        
        # *image_3* updates
        if image_3.status == NOT_STARTED and keyNo == 11:
            # keep track of start time/frame for later
            image_3.frameNStart = frameN  # exact frame index
            image_3.tStart = t  # local t and not account for scr refresh
            image_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image_3.started')
            image_3.setAutoDraw(True)
        if image_3.status == STARTED:
            if bool(keyNo == 26):
                # keep track of stop time/frame for later
                image_3.tStop = t  # not accounting for scr refresh
                image_3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_3.stopped')
                image_3.setAutoDraw(False)
        if image_3.status == STARTED:  # only update if drawing
            image_3.setOpacity((frameN % 4) >= 2, log=False)
        
        # *rest_3* updates
        if rest_3.status == NOT_STARTED and keyNo == 26:
            # keep track of start time/frame for later
            rest_3.frameNStart = frameN  # exact frame index
            rest_3.tStart = t  # local t and not account for scr refresh
            rest_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rest_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'rest_3.started')
            rest_3.setAutoDraw(True)
        if rest_3.status == STARTED:
            if bool(keyNo == 27):
                # keep track of stop time/frame for later
                rest_3.tStop = t  # not accounting for scr refresh
                rest_3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'rest_3.stopped')
                rest_3.setAutoDraw(False)
                EndTrial = True
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in texture_3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "texture_3" ---
    for thisComponent in texture_3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_5.keys in ['', [], None]:  # No response was made
        key_resp_5.keys = None
    trials_3.addData('key_resp_5.keys',key_resp_5.keys)
    if key_resp_5.keys != None:  # we had a response
        trials_3.addData('key_resp_5.rt', key_resp_5.rt)
    # the Routine "texture_3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "texture_4" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    key_resp_6.keys = []
    key_resp_6.rt = []
    _key_resp_6_allKeys = []
    # Run 'Begin Routine' code from code_4
    keyNo = 0
    EndTrial = False
    
    fixation_4.setFillColor('black')
    # keep track of which components have finished
    texture_4Components = [key_resp_6, fixation_4, image_4_part_2, image_4, rest_4]
    for thisComponent in texture_4Components:
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
    
    # --- Run Routine "texture_4" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *key_resp_6* updates
        waitOnFlip = False
        if key_resp_6.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_6.frameNStart = frameN  # exact frame index
            key_resp_6.tStart = t  # local t and not account for scr refresh
            key_resp_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_6.started')
            key_resp_6.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_6.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_6.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_6.status == STARTED:
            if bool(EndTrial == True):
                # keep track of stop time/frame for later
                key_resp_6.tStop = t  # not accounting for scr refresh
                key_resp_6.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_6.stopped')
                key_resp_6.status = FINISHED
        if key_resp_6.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_6.getKeys(keyList=['s'], waitRelease=False)
            _key_resp_6_allKeys.extend(theseKeys)
            if 's' in theseKeys:
                keyNo += 1
            if len(_key_resp_6_allKeys):
                key_resp_6.keys = [key.name for key in _key_resp_6_allKeys]  # storing all keys
                key_resp_6.rt = [key.rt for key in _key_resp_6_allKeys]
        
        # *fixation_4* updates
        if fixation_4.status == NOT_STARTED and keyNo == 1:
            # keep track of start time/frame for later
            fixation_4.frameNStart = frameN  # exact frame index
            fixation_4.tStart = t  # local t and not account for scr refresh
            fixation_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'fixation_4.started')
            fixation_4.setAutoDraw(True)
        if fixation_4.status == STARTED:
            if bool(keyNo == 11):
                # keep track of stop time/frame for later
                fixation_4.tStop = t  # not accounting for scr refresh
                fixation_4.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixation_4.stopped')
                fixation_4.setAutoDraw(False)
        
        # *image_4_part_2* updates
        if image_4_part_2.status == NOT_STARTED and keyNo == 11:
            # keep track of start time/frame for later
            image_4_part_2.frameNStart = frameN  # exact frame index
            image_4_part_2.tStart = t  # local t and not account for scr refresh
            image_4_part_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_4_part_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image_4_part_2.started')
            image_4_part_2.setAutoDraw(True)
        if image_4_part_2.status == STARTED:
            if bool(keyNo == 26):
                # keep track of stop time/frame for later
                image_4_part_2.tStop = t  # not accounting for scr refresh
                image_4_part_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_4_part_2.stopped')
                image_4_part_2.setAutoDraw(False)
        
        # *image_4* updates
        if image_4.status == NOT_STARTED and keyNo == 11:
            # keep track of start time/frame for later
            image_4.frameNStart = frameN  # exact frame index
            image_4.tStart = t  # local t and not account for scr refresh
            image_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image_4.started')
            image_4.setAutoDraw(True)
        if image_4.status == STARTED:
            if bool(keyNo == 26):
                # keep track of stop time/frame for later
                image_4.tStop = t  # not accounting for scr refresh
                image_4.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_4.stopped')
                image_4.setAutoDraw(False)
        if image_4.status == STARTED:  # only update if drawing
            image_4.setOpacity((frameN % 3) >= 1.5, log=False)
        
        # *rest_4* updates
        if rest_4.status == NOT_STARTED and keyNo == 26:
            # keep track of start time/frame for later
            rest_4.frameNStart = frameN  # exact frame index
            rest_4.tStart = t  # local t and not account for scr refresh
            rest_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rest_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'rest_4.started')
            rest_4.setAutoDraw(True)
        if rest_4.status == STARTED:
            if bool(keyNo == 27):
                # keep track of stop time/frame for later
                rest_4.tStop = t  # not accounting for scr refresh
                rest_4.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'rest_4.stopped')
                rest_4.setAutoDraw(False)
                EndTrial = True
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in texture_4Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "texture_4" ---
    for thisComponent in texture_4Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_6.keys in ['', [], None]:  # No response was made
        key_resp_6.keys = None
    trials_3.addData('key_resp_6.keys',key_resp_6.keys)
    if key_resp_6.keys != None:  # we had a response
        trials_3.addData('key_resp_6.rt', key_resp_6.rt)
    # the Routine "texture_4" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "texture_5" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    key_resp_7.keys = []
    key_resp_7.rt = []
    _key_resp_7_allKeys = []
    # Run 'Begin Routine' code from code_5
    keyNo = 0
    EndTrial = False
    
    fixation_5.setFillColor('black')
    # keep track of which components have finished
    texture_5Components = [key_resp_7, fixation_5, image_5_part_2, image_5, rest_5]
    for thisComponent in texture_5Components:
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
    
    # --- Run Routine "texture_5" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *key_resp_7* updates
        waitOnFlip = False
        if key_resp_7.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_7.frameNStart = frameN  # exact frame index
            key_resp_7.tStart = t  # local t and not account for scr refresh
            key_resp_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_7, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_7.started')
            key_resp_7.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_7.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_7.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_7.status == STARTED:
            if bool(EndTrial == True):
                # keep track of stop time/frame for later
                key_resp_7.tStop = t  # not accounting for scr refresh
                key_resp_7.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_7.stopped')
                key_resp_7.status = FINISHED
        if key_resp_7.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_7.getKeys(keyList=['s'], waitRelease=False)
            _key_resp_7_allKeys.extend(theseKeys)
            if 's' in theseKeys:
                keyNo += 1
            if len(_key_resp_7_allKeys):
                key_resp_7.keys = [key.name for key in _key_resp_7_allKeys]  # storing all keys
                key_resp_7.rt = [key.rt for key in _key_resp_7_allKeys]
        
        # *fixation_5* updates
        if fixation_5.status == NOT_STARTED and keyNo == 1:
            # keep track of start time/frame for later
            fixation_5.frameNStart = frameN  # exact frame index
            fixation_5.tStart = t  # local t and not account for scr refresh
            fixation_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'fixation_5.started')
            fixation_5.setAutoDraw(True)
        if fixation_5.status == STARTED:
            if bool(keyNo == 11):
                # keep track of stop time/frame for later
                fixation_5.tStop = t  # not accounting for scr refresh
                fixation_5.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixation_5.stopped')
                fixation_5.setAutoDraw(False)
        
        # *image_5_part_2* updates
        if image_5_part_2.status == NOT_STARTED and keyNo == 11:
            # keep track of start time/frame for later
            image_5_part_2.frameNStart = frameN  # exact frame index
            image_5_part_2.tStart = t  # local t and not account for scr refresh
            image_5_part_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_5_part_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image_5_part_2.started')
            image_5_part_2.setAutoDraw(True)
        if image_5_part_2.status == STARTED:
            if bool(keyNo == 26):
                # keep track of stop time/frame for later
                image_5_part_2.tStop = t  # not accounting for scr refresh
                image_5_part_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_5_part_2.stopped')
                image_5_part_2.setAutoDraw(False)
        
        # *image_5* updates
        if image_5.status == NOT_STARTED and keyNo == 11:
            # keep track of start time/frame for later
            image_5.frameNStart = frameN  # exact frame index
            image_5.tStart = t  # local t and not account for scr refresh
            image_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image_5.started')
            image_5.setAutoDraw(True)
        if image_5.status == STARTED:
            if bool(keyNo == 26):
                # keep track of stop time/frame for later
                image_5.tStop = t  # not accounting for scr refresh
                image_5.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_5.stopped')
                image_5.setAutoDraw(False)
        if image_5.status == STARTED:  # only update if drawing
            image_5.setOpacity((frameN % 2.5) >= 1.25, log=False)
        
        # *rest_5* updates
        if rest_5.status == NOT_STARTED and keyNo == 26:
            # keep track of start time/frame for later
            rest_5.frameNStart = frameN  # exact frame index
            rest_5.tStart = t  # local t and not account for scr refresh
            rest_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rest_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'rest_5.started')
            rest_5.setAutoDraw(True)
        if rest_5.status == STARTED:
            if bool(keyNo == 27):
                # keep track of stop time/frame for later
                rest_5.tStop = t  # not accounting for scr refresh
                rest_5.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'rest_5.stopped')
                rest_5.setAutoDraw(False)
                EndTrial = True
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in texture_5Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "texture_5" ---
    for thisComponent in texture_5Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_7.keys in ['', [], None]:  # No response was made
        key_resp_7.keys = None
    trials_3.addData('key_resp_7.keys',key_resp_7.keys)
    if key_resp_7.keys != None:  # we had a response
        trials_3.addData('key_resp_7.rt', key_resp_7.rt)
    # the Routine "texture_5" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "texture_6" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    key_resp_8.keys = []
    key_resp_8.rt = []
    _key_resp_8_allKeys = []
    # Run 'Begin Routine' code from code_6
    keyNo = 0
    EndTrial = False
    
    fixation_6.setFillColor('black')
    # keep track of which components have finished
    texture_6Components = [key_resp_8, fixation_6, image_2_part, image_6, rest_6]
    for thisComponent in texture_6Components:
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
    
    # --- Run Routine "texture_6" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *key_resp_8* updates
        waitOnFlip = False
        if key_resp_8.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_8.frameNStart = frameN  # exact frame index
            key_resp_8.tStart = t  # local t and not account for scr refresh
            key_resp_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_8, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_8.started')
            key_resp_8.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_8.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_8.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_8.status == STARTED:
            if bool(EndTrial == True):
                # keep track of stop time/frame for later
                key_resp_8.tStop = t  # not accounting for scr refresh
                key_resp_8.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_8.stopped')
                key_resp_8.status = FINISHED
        if key_resp_8.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_8.getKeys(keyList=['s'], waitRelease=False)
            _key_resp_8_allKeys.extend(theseKeys)
            if 's' in theseKeys:
                keyNo += 1
            if len(_key_resp_8_allKeys):
                key_resp_8.keys = [key.name for key in _key_resp_8_allKeys]  # storing all keys
                key_resp_8.rt = [key.rt for key in _key_resp_8_allKeys]
        
        # *fixation_6* updates
        if fixation_6.status == NOT_STARTED and keyNo == 1:
            # keep track of start time/frame for later
            fixation_6.frameNStart = frameN  # exact frame index
            fixation_6.tStart = t  # local t and not account for scr refresh
            fixation_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'fixation_6.started')
            fixation_6.setAutoDraw(True)
        if fixation_6.status == STARTED:
            if bool(keyNo == 11):
                # keep track of stop time/frame for later
                fixation_6.tStop = t  # not accounting for scr refresh
                fixation_6.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixation_6.stopped')
                fixation_6.setAutoDraw(False)
        
        # *image_2_part* updates
        if image_2_part.status == NOT_STARTED and keyNo == 11:
            # keep track of start time/frame for later
            image_2_part.frameNStart = frameN  # exact frame index
            image_2_part.tStart = t  # local t and not account for scr refresh
            image_2_part.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_2_part, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image_2_part.started')
            image_2_part.setAutoDraw(True)
        if image_2_part.status == STARTED:
            if bool(keyNo == 26):
                # keep track of stop time/frame for later
                image_2_part.tStop = t  # not accounting for scr refresh
                image_2_part.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_2_part.stopped')
                image_2_part.setAutoDraw(False)
        
        # *image_6* updates
        if image_6.status == NOT_STARTED and keyNo == 11:
            # keep track of start time/frame for later
            image_6.frameNStart = frameN  # exact frame index
            image_6.tStart = t  # local t and not account for scr refresh
            image_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image_6.started')
            image_6.setAutoDraw(True)
        if image_6.status == STARTED:
            if bool(keyNo == 26):
                # keep track of stop time/frame for later
                image_6.tStop = t  # not accounting for scr refresh
                image_6.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_6.stopped')
                image_6.setAutoDraw(False)
        if image_6.status == STARTED:  # only update if drawing
            image_6.setOpacity((frameN % 2) >= 1, log=False)
        
        # *rest_6* updates
        if rest_6.status == NOT_STARTED and keyNo == 26:
            # keep track of start time/frame for later
            rest_6.frameNStart = frameN  # exact frame index
            rest_6.tStart = t  # local t and not account for scr refresh
            rest_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rest_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'rest_6.started')
            rest_6.setAutoDraw(True)
        if rest_6.status == STARTED:
            if bool(keyNo == 27):
                # keep track of stop time/frame for later
                rest_6.tStop = t  # not accounting for scr refresh
                rest_6.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'rest_6.stopped')
                rest_6.setAutoDraw(False)
                EndTrial = True
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in texture_6Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "texture_6" ---
    for thisComponent in texture_6Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_8.keys in ['', [], None]:  # No response was made
        key_resp_8.keys = None
    trials_3.addData('key_resp_8.keys',key_resp_8.keys)
    if key_resp_8.keys != None:  # we had a response
        trials_3.addData('key_resp_8.rt', key_resp_8.rt)
    # the Routine "texture_6" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
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
        
        # --- Prepare to start Routine "experiment2" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        key_resp_9.keys = []
        key_resp_9.rt = []
        _key_resp_9_allKeys = []
        # Run 'Begin Routine' code from code_7
        keyNo = 0
        EndTrial = False
        
        fixation_7.setFillColor('black')
        # keep track of which components have finished
        experiment2Components = [key_resp_9, fixation_7, image_7_part_2, image_7, rest_7]
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
            
            # *key_resp_9* updates
            waitOnFlip = False
            if key_resp_9.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_9.frameNStart = frameN  # exact frame index
                key_resp_9.tStart = t  # local t and not account for scr refresh
                key_resp_9.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_9, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_9.started')
                key_resp_9.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_9.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_9.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_9.status == STARTED:
                if bool(EndTrial == True):
                    # keep track of stop time/frame for later
                    key_resp_9.tStop = t  # not accounting for scr refresh
                    key_resp_9.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'key_resp_9.stopped')
                    key_resp_9.status = FINISHED
            if key_resp_9.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_9.getKeys(keyList=['s'], waitRelease=False)
                _key_resp_9_allKeys.extend(theseKeys)
                if 's' in theseKeys:
                    keyNo += 1
                if len(_key_resp_9_allKeys):
                    key_resp_9.keys = [key.name for key in _key_resp_9_allKeys]  # storing all keys
                    key_resp_9.rt = [key.rt for key in _key_resp_9_allKeys]
            
            # *fixation_7* updates
            if fixation_7.status == NOT_STARTED and keyNo == 1:
                # keep track of start time/frame for later
                fixation_7.frameNStart = frameN  # exact frame index
                fixation_7.tStart = t  # local t and not account for scr refresh
                fixation_7.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixation_7, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixation_7.started')
                fixation_7.setAutoDraw(True)
            if fixation_7.status == STARTED:
                if bool(keyNo == 11):
                    # keep track of stop time/frame for later
                    fixation_7.tStop = t  # not accounting for scr refresh
                    fixation_7.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'fixation_7.stopped')
                    fixation_7.setAutoDraw(False)
            
            # *image_7_part_2* updates
            if image_7_part_2.status == NOT_STARTED and keyNo == 11:
                # keep track of start time/frame for later
                image_7_part_2.frameNStart = frameN  # exact frame index
                image_7_part_2.tStart = t  # local t and not account for scr refresh
                image_7_part_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_7_part_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_7_part_2.started')
                image_7_part_2.setAutoDraw(True)
            if image_7_part_2.status == STARTED:
                if bool(keyNo == 26):
                    # keep track of stop time/frame for later
                    image_7_part_2.tStop = t  # not accounting for scr refresh
                    image_7_part_2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image_7_part_2.stopped')
                    image_7_part_2.setAutoDraw(False)
            
            # *image_7* updates
            if image_7.status == NOT_STARTED and keyNo == 11:
                # keep track of start time/frame for later
                image_7.frameNStart = frameN  # exact frame index
                image_7.tStart = t  # local t and not account for scr refresh
                image_7.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_7, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_7.started')
                image_7.setAutoDraw(True)
            if image_7.status == STARTED:
                if bool(keyNo == 26):
                    # keep track of stop time/frame for later
                    image_7.tStop = t  # not accounting for scr refresh
                    image_7.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image_7.stopped')
                    image_7.setAutoDraw(False)
            if image_7.status == STARTED:  # only update if drawing
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
                image_7.setOpacity(frame_seq, log=False)
            
            # *rest_7* updates
            if rest_7.status == NOT_STARTED and keyNo == 26:
                # keep track of start time/frame for later
                rest_7.frameNStart = frameN  # exact frame index
                rest_7.tStart = t  # local t and not account for scr refresh
                rest_7.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(rest_7, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'rest_7.started')
                rest_7.setAutoDraw(True)
            if rest_7.status == STARTED:
                if bool(keyNo == 27):
                    # keep track of stop time/frame for later
                    rest_7.tStop = t  # not accounting for scr refresh
                    rest_7.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'rest_7.stopped')
                    rest_7.setAutoDraw(False)
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
        if key_resp_9.keys in ['', [], None]:  # No response was made
            key_resp_9.keys = None
        trials_2.addData('key_resp_9.keys',key_resp_9.keys)
        if key_resp_9.keys != None:  # we had a response
            trials_2.addData('key_resp_9.rt', key_resp_9.rt)
        # the Routine "experiment2" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 6.0 repeats of 'trials_2'
    
    thisExp.nextEntry()
    
# completed 2.0 repeats of 'trials_3'


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
