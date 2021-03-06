#!/usr/bin/env python
import os
import sys
import math
import functools

from ROOT import gROOT, gStyle, TCanvas, TFile, TGraphAsymmErrors, TH1D, TH3D, TMath, TPaveText, TObject

from DisappTrks.StandardAnalysis.plotUtilities import *

setTDRStyle()

gROOT.SetBatch()
gStyle.SetOptStat(0)

class FakeTrackBkgdEstimate:
    _fout = None
    _canvas = None
    _prescale = 1.0
    _luminosityInInvFb = float ("nan")
    _minHits = 7
    _minD0 = 0.02
    _maxD0 = 0.1

    def __init__ (self):
        pass

    def addTFile (self, fout):
        self._fout = fout

    def addTCanvas (self, canvas):
        self._canvas = canvas

    def addPrescaleFactor (self, prescale):
        self._prescale = prescale

    def addLuminosityInInvPb (self, luminosityInInvPb):
        self._luminosityInInvFb = luminosityInInvPb / 1000.0

    def addMinHits (self, minHits):
        self._minHits = minHits

    def addMinD0 (self, minD0):
        self._minD0 = minD0

    def addMaxD0 (self, maxD0):
        self._maxD0 = maxD0

    def addChannel (self, role, name, sample, condorDir):
        channel = {"name" : name, "sample" : sample, "condorDir" : condorDir}
        channel["yield"], channel["yieldError"] = getHistIntegral (sample, condorDir, name + "Plotter", "Track-eventvariable Plots/trackd0WRTPVMag", 0.0, self._maxD0 - 0.001)
        setattr (self, role, channel)
        print "yield for " + name + ": " + str (channel["yield"]) + " +- " + str (channel["yieldError"])

    def printTransferFactor (self):
        if hasattr (self, "Basic3hits"):
            passes, passesError = getHistIntegral (self.Basic3hits["sample"], self.Basic3hits["condorDir"], self.Basic3hits["name"] + "Plotter", "Track-eventvariable Plots/trackd0WRTPVMag", 0.0, 0.02 - 0.001)
            fails, failsError = getHistIntegral (self.Basic3hits["sample"], self.Basic3hits["condorDir"], self.Basic3hits["name"] + "Plotter", "Track-eventvariable Plots/trackd0WRTPVMag", self._minD0, self._maxD0 - 0.001)

            if fails > 0.0:
                transferFactor = passes / fails
                transferFactorError = transferFactor * math.hypot (passesError/passes, failsError/fails)
                print "Transfer factor: " + str (transferFactor) + " +/- " + str (transferFactorError)
                return (transferFactor, transferFactorError, passes, passesError, fails, failsError)
            else:
                print "N(fail d0 cut, 3 hits) = 0, not printing scale factor..."
                return (float ("nan"), float ("nan"), float ("nan"), float ("nan"), float ("nan"), float ("nan"))

        else:
            print "Basic3hits is not defined. Not printing transfer factor..."
            return (float ("nan"), float ("nan"), float ("nan"), float ("nan"), float ("nan"), float ("nan"))

    def printNctrl (self):
        if hasattr (self, "DisTrkInvertD0"):
            n, nError = getHistIntegral (self.DisTrkInvertD0["sample"], self.DisTrkInvertD0["condorDir"], self.DisTrkInvertD0["name"] + "Plotter", "Track-eventvariable Plots/trackd0WRTPVMag", self._minD0, self._maxD0 - 0.001)
            if self._minHits < 7:
                n6, n6Error = getHistIntegral (self.DisTrkInvertD0NHits6["sample"], self.DisTrkInvertD0NHits6["condorDir"], self.DisTrkInvertD0NHits6["name"] + "Plotter", "Track-eventvariable Plots/trackd0WRTPVMag", self._minD0, self._maxD0 - 0.001)
                n += n6
                nError = math.hypot (nError, n6Error)
            if self._minHits < 6:
                n5, n5Error = getHistIntegral (self.DisTrkInvertD0NHits5["sample"], self.DisTrkInvertD0NHits5["condorDir"], self.DisTrkInvertD0NHits5["name"] + "Plotter", "Track-eventvariable Plots/trackd0WRTPVMag", self._minD0, self._maxD0 - 0.001)
                n += n5
                nError = math.hypot (nError, n5Error)
            if self._minHits < 5:
                n4, n4Error = getHistIntegral (self.DisTrkInvertD0NHits4["sample"], self.DisTrkInvertD0NHits4["condorDir"], self.DisTrkInvertD0NHits4["name"] + "Plotter", "Track-eventvariable Plots/trackd0WRTPVMag", self._minD0, self._maxD0 - 0.001)
                n += n4
                nError = math.hypot (nError, n4Error)
            if self._minHits < 4:
                n3, n3Error = getHistIntegral (self.DisTrkInvertD0NHits3["sample"], self.DisTrkInvertD0NHits3["condorDir"], self.DisTrkInvertD0NHits3["name"] + "Plotter", "Track-eventvariable Plots/trackd0WRTPVMag", self._minD0, self._maxD0 - 0.001)
                n += n3
                nError = math.hypot (nError, n3Error)
            if n == 0.0:
                nError = 0.5 * TMath.ChisquareQuantile (0.68, 2 * (n + 1))

            pFake = pFakeError = float ("nan")

            # For ZtoMuMu control regions, need to normalize to BasicSelection
            if hasattr (self, "ZtoLL") and hasattr (self, "Basic"):
                norm = self.Basic["yield"] / self.ZtoLL["yield"]
                normError = norm * math.hypot (self.Basic["yieldError"] / self.Basic["yield"], self.ZtoLL["yieldError"] / self.ZtoLL["yield"])

                pFake = n / self.ZtoLL["yield"]
                pFakeError = math.hypot (n * self.ZtoLL["yieldError"], nError * self.ZtoLL["yield"]) / (self.ZtoLL["yield"] * self.ZtoLL["yield"])

                n = n * norm
                nError = math.hypot (n * normError, nError * norm)
            elif hasattr (self, "Basic"):
                pFake = n / self.Basic["yield"]
                pFakeError = math.hypot (n * self.Basic["yieldError"], nError * self.Basic["yield"]) / (self.Basic["yield"] * self.Basic["yield"])

            n *= self._prescale
            nError *= self._prescale

            if n > 0.0:
                print "N_ctrl: " + str (n) + " +- " + str (nError) + " (" + str (n / self._luminosityInInvFb) + " +- " + str (nError / self._luminosityInInvFb) + " fb)"
            else:
                print "N_ctrl: " + str (n) + " - 0.0 + " + str (nError) + " (" + str (n / self._luminosityInInvFb) + " - 0 + " + str (nError / self._luminosityInInvFb) + " fb)"
            return (n, nError, pFake, pFakeError)
        else:
            print "DisTrkInvertD0 is not defined. Not printing N_ctrl..."
            return (float ("nan"), float ("nan"), float ("nan"), float ("nan"))

    def printNest (self):
        xi, xiError, xiPass, xiPassError, xiFail, xiFailError = self.printTransferFactor ()
        nCtrl, nCtrlError, pFake, pFakeError = self.printNctrl ()

        pFake *= xi
        pFakeError = math.hypot (xi * pFakeError, xiError * pFake)

        N = nCtrl
        alpha = (xiPass / xiFail)
        alphaError = math.hypot (xiFailError * xiPass, xiPassError * xiFail) / (xiFail * xiFail)

        nEst = xi * nCtrl
        nEstError = math.hypot (xiError * nCtrl, nCtrlError * xi)

        if pFake > 0.0:
            print "P_fake: " + str (pFake) + " +- " + str (pFakeError)
        else:
            print "P_fake: " + str (pFake) + " - 0 + " + str (pFakeError)

        print "N: " + str (N)
        if not (alpha == 0):
            print "alpha: " + str (alpha) + " +- " + str (alphaError)
            print "error on alpha: " + str (1.0 + (alphaError / alpha))
        else:
            print "alpha: " + str (alpha) + " - 0 + " + str (alphaError)
            print "error on alpha: nan"

        if nEst > 0.0:
            print "N_est: " + str (nEst) + " +- " + str (nEstError) + " (" + str (nEst / self._luminosityInInvFb) + " +- " + str (nEstError / self._luminosityInInvFb) + " fb)"
        else:
            print "N_est: " + str (nEst) + " + " + str (nEstError) + " - 0.0 (" + str (nEst / self._luminosityInInvFb) + " + " + str (nEstError / self._luminosityInInvFb) + " - 0.0 fb)"

        return (nEst, nEstError)
