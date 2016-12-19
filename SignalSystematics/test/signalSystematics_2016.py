#!/usr/bin/env python

import math
from DisappTrks.SignalSystematics.signalSystematics import *
from DisappTrks.StandardAnalysis.utilities import *
from ROOT import TCanvas, TFile
import os
import re
import sys

dirs = getUser()
masses = [100, 200, 300, 400, 500, 600, 700]
lifetimes = [10, 100, 1000, 10000]
suffix = "80X"
extraSamples = getExtraSamples (suffix)

systematic = "all"
if len (sys.argv) > 1:
    systematic = sys.argv[1]
systematic = systematic.upper ()

if systematic == "PILEUP" or systematic == "ALL":

    print "********************************************************************************"
    print "evaluating pileup systematic (2016B & 2016C)"
    print "--------------------------------------------------------------------------------"

    fout = open (os.environ["CMSSW_BASE"] + "/src/DisappTrks/SignalSystematics/data/systematic_values__pileup_2016BC.txt", "w")

    pileupSystematic_v3 = PileupSystematic (masses, lifetimes)
    pileupSystematic_v3.addFout (fout)
    pileupSystematic_v3.addExtraSamples (extraSamples)
    pileupSystematic_v3.addChannel  ("PileupCentral",  "DisTrkSelection",  suffix,  dirs['Andrew']+"2016_ICHEP/disappearingTracks_signal_weightedToBC")
    pileupSystematic_v3.addChannel  ("PileupDown",     "DisTrkSelection",  suffix,  dirs['Andrew']+"2016_ICHEP/disappearingTracks_signal_weightedToBC_puDown")
    pileupSystematic_v3.addChannel  ("PileupUp",       "DisTrkSelection",  suffix,  dirs['Andrew']+"2016_ICHEP/disappearingTracks_signal_weightedToBC_puUp")
    pileupSystematic_v3.printSystematic ()

    print "********************************************************************************"

    fout.close ()

    print "********************************************************************************"
    print "evaluating pileup systematic (2016D)"
    print "--------------------------------------------------------------------------------"

    fout = open (os.environ["CMSSW_BASE"] + "/src/DisappTrks/SignalSystematics/data/systematic_values__pileup_2016D.txt", "w")

    pileupSystematic_v4 = PileupSystematic (masses, lifetimes)
    pileupSystematic_v4.addFout (fout)
    pileupSystematic_v4.addExtraSamples (extraSamples)
    pileupSystematic_v4.addChannel  ("PileupCentral",  "DisTrkSelection",  suffix,  dirs['Andrew']+"2016_ICHEP/disappearingTracks_signal_weightedToD")
    pileupSystematic_v4.addChannel  ("PileupDown",     "DisTrkSelection",  suffix,  dirs['Andrew']+"2016_ICHEP/disappearingTracks_signal_weightedToD_puDown")
    pileupSystematic_v4.addChannel  ("PileupUp",       "DisTrkSelection",  suffix,  dirs['Andrew']+"2016_ICHEP/disappearingTracks_signal_weightedToD_puUp")
    pileupSystematic_v4.printSystematic ()

    print "********************************************************************************"

    fout.close ()

if systematic == "MET" or systematic == "ALL":

    print "********************************************************************************"
    print "evaluating met systematics"
    print "--------------------------------------------------------------------------------"

    metVaryTypes = [
        'JetRes',
        'JetEn',
        'ElectronEn',
        'TauEn',
        'UnclusteredEn',
        'PhotonEn',
    ]

    metSystematic = MetSystematic (masses, lifetimes)
    metSystematic.addExtraSamples (extraSamples)
    metSystematic.addChannel ("central", "DisTrkNoMet", suffix, dirs['Andrew']+"2016_ICHEP/jetSystematics")
    metSystematic.addChannel ("down",    "DisTrkNoMet", suffix, dirs['Andrew']+"2016_ICHEP/jetSystematics")
    metSystematic.addChannel ("up",      "DisTrkNoMet", suffix, dirs['Andrew']+"2016_ICHEP/jetSystematics")
    metSystematic.addMetTypes (metVaryTypes)
    metSystematic.setMetCut (100.0)
    metSystematic.setFoutNames (os.environ["CMSSW_BASE"] + "/src/DisappTrks/SignalSystematics/data/systematic_values__metVary", "2016.txt")
    metSystematic.printSystematic ()

    print "********************************************************************************"

    print "\n\n"

