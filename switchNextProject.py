#!/usr/bin/python3
# -*- coding: utf-8 -*-
import subprocess
import json
import sys
import re
from necessaryFuncs import *

proc_out = subprocess.run(['i3-msg', '-t', 'get_workspaces'], stdout=subprocess.PIPE)
wkList = json.loads(proc_out.stdout.decode('utf-8'))

focWkName = getFocusedWK(wkList)

allProjectNames = getListOfProjects(wkList)

if (len(allProjectNames) == 0) or (allProjectNames is None):
  sys.exit(1)

currentProjName = getProjectFromWKName(focWkName)

if currentProjName is None:
  nextProjIndex = 0
else:
  nextProjIndex = allProjectNames.index(currentProjName)

  if nextProjIndex == (len(allProjectNames) - 1):
    nextProjIndex = 0
  else:
    nextProjIndex = nextProjIndex + 1

nxtProjWks = getWKNamesFromProj(wkList, allProjectNames[nextProjIndex])

visWks = getVisibleWKs(wkList)

wksToMakeVisible = list(set(nxtProjWks) - set(visWks))

focOutput = getOutputForWK(wkList, focWkName)
focOutputWks = getWorkspacesOnOutput(wkList, focOutput)
wkToBeFocused = list(set(focOutputWks).intersection(nxtProjWks))

parCommToRun = ['workspace ' + x for x in wksToMakeVisible]
if len(wkToBeFocused) > 0 and wksToMakeVisible[-1] != wkToBeFocused[0]:
    parCommToRun.append('workspace ' + wkToBeFocused[0])

commandToRun = ["i3-msg", '; '.join(parCommToRun)]

subprocess.call(commandToRun)

