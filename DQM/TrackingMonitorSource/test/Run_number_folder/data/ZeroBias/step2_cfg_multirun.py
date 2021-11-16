# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: test_11_b_1 -s HARVESTING:dqmHarvesting --conditions auto:com10 --data --filein file:step1_DQM.root",",",",",",",", --scenario pp --no_exec --python_filename=test_step2.py
import FWCore.ParameterSet.Config as cms

process = cms.Process('HARVESTING')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff')
process.load('Configuration.StandardSequences.EDMtoMEAtRunEnd_cff')
process.load('Configuration.StandardSequences.Harvesting_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

# Input source
process.source = cms.Source("PoolSource",
    secondaryFileNames = cms.untracked.vstring(),
    fileNames = cms.untracked.vstring([
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_11_0_0_pre10/src/DQM/TrackingMonitorSource/test/Jobs/Run2016preVFP/data/ZeroBias/step1_output/step1_DQM_1.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_11_0_0_pre10/src/DQM/TrackingMonitorSource/test/Jobs/Run2016preVFP/data/ZeroBias/step1_output/step1_DQM_10.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_11_0_0_pre10/src/DQM/TrackingMonitorSource/test/Jobs/Run2016preVFP/data/ZeroBias/step1_output/step1_DQM_11.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_11_0_0_pre10/src/DQM/TrackingMonitorSource/test/Jobs/Run2016preVFP/data/ZeroBias/step1_output/step1_DQM_12.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_11_0_0_pre10/src/DQM/TrackingMonitorSource/test/Jobs/Run2016preVFP/data/ZeroBias/step1_output/step1_DQM_13.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_11_0_0_pre10/src/DQM/TrackingMonitorSource/test/Jobs/Run2016preVFP/data/ZeroBias/step1_output/step1_DQM_14.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_11_0_0_pre10/src/DQM/TrackingMonitorSource/test/Jobs/Run2016preVFP/data/ZeroBias/step1_output/step1_DQM_15.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_11_0_0_pre10/src/DQM/TrackingMonitorSource/test/Jobs/Run2016preVFP/data/ZeroBias/step1_output/step1_DQM_16.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_11_0_0_pre10/src/DQM/TrackingMonitorSource/test/Jobs/Run2016preVFP/data/ZeroBias/step1_output/step1_DQM_17.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_11_0_0_pre10/src/DQM/TrackingMonitorSource/test/Jobs/Run2016preVFP/data/ZeroBias/step1_output/step1_DQM_18.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_11_0_0_pre10/src/DQM/TrackingMonitorSource/test/Jobs/Run2016preVFP/data/ZeroBias/step1_output/step1_DQM_19.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_11_0_0_pre10/src/DQM/TrackingMonitorSource/test/Jobs/Run2016preVFP/data/ZeroBias/step1_output/step1_DQM_2.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_11_0_0_pre10/src/DQM/TrackingMonitorSource/test/Jobs/Run2016preVFP/data/ZeroBias/step1_output/step1_DQM_20.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_11_0_0_pre10/src/DQM/TrackingMonitorSource/test/Jobs/Run2016preVFP/data/ZeroBias/step1_output/step1_DQM_21.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_11_0_0_pre10/src/DQM/TrackingMonitorSource/test/Jobs/Run2016preVFP/data/ZeroBias/step1_output/step1_DQM_22.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_11_0_0_pre10/src/DQM/TrackingMonitorSource/test/Jobs/Run2016preVFP/data/ZeroBias/step1_output/step1_DQM_23.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_11_0_0_pre10/src/DQM/TrackingMonitorSource/test/Jobs/Run2016preVFP/data/ZeroBias/step1_output/step1_DQM_24.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_11_0_0_pre10/src/DQM/TrackingMonitorSource/test/Jobs/Run2016preVFP/data/ZeroBias/step1_output/step1_DQM_25.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_11_0_0_pre10/src/DQM/TrackingMonitorSource/test/Jobs/Run2016preVFP/data/ZeroBias/step1_output/step1_DQM_26.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_11_0_0_pre10/src/DQM/TrackingMonitorSource/test/Jobs/Run2016preVFP/data/ZeroBias/step1_output/step1_DQM_27.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_11_0_0_pre10/src/DQM/TrackingMonitorSource/test/Jobs/Run2016preVFP/data/ZeroBias/step1_output/step1_DQM_28.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_11_0_0_pre10/src/DQM/TrackingMonitorSource/test/Jobs/Run2016preVFP/data/ZeroBias/step1_output/step1_DQM_29.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_11_0_0_pre10/src/DQM/TrackingMonitorSource/test/Jobs/Run2016preVFP/data/ZeroBias/step1_output/step1_DQM_3.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_11_0_0_pre10/src/DQM/TrackingMonitorSource/test/Jobs/Run2016preVFP/data/ZeroBias/step1_output/step1_DQM_30.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_11_0_0_pre10/src/DQM/TrackingMonitorSource/test/Jobs/Run2016preVFP/data/ZeroBias/step1_output/step1_DQM_31.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_11_0_0_pre10/src/DQM/TrackingMonitorSource/test/Jobs/Run2016preVFP/data/ZeroBias/step1_output/step1_DQM_32.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_11_0_0_pre10/src/DQM/TrackingMonitorSource/test/Jobs/Run2016preVFP/data/ZeroBias/step1_output/step1_DQM_33.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_11_0_0_pre10/src/DQM/TrackingMonitorSource/test/Jobs/Run2016preVFP/data/ZeroBias/step1_output/step1_DQM_34.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_11_0_0_pre10/src/DQM/TrackingMonitorSource/test/Jobs/Run2016preVFP/data/ZeroBias/step1_output/step1_DQM_35.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_11_0_0_pre10/src/DQM/TrackingMonitorSource/test/Jobs/Run2016preVFP/data/ZeroBias/step1_output/step1_DQM_36.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_11_0_0_pre10/src/DQM/TrackingMonitorSource/test/Jobs/Run2016preVFP/data/ZeroBias/step1_output/step1_DQM_37.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_11_0_0_pre10/src/DQM/TrackingMonitorSource/test/Jobs/Run2016preVFP/data/ZeroBias/step1_output/step1_DQM_38.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_11_0_0_pre10/src/DQM/TrackingMonitorSource/test/Jobs/Run2016preVFP/data/ZeroBias/step1_output/step1_DQM_39.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_11_0_0_pre10/src/DQM/TrackingMonitorSource/test/Jobs/Run2016preVFP/data/ZeroBias/step1_output/step1_DQM_4.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_11_0_0_pre10/src/DQM/TrackingMonitorSource/test/Jobs/Run2016preVFP/data/ZeroBias/step1_output/step1_DQM_40.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_11_0_0_pre10/src/DQM/TrackingMonitorSource/test/Jobs/Run2016preVFP/data/ZeroBias/step1_output/step1_DQM_41.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_11_0_0_pre10/src/DQM/TrackingMonitorSource/test/Jobs/Run2016preVFP/data/ZeroBias/step1_output/step1_DQM_42.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_11_0_0_pre10/src/DQM/TrackingMonitorSource/test/Jobs/Run2016preVFP/data/ZeroBias/step1_output/step1_DQM_43.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_11_0_0_pre10/src/DQM/TrackingMonitorSource/test/Jobs/Run2016preVFP/data/ZeroBias/step1_output/step1_DQM_44.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_11_0_0_pre10/src/DQM/TrackingMonitorSource/test/Jobs/Run2016preVFP/data/ZeroBias/step1_output/step1_DQM_45.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_11_0_0_pre10/src/DQM/TrackingMonitorSource/test/Jobs/Run2016preVFP/data/ZeroBias/step1_output/step1_DQM_46.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_11_0_0_pre10/src/DQM/TrackingMonitorSource/test/Jobs/Run2016preVFP/data/ZeroBias/step1_output/step1_DQM_47.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_11_0_0_pre10/src/DQM/TrackingMonitorSource/test/Jobs/Run2016preVFP/data/ZeroBias/step1_output/step1_DQM_48.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_11_0_0_pre10/src/DQM/TrackingMonitorSource/test/Jobs/Run2016preVFP/data/ZeroBias/step1_output/step1_DQM_49.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_11_0_0_pre10/src/DQM/TrackingMonitorSource/test/Jobs/Run2016preVFP/data/ZeroBias/step1_output/step1_DQM_5.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_11_0_0_pre10/src/DQM/TrackingMonitorSource/test/Jobs/Run2016preVFP/data/ZeroBias/step1_output/step1_DQM_50.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_11_0_0_pre10/src/DQM/TrackingMonitorSource/test/Jobs/Run2016preVFP/data/ZeroBias/step1_output/step1_DQM_51.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_11_0_0_pre10/src/DQM/TrackingMonitorSource/test/Jobs/Run2016preVFP/data/ZeroBias/step1_output/step1_DQM_52.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_11_0_0_pre10/src/DQM/TrackingMonitorSource/test/Jobs/Run2016preVFP/data/ZeroBias/step1_output/step1_DQM_53.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_11_0_0_pre10/src/DQM/TrackingMonitorSource/test/Jobs/Run2016preVFP/data/ZeroBias/step1_output/step1_DQM_54.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_11_0_0_pre10/src/DQM/TrackingMonitorSource/test/Jobs/Run2016preVFP/data/ZeroBias/step1_output/step1_DQM_55.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_11_0_0_pre10/src/DQM/TrackingMonitorSource/test/Jobs/Run2016preVFP/data/ZeroBias/step1_output/step1_DQM_56.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_11_0_0_pre10/src/DQM/TrackingMonitorSource/test/Jobs/Run2016preVFP/data/ZeroBias/step1_output/step1_DQM_57.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_11_0_0_pre10/src/DQM/TrackingMonitorSource/test/Jobs/Run2016preVFP/data/ZeroBias/step1_output/step1_DQM_58.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_11_0_0_pre10/src/DQM/TrackingMonitorSource/test/Jobs/Run2016preVFP/data/ZeroBias/step1_output/step1_DQM_59.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_11_0_0_pre10/src/DQM/TrackingMonitorSource/test/Jobs/Run2016preVFP/data/ZeroBias/step1_output/step1_DQM_6.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_11_0_0_pre10/src/DQM/TrackingMonitorSource/test/Jobs/Run2016preVFP/data/ZeroBias/step1_output/step1_DQM_60.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_11_0_0_pre10/src/DQM/TrackingMonitorSource/test/Jobs/Run2016preVFP/data/ZeroBias/step1_output/step1_DQM_61.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_11_0_0_pre10/src/DQM/TrackingMonitorSource/test/Jobs/Run2016preVFP/data/ZeroBias/step1_output/step1_DQM_62.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_11_0_0_pre10/src/DQM/TrackingMonitorSource/test/Jobs/Run2016preVFP/data/ZeroBias/step1_output/step1_DQM_63.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_11_0_0_pre10/src/DQM/TrackingMonitorSource/test/Jobs/Run2016preVFP/data/ZeroBias/step1_output/step1_DQM_64.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_11_0_0_pre10/src/DQM/TrackingMonitorSource/test/Jobs/Run2016preVFP/data/ZeroBias/step1_output/step1_DQM_65.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_11_0_0_pre10/src/DQM/TrackingMonitorSource/test/Jobs/Run2016preVFP/data/ZeroBias/step1_output/step1_DQM_66.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_11_0_0_pre10/src/DQM/TrackingMonitorSource/test/Jobs/Run2016preVFP/data/ZeroBias/step1_output/step1_DQM_67.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_11_0_0_pre10/src/DQM/TrackingMonitorSource/test/Jobs/Run2016preVFP/data/ZeroBias/step1_output/step1_DQM_68.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_11_0_0_pre10/src/DQM/TrackingMonitorSource/test/Jobs/Run2016preVFP/data/ZeroBias/step1_output/step1_DQM_7.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_11_0_0_pre10/src/DQM/TrackingMonitorSource/test/Jobs/Run2016preVFP/data/ZeroBias/step1_output/step1_DQM_8.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_11_0_0_pre10/src/DQM/TrackingMonitorSource/test/Jobs/Run2016preVFP/data/ZeroBias/step1_output/step1_DQM_9.root",
    ]),
    processingMode = cms.untracked.string('RunsAndLumis')
)

process.options = cms.untracked.PSet(
    Rethrow = cms.untracked.vstring('ProductNotFound'),
    fileMode = cms.untracked.string('FULLMERGE')
)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 1.19 $'),
    annotation = cms.untracked.string('test_11_b_1 nevts:1'),
    name = cms.untracked.string('Applications')
)

