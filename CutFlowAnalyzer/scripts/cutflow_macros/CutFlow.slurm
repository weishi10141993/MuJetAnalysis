#!/bin/bash
#SBATCH --job-name=CutFlow18
#SBATCH --time=4:00:00 #DATA need 3hr, MSSMD: 4.5hr; BKG: 4.5hr
#SBATCH --ntasks=1
#SBATCH --mem=9000M    #DATA/BKG need 1000M, MSSMD need 9000M
#SBATCH --output=CutFlow.out.%j
#SBATCH --account=122747014489

module load cctools
export PARROT_CVMFS_ALIEN_CACHE=/scratch/group/mitchcomp/CVMFS_cache
cmsSite=/scratch/group/mitchcomp/CMS/LOCAL_TAMU_HPRC
cmsMount=--mount=/cvmfs/cms.cern.ch/SITECONF/local=$cmsSite

parrot_run $cmsMount $SHELL << EOF
shopt -s expand_aliases
source /cvmfs/cms.cern.ch/cmsset_default.sh
cmsenv
echo 'gROOT->ProcessLine(".L CutFlow_2018L2Mu23.C++"); analysis("SignalsList2018MSSMD_2SAmu_NoVtxProbCut_4HLT.txt")' | root -l -b
EOF
