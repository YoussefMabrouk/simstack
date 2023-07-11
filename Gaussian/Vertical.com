
%chk=CheckPoint.chk
%nprocshared=20
%mem=22GB
# TPSSTPSS scf(xQC) pop=chelpg Geom=Checkpoint scrf(smd,solvent=water)

name="Vertical"

-1 2