# Output definition

# Additional output definition

# Other statements
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '80X_dataRun2_2016LegacyRepro_v3', '')

## FOR Multirun harvesting
#process.DQMStore.collateHistograms = cms.untracked.bool(True)
#process.dqmSaver.saveByRun = cms.untracked.int32(-1) 
#process.dqmSaver.saveAtJobEnd = cms.untracked.bool(True) 
#process.dqmSaver.forceRunNumber = cms.untracked.int32(999999)


# Path and EndPath definitions
process.edmtome_step = cms.Path(process.EDMtoME)
process.validationprodHarvesting = cms.Path(process.hltpostvalidation_prod+process.postValidation_gen)
process.validationHarvesting = cms.Path(process.postValidation+process.hltpostvalidation+process.postValidation_gen)
process.dqmHarvestingPOGMC = cms.Path(process.DQMOffline_SecondStep_PrePOGMC)
#process.validationHarvestingFS = cms.Path(process.HarvestingFastSim)
process.validationpreprodHarvesting = cms.Path(process.postValidation_preprod+process.hltpostvalidation_preprod+process.postValidation_gen)
process.validationHarvestingHI = cms.Path(process.postValidationHI)
process.genHarvesting = cms.Path(process.postValidation_gen)
process.dqmHarvestingPOG = cms.Path(process.DQMOffline_SecondStep_PrePOG)
process.alcaHarvesting = cms.Path()
process.dqmsave_step = cms.Path(process.DQMSaver)

# Schedule definition
process.schedule = cms.Schedule(process.edmtome_step,process.dqmsave_step)
