# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: test_11_b_1 -s HARVESTING:dqmHarvesting --conditions auto:com10 --data --filein file:step1_DQM.root",",", --scenario pp --no_exec --python_filename=test_step2.py
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
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_1.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_10.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_100.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_101.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_102.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_103.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_104.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_105.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_106.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_107.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_108.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_109.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_11.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_110.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_111.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_112.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_113.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_114.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_115.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_116.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_117.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_118.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_119.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_12.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_120.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_121.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_122.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_123.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_124.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_125.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_126.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_127.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_128.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_129.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_13.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_130.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_131.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_132.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_133.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_134.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_135.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_136.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_137.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_138.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_139.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_14.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_140.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_141.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_142.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_143.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_144.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_145.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_146.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_147.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_148.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_149.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_15.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_150.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_151.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_152.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_153.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_154.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_155.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_156.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_157.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_158.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_159.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_16.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_160.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_161.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_162.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_163.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_164.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_165.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_166.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_167.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_168.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_169.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_17.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_170.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_171.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_172.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_173.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_174.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_175.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_176.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_177.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_178.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_179.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_18.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_180.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_181.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_182.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_183.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_184.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_185.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_186.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_187.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_188.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_189.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_19.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_190.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_191.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_192.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_193.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_194.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_195.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_196.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_197.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_198.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_199.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_2.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_20.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_200.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_201.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_202.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_203.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_204.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_205.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_206.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_207.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_208.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_209.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_21.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_210.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_211.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_212.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_213.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_22.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_23.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_24.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_25.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_26.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_27.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_28.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_29.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_3.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_30.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_31.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_32.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_33.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_34.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_35.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_36.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_37.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_38.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_39.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_4.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_40.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_41.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_42.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_43.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_44.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_45.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_46.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_47.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_48.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_49.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_5.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_50.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_51.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_52.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_53.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_54.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_55.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_56.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_57.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_58.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_59.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_6.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_60.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_61.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_62.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_63.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_64.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_65.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_66.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_67.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_68.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_69.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_7.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_70.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_71.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_72.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_73.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_74.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_75.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_76.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_77.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_78.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_79.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_8.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_80.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_81.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_82.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_83.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_84.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_85.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_86.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_87.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_88.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_89.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_9.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_90.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_91.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_92.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_93.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_94.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_95.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_96.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_97.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_98.root",
"file:/afs/cern.ch/work/p/ppalit/public/Data_MC/forgitpush/CMSSW_10_6_8_patch1/src/DQM/TrackingMonitorSource/Jobs/Run2016preVFP_UL/data/NuGun/step1_output/step1_DQM_99.root",

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
process.GlobalTag = GlobalTag(process.GlobalTag, '106X_mcRun2_asymptotic_preVFP_v3', '')

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
