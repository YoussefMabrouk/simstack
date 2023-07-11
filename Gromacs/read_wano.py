import numpy as np
import sys, os, yaml, csv

if __name__ == '__main__':
    
    #WanoFile = {'Parameters': [{'tcoupl': 'nose-hoover', 'nsteps': 0.0, 'ref-t': 0.0, 'xtcout': 0.0}]}
    #print(WanoFile)
    
    #for i in range(len(WanoFile["Parameters"])):
    #    print(WanoFile["Parameters"][i])
    #    for Parameter in WanoFile["Parameters"][i]:
    #        print(Parameter)    
    
    with open('rendered_wano.yml') as file:
        WanoFile = yaml.full_load(file)
   
    InputFile = open('npt.mdp').readlines()
    for Parameter in WanoFile["Parameters"][0]:
        ParamLine = InputFile.index([Line for Line in InputFile if Parameter in Line][0])
        try :
            InputFile[ParamLine] = Parameter + "     = " + str(int(WanoFile["Parameters"][0][Parameter])) + " \n"
        except:
            InputFile[ParamLine] = Parameter + "     = " + str(WanoFile["Parameters"][0][Parameter]) + " \n"

    with open("npt.mdp", "w") as Line:
        for LinePrime in InputFile:
            Line.write(LinePrime)
       
