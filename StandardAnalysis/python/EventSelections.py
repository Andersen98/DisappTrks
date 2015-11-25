import FWCore.ParameterSet.Config as cms
import copy

from DisappTrks.StandardAnalysis.Cuts import * # Put all the individual cuts in this file 


##########################################################################
##### Preselection #####
##########################################################################

basicSelection = cms.PSet(
    name = cms.string("BasicSelection"),
    triggers = triggersMet, 
    cuts = cms.VPSet (
        cutGoodPV,
        cutMet,
        cutJetPt,
        cutJetChgHad,
        cutJetChgEm,
        cutJetNeuHad, 
        cutJetNeuEm,
    )
)

##########################################################################

metMinimalSkim = cms.PSet(
    name = cms.string("metMinimalSkim"),
    triggers = triggersMet, 
    cuts = cms.VPSet (
        cutGoodPV,
        cutMet,
    )
)

##########################################################################

isoTrkSelection = copy.deepcopy(basicSelection) 
isoTrkSelection.name = cms.string("IsoTrkSelection") 
isoTrkCuts = [ 
        cutTrkPt, 
        cutTrkEta,
        cutTrkEcalGapVeto,
        cutTrkEtaMuonIneff1, 
        cutTrkEtaMuonIneff2, 
        cutTrkNValidHits,
        cutTrkNMissIn,
        cutTrkNMissMid, 
        cutTrkIso, 
]
addCuts(isoTrkSelection.cuts, isoTrkCuts)

##########################################################################

nonIsoTrkSelection = copy.deepcopy(isoTrkSelection) 
nonIsoTrkSelection.name = cms.string("NonIsoTrkSelection") 
removeCuts(nonIsoTrkSelection.cuts, [cutTrkIso])

##########################################################################

candTrkSelection = copy.deepcopy(isoTrkSelection) 
candTrkSelection.name = cms.string("CandTrkSelection") 
cutsToAdd = [ 
    cutTrkElecVeto, 
    cutTrkMuonVeto, 
    cutTrkTauVeto, 
]
addCuts(candTrkSelection.cuts, cutsToAdd)
candTrkCuts = isoTrkCuts + cutsToAdd 

##########################################################################

disTrkSelection = copy.deepcopy(candTrkSelection) 
disTrkSelection.name = cms.string("DisTrkSelection") 
cutsToAdd = [ 
    cutTrkEcalo, 
    cutTrkNMissOut, 
]
addCuts(disTrkSelection.cuts, cutsToAdd)
disTrkCuts = candTrkCuts + cutsToAdd 

##########################################################################

# Use this selection for the muon background estimate.   
disTrkSelectionMatchGenMuon = copy.deepcopy(disTrkSelection) 
disTrkSelectionMatchGenMuon.name = cms.string("DisTrkSelectionMatchGenMuon") 
cutsToAdd = [ 
    cutTrkMatchGenMuon, 
]  
addCuts(disTrkSelectionMatchGenMuon.cuts, cutsToAdd) 

##########################################################################

elecCtrlSelection = copy.deepcopy(candTrkSelection) 
elecCtrlSelection.name = cms.string("ElecCtrlSelection") 
cutsToRemove = [ 
    cutTrkElecVeto, 
    cutTrkTauVeto, 
]
removeCuts(elecCtrlSelection.cuts, cutsToRemove)

##########################################################################

muonCtrlSelection = copy.deepcopy(candTrkSelection) 
muonCtrlSelection.name = cms.string("MuonCtrlSelection") 
cutsToRemove = [ 
    cutTrkMuonVeto, 
    cutTrkTauVeto,  
]
removeCuts(muonCtrlSelection.cuts, cutsToRemove)
cutsToAdd = [ 
    cutTrkMatchGenMuon, 
]  
#addCuts(muonCtrlSelection.cuts, cutsToAdd)

##########################################################################

tauCtrlSelection = copy.deepcopy(candTrkSelection) 
tauCtrlSelection.name = cms.string("TauCtrlSelection") 
cutsToRemove = [ 
    cutTrkTauVeto, 
]
removeCuts(tauCtrlSelection.cuts, cutsToRemove)

##########################################################################

caloSdbandSelection = copy.deepcopy(disTrkSelection) 
caloSdbandSelection.name = cms.string("CaloSdbandSelection") 
cutsToRemove = [ 
    cutTrkEcalo, 
]
removeCuts(caloSdbandSelection.cuts, cutsToRemove)
cutsToAdd = [ 
    cutTrkEcaloInv, 
]
addCuts(caloSdbandSelection.cuts, cutsToAdd)

##########################################################################

nMissOutSdbandSelection = copy.deepcopy(disTrkSelection) 
nMissOutSdbandSelection.name = cms.string("NMissOutSdbandSelection") 
cutsToRemove = [ 
    cutTrkNMissOut, 
]
removeCuts(nMissOutSdbandSelection.cuts, cutsToRemove)
cutsToAdd = [ 
    cutTrkNMissOutInv, 
]
addCuts(nMissOutSdbandSelection.cuts, cutsToAdd)

##########################################################################
