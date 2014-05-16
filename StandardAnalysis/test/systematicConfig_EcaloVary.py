#!/usr/bin/env python

makeRewtdPlot = False
systematic_name = "EcaloRewt"
condor_dir = 'condor_2014_03_18_ZtoMuMuFakeTrkNHits4NoEcalo'  
channel =  'ZtoMuMuFakeTrkNHits4NoEcalo'   

datasets = [
    'AMSB_mGrav32K_0p5ns',
    'AMSB_mGrav32K_1ns',
    'AMSB_mGrav32K_5ns',

    'AMSB_mGrav50K_0p5ns',
 'AMSB_mGrav50K_1ns',
    'AMSB_mGrav50K_5ns',

#    'AMSB_mGrav61K_0p2ns',
    'AMSB_mGrav61K_0p5ns',
    'AMSB_mGrav61K_1ns',
    'AMSB_mGrav61K_5ns',

    'AMSB_mGrav75K_0p5ns',
    'AMSB_mGrav75K_1ns',
    'AMSB_mGrav75K_5ns',

    'AMSB_mGrav100K_0p5ns',
    'AMSB_mGrav100K_1ns',
    'AMSB_mGrav100K_5ns',

    'AMSB_mGrav125K_0p5ns',
    'AMSB_mGrav125K_1ns',
    'AMSB_mGrav125K_5ns',

    'AMSB_mGrav150K_0p5ns',
    'AMSB_mGrav150K_1ns',
    'AMSB_mGrav150K_5ns',

    ]


