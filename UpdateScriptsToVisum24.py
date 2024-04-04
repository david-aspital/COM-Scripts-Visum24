import glob
import os


'''
Deprecated Methods:

IVisum.Lists since 30.01.2014
Replaced by IVisum.Workbench.Lists.

IProcedures.OpenXml since 29.09.2015
Replaced by IProcedures.Open

IProcedures.SaveXml since 29.09.2015
Replaced by IProcedures.Save

IVisum.LoadNet since 16.12.2015
Replaced by IVisum.IO.LoadNet

IVisum.SaveNet since 16.12.2015
Replaced by IVisum.IO.SaveNet

IOperation.TFlowFuzzyParameters since 09.03.2017
Replaced by IOperation.DemandMatrixCorrectionParameters

ITimeProfile.VehJourneys since 15.02.2018
Replaced by ITimeProfile.VehicleJourneys

INet.VehJourneySections since 15.02.2018
Replaced by INet.VehicleJourneySections

IFunctions.AnalysisTimes since 13.05.2019
Replaced by IVisum.Net.CalendarPeriod

IODPairFilter.FilterNetworkVolumes since 16.03.2020
Replaced by IFilters.VolumeAttributeValueFilter.FilterByActiveODPairsAndPuTPaths
'''

scriptPath = "oldScripts"
newScriptPath = "newScripts"

updateDict = {
    "Visum.Lists":"Visum.Workbench.Lists",
    "Procedures.OpenXml(":"Procedures.Open(", #! Note the ( is needed here to avoid replacing OpenXmlWithOptions procedures
    "Procedures.SaveXml":"Procedures.Save",
    "Visum.LoadNet":"Visum.IO.LoadNet",
    "Visum.SaveNet":"Visum.IO.SaveNet",
    "Operation.TFlowFuzzyParameters":"Operation.DemandMatrixCorrectionParameters",
    "TimeProfile.VehJourneys":"TimeProfile.VehicleJourneys",
    "Net.VehJourneySections":"Net.VehicleJourneySections",
    "Procedures.Functions.AnalysisTimes":"Net.CalendarPeriod",
    "ODPairFilter":"VolumeAttributeValueFilter.FilterByActiveODPairsAndPuTPaths"
}


for file in glob.glob(f"{scriptPath}\*.py"):
    with open(file, "r") as f:
        script = f.read()
        for key, value in updateDict.items():
            script = script.replace(key, value)

    filename = os.path.split(file)[1]
    with open(os.path.join(newScriptPath, filename), "w") as f:
        f.write(script)


