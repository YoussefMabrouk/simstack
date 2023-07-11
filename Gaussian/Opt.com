
%chk=CheckPoint.chk
%nprocshared=20
%mem=22GB
# TPSSTPSS opt freq scf(xQC) pop=chelpg Geom=Checkpoint scrf(smd,solvent=water)

name="Optimal"

-1 2     

