#!/usr/bin/env python2
from subprocess import call

#from sympy import *

import math
import numpy as np
import matplotlib.pyplot as plt
import json
from string import Template  

# reading the data from the file system/shipSpecs
with open('./system/shipSpecs.json',mode='r') as f:
    dat = json.load(f)

# geometricProperties
Lpp=float(dat['Lpp'])
dom=dat['dom']



#Calculate Mesh  parameters

maxRefLevel=int(dat['maxRefLevel'])
minCellSize=Lpp/int(dat['minCellSize'])
cellSize=[]
for i in range(0,maxRefLevel+1):
    cellSize.append(minCellSize*2**(maxRefLevel-i))




# initial number of Cells
nxCells=int(math.ceil((-dom[0]+dom[1])*Lpp/cellSize[0]))
nyCells=int(math.ceil((-dom[2]+dom[3])*Lpp/cellSize[0]))
nzCells=int(math.ceil((-dom[4]+dom[5])*Lpp/cellSize[0]))

#Generate Points and number of Cells for blockMeshDict
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





