import FWCore.ParameterSet.Config as cms

process = cms.Process("LeptonJetAnalyzer")

process.load("MuJetAnalysis.CutFlowAnalyzer.LeptonJetAnalyzer_cfi")
process.load("TrackingTools.TransientTrack.TransientTrackBuilder_cfi")
process.load('Configuration/StandardSequences/FrontierConditions_GlobalTag_cff')
process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger = cms.Service("MessageLogger", 
    destinations = cms.untracked.vstring("cout"), 
    cout = cms.untracked.PSet(threshold = cms.untracked.string("ERROR"))
)

from Configuration.AlCa.GlobalTag_condDBv2 import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run2_mc', '')

process.source = cms.Source("PoolSource",
    secondaryFileNames = cms.untracked.vstring(),
    fileNames = cms.untracked.vstring(
        'file:/fdata/hepx/store/user/dildick/DarkSUSY_mH_125_mGammaD_0400_13TeV_cT_000_2e2mu_madgraph452_bridge224_LHE_pythia8_SIM/DarkSUSY_mH_125_mGammaD_0400_13TeV_cT_000_2e2mu_madgraph452_bridge224_LHE_pythia8_ANA/bf44a13ded20097547ccf9dac2bcef37/out_pat_1_1_bsE.root',
    )
)

from MuJetAnalysis.AnalysisTools.InputFileHelpers import *
dir = "/fdata/hepx/store/user/dildick/DarkSUSY_mH_125_mGammaD_0400_13TeV_cT_000_2e2mu_madgraph452_bridge224_LHE_pythia8_SIM/DarkSUSY_mH_125_mGammaD_0400_13TeV_cT_000_2e2mu_madgraph452_br\
idge224_LHE_pythia8_ANA/bf44a13ded20097547ccf9dac2bcef37/"
process = useInputDir(process, dir)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(10000)
)

process.TFileService = cms.Service("TFileService",
    fileName = cms.string("out_leptonjet_ana.root")
)

process.p = cms.Path(
    process.LeptonJetAnalyzer
)
