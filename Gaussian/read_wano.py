import numpy as np
import sys, os, yaml, csv

if __name__ == '__main__':
    
    with open('rendered_wano.yml') as file:
        WanoFile = yaml.full_load(file)
    
    #WanoFile = {'Parameters': [{'Charge': -1.0, 'Spin': 1.0, 'System': 'Gas-Phase'}]}
    #print(WanoFile)
    
    #print(WanoFile)
    #for i in range(len(WanoFile["Parameters"])):
    #    print(WanoFile["Parameters"][i])
    #    for Parameter in WanoFile["Parameters"][i]:
    #        print(Parameter)
   
    InputFile = open('Neutral.com').readlines()
    SpinChargeIndex = 8
    FunctionalsIndex = 4
    print(len(InputFile))
    InputFile[SpinChargeIndex] = "{} {} \n".format(int(WanoFile["Parameters"][0]["Charge"]), int(WanoFile["Parameters"][0]["Spin"]))
    if WanoFile["Parameters"][0]["System"] == "PCM-Water":
        InputFile[FunctionalsIndex] = "# TPSSTPSS opt freq scf(xQC) pop=chelpg scrf(smd,solvent=water) \n"
    else :
        InputFile[FunctionalsIndex] = "# TPSSTPSS opt freq scf(xQC) pop=chelpg \n"    
   
    with open("Neutral.com", "w") as Line:
        for LinePrime in InputFile:
            Line.write(LinePrime)
            
