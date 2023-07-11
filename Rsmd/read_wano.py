import numpy as np
import sys, os, yaml, csv

if __name__ == '__main__':
    
    #WanoFile = {'Parameters': [{'System': 'Rate', 'cycles': 10.0, 'nsteps': 100.0}]}    
    #for i in range(len(WanoFile["Parameters"])):
    #    print(WanoFile["Parameters"][i])
    #    for Parameter in WanoFile["Parameters"][i]:
    #        print(Parameter)    

    with open('rendered_wano.yml') as file:
        WanoFile = yaml.full_load(file)        
    
    for FileName in "INPUT", "cycle.mdp":
        InputFile = open(FileName).readlines()
        for Parameter in WanoFile["Parameters"][0]:
            try : 
                ParamLine = InputFile.index([Line for Line in InputFile if Parameter in Line][0])
                InputFile[ParamLine] = Parameter + "     = " + str(int(WanoFile["Parameters"][0][Parameter])) + " \n"
            except :
                continue            
        with open(FileName, "w") as Line:
            for LinePrime in InputFile:
                Line.write(LinePrime)    
