#!/usr/bin/env python3

'''
This checker script evaulates common scenarios for Linux system administrators.
This helps to prepare for industry exams by learning with the system and validate the results.

The scenario file can be extended with custom scenarios. It is stored as a JSON document.
The followng sample shows the overall structure of the document. Each scenario has a validation
which can be either shell based or python based. The execution should return a number which
signifies the achieved points (where the maximum is defined by the points attribute).abs

For overall evaluation all points are considered and minimum goal of 80% is applied.

[
    {
        "name": "",
        "description": "",
        "points": 0,
        "validation": {
            "type": "(shell|python)",
            "code": ""
        }
    }
]
'''

import os
import json
import subprocess

class bgcolors:
    OK = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

def printScenarioHeader(scenario):
    print("Validating {} - {}: ".format(scenario["name"], scenario["description"]), end = "")

def printScenarioEvaluation(hitPoints, maxPoints, skip = False):
    if skip is True:
        print("{}skipped{} (this scenario can only be run on a VM)".format(bgcolors.WARNING, bgcolors.ENDC))
    else:
        if hitPoints == maxPoints:
            print("{}passed{} ({}/{})".format(bgcolors.OK, bgcolors.ENDC, hitPoints, maxPoints))
        else:
            print("{}failed{} ({}/{})".format(bgcolors.FAIL, bgcolors.ENDC, hitPoints, maxPoints))

def printSummary(hitPoints, maxPoints):
    ratio = hitPoints / maxPoints * 100

    print("", end = "\n")
    print("FINAL RESULT: ", end = "")

    if ratio >= 80:
        print("{}passed{} ({}/{})".format(bgcolors.OK, bgcolors.ENDC, hitPoints, maxPoints))
    else:
        print("{}failed{} ({}/{})".format(bgcolors.FAIL, bgcolors.ENDC, hitPoints, maxPoints))

def evaluateScenario(scenario):
    points = scenario["points"]
    validation = scenario["validation"]

    if validation["type"] == "python":
        print("not implemented yet")
    elif validation["type"] == "shell":
        code = validation["code"]
        devnull = open(os.devnull, 'w')
        returncode = subprocess.call(code, shell = True, stdout = devnull, stderr = devnull)
        devnull.close()

    if returncode == 0:
        return points

    return 0

if os.path.isfile('scenarios.json'):
    if os.path.isfile("/.dockerenv"):
        isContainer = True;

    # Load scenarios
    with open('scenarios.json') as file:
        data = json.load(file)

    # Iterate screnarios and evaluate results
    hitPoints = 0
    maxPoints = 0

    for scenario in data:
        printScenarioHeader(scenario)

        if ("constraints" in scenario and scenario["constraints"] == 1 and isContainer is False) or isContainer is True:
            printScenarioEvaluation(0, scenario["points"])

            hitPoints += evaluateScenario(scenario)
            maxPoints += scenario["points"]
        else:
            printScenarioEvaluation(0, 0, True)

    # Print results
    printSummary(hitPoints, maxPoints)
else:
    print("Scenarios could not be found")
