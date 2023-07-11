import numpy as np
import sys, os, yaml, csv

if __name__ == '__main__':
    
    #WanoFile = {'Parameters': [{'EC': 100.0, 'Li+': 10.0, 'PF6-': 10.0}]}
    #print(WanoFile)

    #for i in range(len(WanoFile["Parameters"])):
    #    print(WanoFile["Parameters"][i])
    #    for Parameter in WanoFile["Parameters"][i]:
    #        print(Parameter)    
    
    with open('rendered_wano.yml') as file:
        WanoFile = yaml.full_load(file)
   
    InputFile = open('generate.inp').readlines()
    for Molecule in WanoFile["Parameters"][0]:
        MolLine = InputFile.index([Line for Line in InputFile if Molecule in Line][0])
        InputFile[MolLine+1] = "  number {} \n".format(int(WanoFile["Parameters"][0][Molecule]))
   
    with open("generate.inp", "w") as Line:
        for LinePrime in InputFile:
            Line.write(LinePrime)
