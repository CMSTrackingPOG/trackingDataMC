## trackingDataMC
Data vs MC comparison for CMS tracker
## General instructions

```
cmsrel CMSSW_1X_X_X_X

cd CMSSW_1X_X_X_X/src ; cmsenv

git clone this repository

cd DQM/TrackingMonitorSource/

scram b

cd test/
```

create a folder with the corresponding run number to keep track, mv Run_number_folder corresponding_Run_number_folder

cd corresponding_Run_number_folder/Data/ZeroBias , here ZeroBias is for zerobias dataset, change the folder name according to the dataset for own conveninece

```
voms-proxy-init --voms cms --valid 192:00

dasgoclient --query="file dataset=/ZeroBias/Run2018A-PromptReco-v1/AOD run=Run_number" > filelist.txt 
```

open filelist.txt, keep every file name within "",   : like in the example file : "ex1.root", "ex2.root", "ex3.root",.....

open step1_cfg.py.tmpl , change *lumisToProcess = cms.untracked.VLuminosityBlockRange('278509:91-278509:1557')*  according to json file, change *process.GlobalTag = GlobalTag(process.GlobalTag, '106X_dataRun2_v27', '')*

open submit.sh.tmpl, change *export X509_USER_PROXY=*

open batch.sub.tmpl, change *+JobFlavour* as required

open createjob.sh , change *while [ $i -lt 49 ]* to *while [ $i -lt total_number_of_files_in_filelist.txt]* , change *condor_submit "batch_"$i".sub"* to *#condor_submit "batch_"$i".sub"*

```
sh createjob.sh 
```

open step1_1_cfg.py, change *input = cms.untracked.int32(-1)* to *input = cms.untracked.int32(100)* for 100 events

cmsRun step1_1_cfg.py

If it runs without error, open createjob.sh, change *#condor_submit "batch_"$i".sub"* to *condor_submit "batch_"$i".sub"*

```
sh createjob.sh
```

once you get all output, check some runlogs. 

```
ls $PWD/step1_output/*.root

copy the output of ls
```

open step2_cfg.py, put the output of ls in *fileNames* as "file:/dir/ex1.root",..., change *process.GlobalTag*

cmsRun step2_cfg.py

For multirun, give the run and lumi in step1_cfg.py and open the multirun block in step2_cfg_multirun.py script (**currently, it is giving bug!!**)

cd ../../MC/MinBias , change the folder name according to the dataset for own conveninece

Similar steps as data, only change *process.standaloneTrackMonitorMC.doPUCorrection = cms.untracked.bool(True)* to *False* before PU reweight

After step2, do not forget to keep a copy of step2_output_rootfile in a different name like step2_output_nopu_rootfile, it can be needed later 

Go to DQM/TrackingMonitorSource/Scripts/

open pileupreweight.C, put the correct data and MC step2 root files, put the correct folder names and output file name

```
root -l pileupreweight.C
```

copy the output of PU reweight to DQM/TrackingMonitorSource/test/Run_number_folder/MC/MinBias/

Write the pu reweight output file name in *process.standaloneTrackMonitorMC.puScaleFactorFileprocess.standaloneTrackMonitorMC.puScaleFactorFile* , change *process.standaloneTrackMonitorMC.doPUCorrection = cms.untracked.bool(False)* to *True*

For ZtoMuMu or ZtoEE MC datasets, exact same file of *standaloneTrackMonitorMC* will be given as PU reweight file

Re-run step1 and step2, get the MC step2 output after PU reweight

####Instructions for plotting

Go to DQM/TrackingMonitorSource/Scripts

edit filelist_run3.txt, Put data step2 file in *:Data* row and MC step2 file in *:MC* row

edit run numbers/ folder in two root macros accordingly

```
root -b -l 
.L datamccomparison_run3.C
datamccomparison_run3(""2017)
.q

root -b -l 
.L compareprofile_run3.C
compareprofile_run3(""2017)
.q

mkdir plots
mv *.png plots
```