if systematic == "JEC" or systematic == "ALL":

    print "********************************************************************************"
    print "evaluating JEC systematic"
    print "--------------------------------------------------------------------------------"

    fout = open (os.environ["CMSSW_BASE"] + "/src/DisappTrks/SignalSystematics/data/systematic_values__jec_2016.txt", "w")

    jecSystematic = YieldSystematic (masses, lifetimes)
    jecSystematic.addFout (fout)
    jecSystematic.addExtraSamples (extraSamples)
    jecSystematic.addChannel  ("central",  "disTrkSelectionSmearedJets",         suffix,  dirs['Andrew']+"2016_ICHEP/jetSystematics")
    jecSystematic.addChannel  ("down",     "disTrkSelectionSmearedJetsJECUp",    suffix,  dirs['Andrew']+"2016_ICHEP/jetSystematics")
    jecSystematic.addChannel  ("up",       "disTrkSelectionSmearedJetsJECDown",  suffix,  dirs['Andrew']+"2016_ICHEP/jetSystematics")
    jecSystematic.printSystematic ()

    print "********************************************************************************"

    fout.close ()

    print "\n\n"

if systematic == "JER" or systematic == "ALL":

    print "********************************************************************************"
    print "evaluating JER systematic"
    print "--------------------------------------------------------------------------------"

    fout = open (os.environ["CMSSW_BASE"] + "/src/DisappTrks/SignalSystematics/data/systematic_values__jer_2016.txt", "w")

    jerSystematic = YieldSystematic (masses, lifetimes)
    jerSystematic.addFout (fout)
    jerSystematic.addExtraSamples (extraSamples)
    jerSystematic.addChannel  ("central", "disTrkSelectionSmearedJets",      suffix,  dirs['Andrew']+"2016_ICHEP/jetSystematics")
    jerSystematic.addChannel  ("up",      "disTrkSelectionSmearedJetsUp",    suffix,  dirs['Andrew']+"2016_ICHEP/jetSystematics")
    jerSystematic.addChannel  ("down",    "disTrkSelectionSmearedJetsDown",  suffix,  dirs['Andrew']+"2016_ICHEP/jetSystematics")
    jerSystematic.printSystematic ()

    print "********************************************************************************"

    fout.close ()

    print "\n\n"

if systematic == "ISR" or systematic == "ALL":

    print "********************************************************************************"
    print "evaluating ISR systematic"
    print "--------------------------------------------------------------------------------"

    fout = open(os.environ["CMSSW_BASE"] + "/src/DisappTrks/SignalSystematics/data/systematic_values__isr_2016.txt", "w")

    isrSystematic = YieldSystematic (masses, lifetimes)
    isrSystematic.addFout (fout)
    isrSystematic.addExtraSamples (extraSamples)
    isrSystematic.addChannel ("central", "disTrkSelectionSmearedJets", suffix, dirs['Brian']+"signalCentralValue_80X")
    isrSystematic.addChannel ("up",      "disTrkSelectionSmearedJets", suffix, dirs['Brian']+"isrSystematic_80X")
    isrSystematic.addChannel ("down",    "disTrkSelectionSmearedJets", suffix, dirs['Brian']+"signalCentralValue_80X")
    isrSystematic.printSystematic ()

    print "********************************************************************************"

    fout.close ()

    print "\n\n"

if systematic == "TRIGGER" or systematic == "ALL":

    print "********************************************************************************"
    print "evaluating trigger efficiency systematics (2016BC)"
    print "--------------------------------------------------------------------------------"

    triggerFluctuations = [
        'metLegWeightData',
        'metLegWeightMC',
        'trackLegWeightData',
        'trackLegWeightMC',
    ]

    triggerSystematic = TriggerSystematic (masses, lifetimes)
    triggerSystematic.addExtraSamples (extraSamples)
    triggerSystematic.addChannel ("central", "disTrkSelectionSmearedJets", suffix, dirs['Brian']+"2016/triggerSystematics_BC")
    triggerSystematic.addChannel ("down",    "disTrkSelectionSmearedJets", suffix, dirs['Brian']+"2016/triggerSystematics_BC")
    triggerSystematic.addChannel ("up",      "disTrkSelectionSmearedJets", suffix, dirs['Brian']+"2016/triggerSystematics_BC")
    triggerSystematic.addTriggerFluctuations (triggerFluctuations)
    triggerSystematic.setFoutNames (os.environ["CMSSW_BASE"] + "/src/DisappTrks/SignalSystematics/data/systematic_values__trigger_", "2016BC.txt")
    triggerSystematic.printSystematic ()

    print "********************************************************************************\n\n"

    print "\n\n"

    print "********************************************************************************"
    print "evaluating trigger efficiency systematics (2016DEFG)"
    print "--------------------------------------------------------------------------------"

    triggerFluctuations = [
        'metLegWeightData',
        'metLegWeightMC',
        'trackLegWeightData',
        'trackLegWeightMC',
    ]

    triggerSystematic = TriggerSystematic (masses, lifetimes)
    triggerSystematic.addExtraSamples (extraSamples)
    triggerSystematic.addChannel ("central", "disTrkSelectionSmearedJets", suffix, dirs['Brian']+"2016/triggerSystematics_DEFG")
    triggerSystematic.addChannel ("down",    "disTrkSelectionSmearedJets", suffix, dirs['Brian']+"2016/triggerSystematics_DEFG")
    triggerSystematic.addChannel ("up",      "disTrkSelectionSmearedJets", suffix, dirs['Brian']+"2016/triggerSystematics_DEFG")
    triggerSystematic.addTriggerFluctuations (triggerFluctuations)
    triggerSystematic.setFoutNames (os.environ["CMSSW_BASE"] + "/src/DisappTrks/SignalSystematics/data/systematic_values__trigger_", "2016DEFG.txt")
    triggerSystematic.printSystematic ()

    print "********************************************************************************\n\n"

    print "\n\n"

