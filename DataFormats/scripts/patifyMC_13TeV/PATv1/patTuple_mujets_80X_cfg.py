## import skeleton process
from PhysicsTools.PatAlgos.patTemplate_cfg import *

# verbose flags for the PF2PAT modules
process.options.allowUnscheduled = cms.untracked.bool(False)

### Add MuJet Dataformats
from MuJetAnalysis.DataFormats.EventContent_version10_cff import *
process = customizePatOutput(process)

process.load("MuJetAnalysis.DataFormats.miniAODtoPAT_cff")

## pick latest HLT process
process.patTriggerEvent.processName = cms.string( "*" )

process.load("MuJetAnalysis.MuJetProducer.MuJetProducer_cff")

process.source = cms.Source("PoolSource",
  fileNames = cms.untracked.vstring(
        'file:/fdata/hepx/store/user/dildick/DarkSUSY_mH_125_mGammaD_0250_cT_000_13TeV_MG452_BR224_LHE_pythia8_GEN_SIM_MINIAOD_V2_v1/crab_DarkSUSY_mH_125_mGammaD_0250_cT_000_13TeV_MG452_BR224_LHE_pythia8_MINIAOD_MINIAOD_V2_v2/161005_194724/0000/out_miniaod_1.root'
  )
)

process.maxEvents.input = 100

process.p = cms.Path(
    process.patifyMC *
    process.MuJetProducers
)