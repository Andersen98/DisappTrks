# Table produced with makeANTables.py  
#!/usr/bin/env python  
# ../scripts/bkgdFromData.py -l bkgdOptionsCandTrk.py -w condor_2016_MM_DD_BkgdEstFullSel   
# mergeOutput.py -q -C -s FakeBkgd -l localConfigBkgdEst.py -w condor_2016_MM_DD_BkgdEstFullSel  # To combine ee and mumu fake track samples (optional) 
# makePlots.py       -l localConfigBkgdEst.py -w condor_2016_MM_DD_BkgdEstFullSel -o stacked_histograms.root   
# makePlots.py -P paperPlotsOptions.py      
   
import os   
   
cwd = os.getcwd()   
   
if 'wulsin' in cwd:   
    WellsDir = ''     
    AndrewDir = 'hartCondor/'   
elif 'hart' in cwd:   
    WellsDir = 'WellsCondorNew/'   
    AndrewDir = ''   
else:   
    print 'Error: could not identify user as wulsin or hart.'   
    os.exit(0)   
       
impurities = []  # not yet implemented   
       
bkgd_sources = {   
    'MET' :  { 'inputDir'   : 'candTrkSelection',   
               'datasetsIn'  : ['MET_2015D'],   
               'scale_factor' :       1.0,   
               'scale_factor_error' : 0.0,   
               'channel_map' : {   
    'CandTrkSelectionPlotter' : ['CandTrkSelectionPlotter'],   
    }   
               },   
       
    'ElecBkgd' :  { 'inputDir'   : 'elecCtrlSelection',   
                    'datasetsIn'  : ['MET_2015D'],   
                    'scale_factor' :        0.018394220635,   
                    'scale_factor_error' :  0.00163412427046,   
                    'channel_map' : {   
    'ElecCtrlSelectionPlotter' : ['CandTrkSelectionPlotter'],   
    }   
                    },   
       
    'MuonBkgd' :  { 'inputDir'   : 'muonCtrlSelection',   
                    'datasetsIn'  : ['MET_2015D'],   
                    'scale_factor' :        3.3892560583e-05,   
                    'scale_factor_error' :  7.75639419197e-05,   
                    'channel_map' : {   
    'MuonCtrlSelectionPlotter' : ['CandTrkSelectionPlotter'],   
    }   
                    },   
       
    'TauBkgd' :  { 'inputDir'   : 'tauCtrlSelection',   
                   'datasetsIn'  : ['MET_2015D'],   
                   'scale_factor' :        0.0406852971603,   
                   'scale_factor_error' :  0.00366316359136,   
                   'channel_map' : {   
    'TauCtrlSelectionPlotter' : ['CandTrkSelectionPlotter'],   
    }   
                   },   
       
       
       
    'FakeMuMuBkgd' :  { 'inputDir'   : 'ZtoMuMuCandTrk',   
                    'datasetsIn'  : ['SingleMu_2015D'],   
                    'scale_factor' :        2.63909686671,   
                    'scale_factor_error' :  0.00565947398431,   
                    'channel_map' : {   
    'ZtoMuMuCandTrkPlotter' : ['CandTrkSelectionPlotter'],   
    }   
                    },   
       
       
    }   
