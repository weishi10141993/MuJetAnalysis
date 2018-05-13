#!/bin/bash


#period=("B" "C" "D" "E" "F")
period=("B")
   
for i in "${period[@]}"
do

cat  >  run_jpsi_$i.slrm <<EOF
#!/bin/bash      
#SBATCH -J AnalysisJpsi_period$i
#SBATCH -n1
#SBATCH --time=08:30:00
#SBATCH --mem-per-cpu=8000mb
#SBATCH -p background
#SBATCH -o $PWD/out_Run2016$i.stdout
#SBATCH -e $PWD/out_Run2016$i.stderr
      
export PROCESS=\$SLURM_ARRAY_TASK_ID
cd /fdata/scratch/castaned/DisplacedMuonJetAnalysis_2016/CMSSW_8_0_20/src 
export VO_CMS_SW_DIR=/cvmfs/cms.cern.ch
source $VO_CMS_SW_DIR/cmsset_default.sh
export SCRAM_ARCH=slc6_amd64_gcc493
eval \`scramv1 runtime -sh\`
cd /fdata/scratch/castaned/DisplacedMuonJetAnalysis_2016/CMSSW_8_0_20/src/MuJetAnalysis/CutFlowAnalyzer/scripts
echo 'gROOT->LoadMacro("jpsi.C"); analysis("MuOnia_Run2016$i.txt"); gSystem->Exit(0);' | root -b -l
      
exit 0

EOF
done

