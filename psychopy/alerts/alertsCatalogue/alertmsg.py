#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file was generated by generateAlertmsg.py.
# Following strings are used to localize alerts.
# Rebuild this file if alert messages in *.yaml files are modified.

from psychopy.localization import _translate

# Alert 2115
_translate(
    "Your stimulus size exceeds the {dimension} dimension of your window.")

# Alert 2120
_translate(
    "Your stimulus size is smaller than 1 pixel ({dimension} dimension).")

# Alert 2155
_translate(
    "Your stimulus position exceeds the {dimension} dimension of your window.")

# Alert 3110
_translate(
    "Your stimulus {type} time of {time} is less than a screen refresh for a {Hz}Hz monitor.")

# Alert 3115
_translate(
    "Your stimulus {type} time of {time} seconds cannot be accurately presented for {time} on a {Hz}Hz monitor.")

# Alert 4051
_translate(
    "Experiment was built in a future version of PsychoPy ({version}), we recommend either updating PsychoPy or changing the \"Use Version\" setting in Experiment Settings to this version.")

# Alert 4052
_translate(
    "Experiment was built in a past version of PsychoPy ({version}), saving it in this version may add parameters which cannot be parsed.")

# Alert 4105
_translate(
    "Your stimulus start {type} exceeds the stop {type}. Consider using a {type} duration.")

# Alert 4115
_translate(
    "Your stimulus {type} type {frameType} must be expressed as a whole number.")

# Alert 4205
_translate(
    "Python Syntax Error in '{codeTab}' tab. See '{code}' on line number {lineNumber} of the '{codeTab}' tab.")

# Alert 4210
_translate(
    "JavaScript Syntax Error in '{codeTab}' tab. See '{lineNumber}' in the '{codeTab}' tab.")

# Alert 4305
_translate(
    "The component {name} is currently disabled and will not be written to your experiment script.")

# Alert 4310
_translate("Cannot calculate parameter.")

# Alert 4315
_translate(
    "Builder cannot interpret value \"{param.val}\" of {param.label} for {component.type} component \"{component.params[name].val}\" as a dollar sign has been used incorrectly.")

# Alert 4320
_translate(
    "Font `{param.val}` not found locally, will check Google Fonts on next run.")

# Alert 4325
_translate(
    "Font `{font} {style}` not available in weight `{weight}`, component `{name}` will default to Open Sans Regular.")

# Alert 4330
_translate(
    "Recording device '{device}' not found, using default device instead.")

# Alert 4405
_translate(
    "Editable textbox component {textbox} and keyboard component {keyboard} in the same routine may compete for keypresses")

# Alert 4505
_translate("Experiment includes components or routines which use eyetracking, but no eye tracker is configured.")

# Alert 4510
_translate(
    "A {eyetracker} eye tracker has been configured, but no calibration routine is present.")

# Alert 4520
_translate("As {brand} eyetrackers do not support animations in their calibration routine, animation values have not been used in your calibration routine.")

# Alert 4530
_translate("Eyetrackers by {brand} do not support manual pacing")

# Alert 4540
_translate(
    "Window mode is set to be windowed, but eyetracking requires the window to be full screen.")

# Alert 4545
_translate(
    "A monitor config is required for accurate eyetracking measurements, but none was found.")

# Alert 4550
_translate(
    "Region Of Interest component {name} is not accompanied by an Eyetracker Record component. Without an Eyetracker Record component, eye position will not be available.")

# Alert 4605
_translate(
    "Audio transcription service \"{transcriber}\" is not supported online.")

# Alert 4610
_translate(
    "Audio transcription service \"{transcriber}\" is not supported offline.")

# Alert 4615
_translate(
    "Chosen transcriber '{engine}' requires an API key, please supply one in Preferences.")

# Alert 5055
_translate(
    "Device parameter of microphone component \"{name}\" will not be used online.")

# Alert 6105
_translate(
    "The file you are attempting to run does not seem to exist, the full path supplied to Runner was {path}")

# Alert 8105
_translate(
    "Color space attribute `.{colorSpaceAttrib}` is no longer in use, as colors are no longer tied to one space.")

# Alert 8110
_translate(
    "RGB attribute `.{rgbAttrib}` is no longer in use, as non-RGB colors now handle their own conversion.")
