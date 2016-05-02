#!/usr/bin/env python
#
#
# Test case for Grove DRV8830
# SDL_Pi_GROVE_DRV8830 Library for Rasbperry Pi
#
# SwitchDoc Labs, March 2016
#

# imports

import sys
import time
import datetime
import random 
import SDL_Pi_GROVE_DRV8830 

import SDL_Pi_GROVE_Stepper

import subprocess



print ""
print "Test SDL_Pi_GROVE_DVR8830 Version 1.0 - SwitchDoc Labs"
print ""
print "Program Started at:"+ time.strftime("%Y-%m-%d %H:%M:%S")
print ""

i2ccommand = "sudo i2cdetect -y 1"
output = subprocess.check_output (i2ccommand,shell=True, stderr=subprocess.STDOUT )
print output

print "-----------------------------------"
print

groveMini = SDL_Pi_GROVE_DRV8830.SDL_Pi_GROVE_DRV8830()

stepper = SDL_Pi_GROVE_Stepper.SDL_Pi_GROVE_Stepper(groveMini,513)

stepper.setSpeed(100, 100)

print "fault Motor 0 %i" % (groveMini.getFault(0))

print "fault Motor 1 %i" % (groveMini.getFault(1))


for x in range (0, 513):

	print "step  %i = " % x
	stepper.step(1)
	
