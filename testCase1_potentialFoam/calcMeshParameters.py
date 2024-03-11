#!/usr/bin/env python2
from subprocess import call

#from sympy import *

import math
import numpy as np
import matplotlib.pyplot as plt
import json
from string import Template  

# reading the data from the file
with open('./system/shipSpecs') as f:
    data = f.read()
  


# reconstructing the data as a dictionary
dat = json.loads(data)


# geometricProperties
Lpp=float(dat['Lpp'])
d=float(dat['d'])
b=float(dat['b'])
z0=float(dat['z0'])
trim=float(dat['trim'])
sink=float(dat['sink'])
drift=float(dat['drift'])
v=float(dat['v'])
dom=dat['dom']
lcog=float(dat['lcog'])
xcog=lcog



# Froude number
print('Froude number min/max:')
Fr=v/(math.sqrt(9.81*Lpp))





#Calculate Mesh  parameters

maxRefLevel=int(dat['maxRefLevel'])
minCellSize=Lpp/int(dat['minCellSize'])
cellSize=[]
for i in range(0,maxRefLevel+1):
    cellSize.append(minCellSize*2**(maxRefLevel-i))


#calculate Layer Parameters

yPlusTarget=dat['yPlusTarget']
growthRatio=dat['growthRatio']
Re=Lpp*v/(1.0632e-6)
Cw=np.power(2*np.log10(Re)-0.65,-2.3)
tauw=0.5*np.power(v,2)*1000*Cw
ustar=np.sqrt(tauw/1000)
firstCell=yPlusTarget*0.001002/(1000*ustar)
delta=0.37*Lpp/np.power(Re,1/5)

meshCellSize=cellSize[maxRefLevel]


lCellSize=0
nLayers=0
cumSize=0

while lCellSize<cellSize[maxRefLevel] :
	if nLayers==0:
            lCellSize=firstCell
            nLayers=nLayers+1
            print(nLayers)
            print(lCellSize)
            cumSize=lCellSize
	else:
            lCellSize=lCellSize*growthRatio
            nLayers=nLayers+1
            print(nLayers)
            print(lCellSize)
            cumSize=cumSize+lCellSize

nLayers=nLayers-1
lCellSize=lCellSize/growthRatio


print ('firstCell')
print (firstCell)
print('outerCell')
print (meshCellSize)
print('nLayers')
print (nLayers)
print('delta')
print(delta)

outerCellSize=lCellSize	



# initial number of Cells
nxCells=int(math.ceil((-dom[0]+dom[1])*Lpp/cellSize[0]))
nyCells=int(math.ceil((-dom[2]+dom[3])*Lpp/cellSize[0]))
nzCells=int(math.ceil((-dom[4]+dom[5])*Lpp/cellSize[0]))

#Generate Points and number of Cells for blockMeshDict (with symmetry Plane)
minx=dom[0]*Lpp
maxx=minx+nxCells*cellSize[0]
maxy=(nyCells*cellSize[0])/2
miny=-(nyCells*cellSize[0])/2 
maxz=dom[5]*Lpp
minz=maxz-nzCells*cellSize[0]

#Substitute values in blockMeshDict

#open the file
filein = open( 'system/blockMeshDict.temp')
#read it
src=Template( filein.read() )
#document data
sub={'minx':minx,'maxx':maxx,'miny':miny,'maxy':maxy,'minz':minz,'maxz':maxz,'nx':nxCells,'ny':nyCells,'nz':nzCells}
#do the substitution
result = src.substitute(sub)

blockMeshDict= open("system/blockMeshDict", "w")
blockMeshDict.write(result)
blockMeshDict.close()

#call("blockMesh",  shell=True)





