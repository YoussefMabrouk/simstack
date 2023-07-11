import numpy as np
import pandas as pd

box_length = 17
mol_pos = 5                  
atom_pos = 9
num_pos = 5
coordinate_pos = 8
round_pos = 3
filename = "Input-File"
structure = open(filename)
data = []
for line in structure:
    data.append(line)  
data = data[5:-1] 
elements = []
for i in range(len(data)):
    if data[i][12] != ' ':
        elements.append(data[i][12])
    else :
        elements.append(data[i][13])
coordinates = []
for i in range(len(data)):
    coordinates.append([float(data[i][32:38]), float(data[i][40:46]), float(data[i][47:54])])
coordinates = np.array([coordinates])[0]
conv = 0.1
coordinates *= conv
str_coordinates = []
for i in range(len(data)):
    str_vec = []
    for j in range(3):
        coordinate = "{:5.3f}".format(coordinates[i, j])
        str_vec.append(coordinate)
    str_coordinates.append(str_vec)
EC = ['O', 'C', 'O', 'C', 'H', 'H', 'O', 'C', 'H', 'H'] 
EC_index = [1, 1, 2, 2, 1, 2, 3, 3, 3, 4]                
EC_counter = 1
PF6 = ['P', 'F', 'F', 'F', 'F', 'F', 'F']
PF6_index = [1, 1, 2, 3, 4, 5, 6]
PF6_counter = 1
Li = ['L']
Li_index = [1]
Li_counter = 1
A = ['A']
A_index = [1]
A_counter = 1
atom_counter = 1
first_data=[]           
for i in range(len(data)):        
    if elements[i:i+len(Li)] == Li :
        for j in range(len(Li)):
            first_data.append(f"{'%d'%Li_counter:>{mol_pos}}" + 'LI'\
                            f"{data[i+j][13]+'i%d'%Li_index[j]:>{atom_pos-(len('LI')-1)}}" + \
                            f"{'%d'%atom_counter:>{num_pos}}" + \
                            f"{str_coordinates[i+j][0]:>{coordinate_pos}}" + \
                            f"{str_coordinates[i+j][1]:>{coordinate_pos}}" + \
                            f"{str_coordinates[i+j][2]:>{coordinate_pos}}")
            atom_counter += 1
        Li_counter += 1      
for i in range(len(data)):        
    if elements[i:i+len(A)] == A :
        for j in range(len(A)):
            first_data.append(f"{'%d'%A_counter:>{mol_pos}}" + 'A'\
                            f"{data[i+j][13]+'%d'%A_index[j]:>{atom_pos-(len('A')-1)}}" + \
                            f"{'%d'%atom_counter:>{num_pos}}" + \
                            f"{str_coordinates[i+j][0]:>{coordinate_pos}}" + \
                            f"{str_coordinates[i+j][1]:>{coordinate_pos}}" + \
                            f"{str_coordinates[i+j][2]:>{coordinate_pos}}")
            atom_counter += 1
        A_counter += 1            
for i in range(len(data)-len(PF6)):        
    if elements[i:i+len(PF6)] == PF6 :
        for j in range(len(PF6)):
            first_data.append(f"{'%d'%PF6_counter:>{mol_pos}}" + 'PF6'\
                            f"{data[i+j][12]+'%d'%PF6_index[j]:>{atom_pos-(len('PF6')-1)}}" + \
                            f"{'%d'%atom_counter:>{num_pos}}" + \
                            f"{str_coordinates[i+j][0]:>{coordinate_pos}}" + \
                            f"{str_coordinates[i+j][1]:>{coordinate_pos}}" + \
                            f"{str_coordinates[i+j][2]:>{coordinate_pos}}")
            atom_counter += 1
        PF6_counter += 1
for i in range(len(data)-len(EC)):            
    if elements[i:i+len(EC)] == EC :
        for j in range(len(EC)):
            first_data.append(f"{'%d'%EC_counter:>{mol_pos}}" + 'EC'\
                            f"{data[i+j][12]+'%d'%EC_index[j]:>{atom_pos-(len('EC')-1)}}" + \
                            f"{'%d'%atom_counter:>{num_pos}}" + \
                            f"{str_coordinates[i+j][0]:>{coordinate_pos}}" + \
                            f"{str_coordinates[i+j][1]:>{coordinate_pos}}" + \
                            f"{str_coordinates[i+j][2]:>{coordinate_pos}}")  
            atom_counter += 1   
        EC_counter += 1          
        
 

 
filename = "start.xyz"                                          
structure = open(filename)
data = []
for line in structure:
    data.append(line)  
data = data[2:]
elements = []
for i in range(len(data)):
    elements.append(data[i][0])
new_data = []
coordinates = []
for i in range(len(data)):
    coordinates.append([float(data[i][2:12]), float(data[i][13:23]), float(data[i][24:34])])
coordinates = np.array([coordinates])[0]
conv = 0.1
coordinates *= conv
str_coordinates = []
for i in range(len(data)):
    str_vec = []
    for j in range(3):
        coordinate = "{:5.3f}".format(coordinates[i, j])
        str_vec.append(coordinate)
    str_coordinates.append(str_vec)
    
    
C = ['C', 'C', 'C']
C_index = [1, 1, 1]
C_counter = 1
S = ['C', 'C', 'C']
S_index = [1, 1, 1]
S_counter = 1
second_data = []
for i in range(len(data)-len(C)):        
    if elements[i:i+len(C)] == C and coordinates[i][2]<0.:       
        second_data.append(f"{'%d'%C_counter:>{mol_pos}}" + 'G'\
                        f"{data[i][0]+'%d'%C_index[0]:>{atom_pos-(len('G')-1)}}" + \
                        f"{'%d'%atom_counter:>{num_pos}}" + \
                        f"{str_coordinates[i][0]:>{coordinate_pos}}" + \
                        f"{str_coordinates[i][1]:>{coordinate_pos}}" + \
                        f"{str_coordinates[i][2]:>{coordinate_pos}}")
        atom_counter += 1
        C_counter += 1         
for i in range(len(data)-len(S)):        
    if elements[i:i+len(S)] == S and coordinates[i][2]>=0.:
        second_data.append(f"{'%d'%S_counter:>{mol_pos}}" + 'S'\
                        f"{data[i][0]+'%d'%S_index[0]:>{atom_pos-(len('S')-1)}}" + \
                        f"{'%d'%atom_counter:>{num_pos}}" + \
                        f"{str_coordinates[i][0]:>{coordinate_pos}}" + \
                        f"{str_coordinates[i][1]:>{coordinate_pos}}" + \
                        f"{str_coordinates[i][2]:>{coordinate_pos}}")
        atom_counter += 1
        S_counter += 1             
        
new_data = first_data + second_data                
newer_data = [] 
newer_data.append('Built with Python') 
newer_data.append(' %d'%len(new_data)) 
for i in range(len(new_data)): 
    newer_data.append(new_data[i])
newer_data.append(' 3.50 3.50 {}'.format(box_length+3.0))
with open('initial.gro', 'w') as f: 
    for item in newer_data: 
        f.write("%s\n" % item)
