
source /home/m/mabrouk/anaconda3/etc/profile.d/conda.sh
conda activate
python read_wano.py
/Applic.HPC/software/QC/bin/run-g16 Neutral.com Neutral.out
cp CheckPoint.chk Neutral.chk
/Applic.HPC/software/QC/bin/run-g16 Vertical.com Vertical.out 
cp CheckPoint.chk  Vertical.chk
/Applic.HPC/software/QC/bin/run-g16 Opt.com Opt.out
cp CheckPoint.chk  Opt.chk
python write_wano.py
