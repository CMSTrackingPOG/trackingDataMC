#!/bin/bash
#set -o nounset

APPDIR=#PUT THE CMSSW AREA PATH 
JOBDIR=$APPDIR/DQM/TrackingMonitorSource/test/data/ZMM
cd $APPDIR
eval $(scramv1 runtime -sh)
cd $JOBDIR
cmsRun step2_cfg_multirun.py
exit $?