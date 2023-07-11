
%chk=CheckPoint.chk
%nprocshared=20
%mem=22GB
# TPSSTPSS opt freq scf(xQC) pop=chelpg scrf(smd,solvent=water) 

name="Neutral"

0 1
