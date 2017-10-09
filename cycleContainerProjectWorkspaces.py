#!/usr/bin/python3
# -*- coding: utf-8 -*-
import subprocess
import json
import sys
import re
from necessaryFuncs import *

proc_out = subprocess.run(['i3-msg', '-t', 'get_workspaces'], stdout=subprocess.PIPE)
wkList = json.loads(proc_out.stdout.decode('utf-8'))

allWKNames = getWKNames(wkList)

currentWK = getFocusedWK(wkList)

currentProj = getProjectFromWKName(currentWK)

if currentProj is None:
    sys.exit(1)

currentProjWKs = getWKNamesFromProj(wkList, currentProj)
  
thisWKPos = currentProjWKs.index(currentWK)

newWKPos = thisWKPos + 1
if newWKPos == len(currentProjWKs):
    newWKPos = 0

commandToRun = ['i3-msg', 'move container to workspace ' + currentProjWKs[newWKPos]]

subprocess.call(commandToRun)
