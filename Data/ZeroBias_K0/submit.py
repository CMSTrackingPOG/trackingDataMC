from CRABClient.UserUtilities import config
config = config()

config.General.requestName = #PUT A REQUEST NAME
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.psetName = 'step1_cfg.py'
config.JobType.allowUndistributedCMSSW = True

config.Data.inputDataset = '/ZeroBias/*/AOD' #TO BE MODIFIED TO ACTUALLY SELECT YOU REQUIRED DATASET (CAN ALSO BE RECO)
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 25
config.Data.publication = False
config.Data.outputDatasetTag = 'Run2023C' #CAN BE MODIFIED ACCORDINGLY
config.Data.lumiMask = 'Cert_Collisions2023_eraC_367095_368823_Golden.json' #EXAMPLE LUMISECTION JSON FILE

config.Site.storageSite = #NAME OF A STORAGE SITE WHERE YOU HAVE WRITING PERMISSIONS
