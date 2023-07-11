
source /home/m/mabrouk/anaconda3/etc/profile.d/conda.sh
ml palma/2020b
ml GCC/10.2.0
ml packmol/20.2.2
conda activate
python read_wano.py
packmol < generate.inp
python write_wano.py
