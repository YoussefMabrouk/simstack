
source /home/m/mabrouk/anaconda3/etc/profile.d/conda.sh

module load palma/2019b GCC/8.3.0 OpenMPI/3.1.4
module load GROMACS/2019.6

conda activate
python read_wano.py
python pdbTOgro.py
gmx grompp -f npt.mdp -p topology.top -c initial.gro -o npt.tpr -po mdout_npt.mdp -maxwarn 4
gmx mdrun -ntmpi 30 -ntomp 1 -s npt.tpr -deffnm npt -append -cpi npt.cpt
python write_wano.py
