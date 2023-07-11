
source /home/m/mabrouk/anaconda3/etc/profile.d/conda.sh
module purge
module load intel
module load palma/2019a
module load GCC/8.2.0-2.31.1  OpenMPI/3.1.3
module load GROMACS/2019.3
module load Boost/1.70.0
conda activate
python read_wano.py
srun /scratch/tmp/mabrouk/rsmd_injection/rsmd/build/rsmd -i INPUT --gromacs.ntmpi 30 --gromacs.ntomp 1  
python write_wano.py
