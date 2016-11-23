from OSUT3Analysis.Configuration.configurationOptions import *
from DisappTrks.StandardAnalysis.utilities import *
import copy
import os
import re

from DisappTrks.StandardAnalysis.miniAODV2Samples import *
if os.environ["CMSSW_VERSION"].startswith ("CMSSW_8_0_"):
    print "Using datasets from miniAOD_80X_Samples since we are in " + os.environ["CMSSW_VERSION"] + "..."
    from DisappTrks.StandardAnalysis.miniAOD_80X_Samples import *
else:
    print "Using datasets from miniAODV2Samples since we are in " + os.environ["CMSSW_VERSION"] + "..."

config_file = "config_cfg.py"

InputCondorArguments = {'request_memory': '2048MB', 'request_cpus': '1'}

datasetsBkgd = [
    'QCD',
    'DYJetsToLL',
    'ZJetsToNuNu',
    'VV',
    'SingleTop',
    'TTJets',
]
datasetsBkgdForMET = copy.deepcopy(datasetsBkgd)

datasetsBkgd += 'WJetsToLNu'
datasetsBkgdForMET += 'WJetsToLNu_HT'

datasetsSig = [
    'AMSB_chargino_100GeV_10cm_76X',
    'AMSB_chargino_100GeV_100cm_76X',
    'AMSB_chargino_100GeV_1000cm_76X',
    'AMSB_chargino_100GeV_10000cm_76X',

    'AMSB_chargino_200GeV_10cm_76X',
    'AMSB_chargino_200GeV_100cm_76X',
    'AMSB_chargino_200GeV_1000cm_76X',
    'AMSB_chargino_200GeV_10000cm_76X',

    'AMSB_chargino_300GeV_10cm_76X',
    'AMSB_chargino_300GeV_100cm_76X',
    'AMSB_chargino_300GeV_1000cm_76X',
    'AMSB_chargino_300GeV_10000cm_76X',

    'AMSB_chargino_400GeV_10cm_76X',
    'AMSB_chargino_400GeV_100cm_76X',
    'AMSB_chargino_400GeV_1000cm_76X',
    'AMSB_chargino_400GeV_10000cm_76X',

    'AMSB_chargino_500GeV_10cm_76X',
    'AMSB_chargino_500GeV_100cm_76X',
    'AMSB_chargino_500GeV_1000cm_76X',
    'AMSB_chargino_500GeV_10000cm_76X',

    'AMSB_chargino_600GeV_10cm_76X',
    'AMSB_chargino_600GeV_100cm_76X',
    'AMSB_chargino_600GeV_1000cm_76X',
    'AMSB_chargino_600GeV_10000cm_76X',

    'AMSB_chargino_700GeV_10cm_76X',
    'AMSB_chargino_700GeV_100cm_76X',
    'AMSB_chargino_700GeV_1000cm_76X',
    'AMSB_chargino_700GeV_10000cm_76X',
]

if os.environ["CMSSW_VERSION"].startswith ("CMSSW_8_0_"):
    print "Switching to 80X signal samples since we are in " + os.environ["CMSSW_VERSION"] + "..."
    for i in range (0, len (datasetsSig)):
        datasetsSig[i] = re.sub (r"(.*)_76X$", r"\1_80X", datasetsSig[i])
else:
    print "Using 76X signal samples since we are in " + os.environ["CMSSW_VERSION"] + "..."

datasetsSigShort = copy.deepcopy(datasetsSig)

datasetsSigVeryShort = datasetsSig[-4:]

addLifetimeReweighting (datasetsSig)

composite_dataset_definitions["allBkgd"] = datasetsBkgd

composite_dataset_definitions['SingleTop'] = [
    'SingleTop_s_channel',
    'SingleTop_t_channel',
    'SingleTop_tW',
    'SingleTop_tbarW',
]

composite_dataset_definitions["WW"] = [
    'WWToLNuQQ',
    'WWToLNuLNu',
]

composite_dataset_definitions["VG"] = [
    'WG',
    'ZG',
]

composite_dataset_definitions["VV"] = [
    'WWToLNuQQ',
    'WWToLNuLNu',
    'WZ',
    'ZZ',
    'WG',
    'ZG',
]

types["WW"] = "bgMC"
types["WZ"] = "bgMC"
types["ZZ"] = "bgMC"
types["VG"] = "bgMC"
types["VV"] = "bgMC"
types["allBkgd"] = "bkMC"

colors["WW"] = 390
colors["WZ"] = 393
colors["ZZ"] = 397
colors["VG"] = 400
colors["VV"] = 393
colors["allBkgd"] = 601

labels["DYJetsToLL_50"] = "Z#rightarrowl^{+}l^{-}"
labels["DYJetsToNuNu"] = "Z#rightarrow#nu#bar{#nu}"
labels["WJetsToLNu"] = "W#rightarrowl#nu"
labels["WW"] = "WW"
labels["WZ"] = "WZ"
labels["ZZ"] = "ZZ"
labels["VG"] = "V#gamma"
labels["VV"] = "Diboson"
labels["allBkgd"] = "Total bkgd"