#this is a HF energy calculation program for closed shell molecule (RHF)

from no_of_electron import no_of_e
from distance import find_distance 
#to read input file (geometry)
input_file=open('geom.dat','r')  # this is default mode to read ... w will be to write .. a for append 
file_content=input_file.read()
input_file.close()
#print(file_content)

input_file=open('geom.dat','r')  # this is default mode to read ... w will be to write .. a for append 
file_content=input_file.readlines()
input_file.close()
#print(file_content)

#storing input in list so that we can apply operations over it 
temp_geom=[]
for line in file_content:
    temp_geom.append(line)

#print(temp_geom)
#or
temp_geom=[]
for line in file_content:
    v_line=line.rstrip()   # to remove white space at the end of the line only 
    temp_geom.append(v_line)

#print(temp_geom)


temp_geom=[]
for line in file_content:
    v_line=line.rstrip()   # to strip the lines separately
    if len(v_line)>0:      ############ this way it will take only those lines which have some element ... ll ignore the blank lines 
     f=v_line.split()
     temp_geom.append(f)

print(temp_geom)
print(temp_geom[1][0]) # to print the position of O
NATOM=int(temp_geom[0][0]) # no of atoms 
print ('total no of atoms  '+str(NATOM))
ATOM_SYMBOL=[]
GEOM=[]
for i in range(1,NATOM+1):
    ATOM_SYMBOL.append(temp_geom[i][0])
    GEOM.append(temp_geom[i][1:4])
print('ATOM SYMBOL is')

print(ATOM_SYMBOL)
print('CARTESIAN COORDINATES ARE :')
print(GEOM)



# count the total no oif electron 
NE=0
for i in range(len(ATOM_SYMBOL)):
    k=no_of_e(ATOM_SYMBOL[i])
    NE+=k
print('TOTAL NO OF ELECTRON'+str(NE)
        )



### to calculate the nuclear energy repulsion
E_nuc=0.0
for i in range(NATOM):
    for j in range(0,i):
        z_a=no_of_e(ATOM_SYMBOL[i])
        print('za',z_a)
        z_b=no_of_e(ATOM_SYMBOL[j])
        print('zb',z_b)
        R_ab=find_distance(GEOM[i],GEOM[j])
        
        E_nuc=(z_a*z_b)/R_ab

print('r:',R_ab)         
print('energy:',E_nuc)         


#read one electron integral 








