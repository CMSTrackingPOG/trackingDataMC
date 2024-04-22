## trackingDataMC
Data vs MC comparison for CMS tracker
## General instructions

All the instructions to create the CMSSW working area are here: https://twiki.cern.ch/twiki/bin/viewauth/CMS/TkDataMCTool

Once those instructions have been followed you need to run:

```
voms-proxy-init --voms cms --valid 192:00
```
to use your GRID certificate. This creates a file which is stored in the /tmp folder of the machine in which it was run (you will need to copy this file to afs for MC processing, as it is configured to run on htcondor)

#### Data processing

Once you have done everything, you should be in the folder $CMSSW_BASE/src/DQM/TrackingMonitorSource/test, and you should have, among others, the Data/ and MC/ folders. Inside Data you will find the python CMSSW configuration files for ZeroBias, Z into muons, Z into electrons and Kshort and Lambda (using ZeroBias data) processing. You first do:

```
cd Data/#FOLDER OF THE PROCESS YOU NEED
```

then edit submit.py to pick the dataset you want to process, and modify the commented lines accordingly. Here you also need to put the JSON file with all the GOOD lumisections (they can be found here: https://cms-service-dqmdc.web.cern.ch/CAF/certification/, usually we want to use the Golden json, so that it contains only the lumisections certified as GOOD for all CMS subdetectors).

For the dataset you want to process, check what is the Global Tag used in the production, then modify step1_cfg.py and step2_cfg_multirun.py so the that you use the same (just put the GT in the lines which have a comment next to them).

Then do:

```
echo $CMSSW_BASE
```

and modify the line starting with APPDIR= to set APPDIR to the output of the previous command to which the string "/src" needs to be added.

Now you can start processing the data: you first run

```
crab submit -c submit.py
```

which will run the so-called step1 for the DQM processing, and will store the step1 files on the config.Site.storageSite in submit.py. After all of the CRAB jobs have finished successfully, you have to create the step1files.txt files, needed to run the step2 of the DQM processing. This file contains the paths to each of the step1 files. You can create this by doing, for example:

```
find "FOLDER WITH THE STEP1 FILES" > step1files.txt
```

Then you modify step1files.txt so that only the root files are present (usually it also contains the name of the folder itself, if you run the previous command) and so that each line starts with
```
file:
```
Then you run:

```
cmsRun step2_cfg_multirun.py
```

which will create the file with all the histograms for data (which you can then use for the data/MC comparison). Since this usually takes some time, it is best to run:

```
condor_submit step2.sub
```

so that a job is submitted to batch instead.

#### MC processing

MC processing is instead configured to run on htcondor (at least the step1). First:

```
cd MC/#FOLDER OF THE PROCESS YOU NEED
```

Once you have selected the dataset to process, do 

```
dasgoclient --query="file dataset=#NAME OF THE DATASET YOU WANT TO PROCESS" > filelist.txt 
```

then open filelist.txt, keep every file name within "",   : like in the example file : "ex1.root", "ex2.root", "ex3.root",.....

open step1_cfg.py.tmpl, change *process.GlobalTag = GlobalTag(process.GlobalTag, 'GLOBAL_TAG', '')* so that the GT matches the one with which the dataset was produced

open submit.sh.tmpl, change *export X509_USER_PROXY=* so that it contains the path and the name of where the GRID proxy is stored

open createjob.sh , change the commented lines accordingly (the comments in the file explain what to do)

open submitscript.sh , change the commented lines accordingly (the comments in the file explain what to do)

Then you are ready to submit the jobs for step1, first do:

```
./createjob.sh 
```

then:

```
./submitscript.sh 
```

After all the condor jobs are finished, you have to create the step1files.txt files, needed to run the step2 of the DQM processing. This file contains the paths to each of the step1 files. You can create this by doing, for example:

```
find "FOLDER WITH THE STEP1 FILES" > step1files.txt
```

Then you modify step1files.txt so that only the root files are present (usually it also contains the name of the folder itself, for example if you run the previous command) and so that each line starts with

```
file:
```
Then you run:

```
cmsRun step2_cfg.py
```

which will create the file with all the histograms for data (which you can then use for the data/MC comparison).

For MC, this whole sequence needs to be run twice (as also explained in step1_cfg.py.tmpl), once to create the histograms without PU reweighting, to get the PU distribution in the MC dataset you chose, then with the PU reweighting after you have derived the file with the weights. To do this in change *process.standaloneTrackMonitorMC.doPUCorrection = cms.untracked.bool(True)* to *False* before PU reweight step1_cfg.py.tmpl

#### PU Reweighting

Go to DQM/TrackingMonitorSource/test/Scripts/

open pileupreweight.C, put the correct data and MC step2 root files, put the correct folder names and output file name

```
root -l pileupreweight.C
```

You need to set "puScaleFactorFile" in in step1_cfg.py.tmpl to the absolute name of the file you just created.

Then change *process.standaloneTrackMonitorMC.doPUCorrection = cms.untracked.bool(False)* to *True*

For ZtoMuMu or ZtoEE MC datasets, exact same file of *standaloneTrackMonitorMC* will be given as PU reweight file

Re-run step1 and step2, get the MC step2 output after PU reweight

#### Instructions for plotting

Go to DQM/TrackingMonitorSource/test/Scripts. Here you have plotting scripts for each process, *_ZMM.C, *_ZEE.C, *_ZeroBias.C, *_ZeroBias_K0*.C, *_ZeroBias_Lambda*.C

edit filelist_run3_#NAME OF THE PROCESS.txt, Put data step2 file in *:Data* row and MC step2 file in *:MC* row. The *:Data* and *:MC* labels can also be modified to show different text in the plots (for example *:Data*->*:Data 2023C*)

The *Histolist_run3.txt and *Profile_run3.txt can be modified to produce plots for different distributions (for example if some histograms are added to StandaloneTrackMonitor.cc or DQM/TrackingMonitor/src/V0Monitor.cc)

```
root -b -l 
.L datamccomparison_run3_#NAME OF PROCESS.C
datamccomparison_run3("2017")
.q

root -b -l 
.L compareprofile_run3_#NAME OF PROCESS.C
compareprofile_run3("2017")
.q

mkdir plots
mv *.png plots
```

###### Specific instructions for plotting for Kshort and Lambda

In this case you need to run (NAME OF PROCESS is either K0 or Lambda):

```
root -b -l 
.L datamccomparison_run3_ZeroBias_#NAME OF PROCESS_Standalone.C
datamccomparison_run3("2017")
.q

.L datamccomparison_run3_ZeroBias_#NAME OF PROCESS_Monitoring.C
datamccomparison_run3("2017")
.q

root -b -l 
.L compareprofile_run3_ZeroBias_#NAME OF PROCESS_Standalone.C
compareprofile_run3("2017")
.q

root -b -l 
.L compareprofile_run3_ZeroBias_#NAME OF PROCESS_Monitoring.C
compareprofile_run3("2017")
.q

mkdir plots
mv *.png plots
mv *.pdf plots
```

This is because the macros with the "Standalone" suffix produce the comparison plots for the distributions given by StandaloneTrackMonitor.cc, while those with the "Monitoring" suffix are for DQM/TrackingMonitor/src/V0Monitor.cc

(This can and probably should be optimized better)