if systematic == "ECALO" or systematic == "ALL":

    print "********************************************************************************"
    print "evaluating ECalo systematic (2016B & 2016C)"
    print "--------------------------------------------------------------------------------"

    ecaloSystematic_2016BC = ECaloSystematic ()
    ecaloSystematic_2016BC.addChannel  ("Data",  "ZtoMuMuDisTrkNHits4NoECaloCut",  "SingleMu_2016BC",  dirs['Andrew']+"2016/ecaloSystematic")
    ecaloSystematic_2016BC.addChannel  ("MC",    "ZtoMuMuDisTrkNHits4NoECaloCut",  "Background",       dirs['Andrew']+"2016/ecaloSystematic")

    print "********************************************************************************"

    ecaloSystematic_2016BC.printSystematic ()

    print "********************************************************************************"

    print "\n\n"

    print "********************************************************************************"
    print "evaluating ECalo systematic (2016DEFG)"
    print "--------------------------------------------------------------------------------"

    ecaloSystematic_2016DEFG = ECaloSystematic ()
    ecaloSystematic_2016DEFG.addChannel  ("Data",  "ZtoMuMuDisTrkNHits4NoECaloCut",  "SingleMu_2016DEFG",  dirs['Andrew']+"2016/ecaloSystematic")
    ecaloSystematic_2016DEFG.addChannel  ("MC",    "ZtoMuMuDisTrkNHits4NoECaloCut",  "Background",         dirs['Andrew']+"2016/ecaloSystematic")

    print "********************************************************************************"

    ecaloSystematic_2016DEFG.printSystematic ()

    print "********************************************************************************"

    print "\n\n"

if systematic == "HITS" or systematic == "ALL":

    print "********************************************************************************"
    print "evaluating hits systematic (2016B & 2016C)"
    print "--------------------------------------------------------------------------------"

    hitsSystematic = HitsSystematic ()
    hitsSystematic.addChannel  ("Data",  "HitsSystematicsCtrlSelection",  "MET_2016BC",   dirs['Andrew']+"2016/hitsSystematics")
    hitsSystematic.addChannel  ("MC",    "HitsSystematicsCtrlSelection",  "Background",  dirs['Andrew']+"2016/hitsSystematics_hist")
    hitsSystematic.addIntegrateHistogram ("Track Plots/trackNHitsMissingMiddleVsInner")
    print "--------------------------------------------------------------------------------"
    print "before correction to missing middle hits"
    hitsSystematic.printSystematic ()
    hitsSystematic.addIntegrateHistogram ("Track Plots/trackNHitsMissingMiddleCorrectedVsInner")
    print "--------------------------------------------------------------------------------"
    print "after correction to missing middle hits"
    hitsSystematic.printSystematic ()

    print "********************************************************************************"

    print "\n\n"

if systematic == "MISSING_OUTER_HITS" or systematic == "ALL":

    print "********************************************************************************"
    print "evaluating missing outer hits systematic (2016B & 2016C)"
    print "--------------------------------------------------------------------------------"

    missingOuterHitsSystematic = MissingOuterHitsSystematic ()
    missingOuterHitsSystematic.addChannel  ("Data",  "MuonCtrlSelection",  "MET_2016BC",   dirs['Andrew']+"2016/hipAndTOBDrop")
    missingOuterHitsSystematic.addChannel  ("MC",    "MuonCtrlSelection",  "Background",  dirs['Andrew']+"2016/hipAndTOBDrop_new")
    missingOuterHitsSystematic.addIntegrateHistogram ("Track Plots/trackNHitsMissingOuter")
    print "--------------------------------------------------------------------------------"
    print "before correction to missing outer hits"
    missingOuterHitsSystematic.printSystematic ()
    missingOuterHitsSystematic.addIntegrateHistogram ("Track Plots/trackNHitsMissingOuterCorrected")
    print "--------------------------------------------------------------------------------"
    print "after correction to missing outer hits"
    missingOuterHitsSystematic.printSystematic ()

    print "********************************************************************************"

    print "\n\n"
