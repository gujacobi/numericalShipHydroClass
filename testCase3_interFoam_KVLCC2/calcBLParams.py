#!/usr/bin/env python2
from subprocess import call

#from sympy import *

import math
import numpy as np
import matplotlib.pyplot as plt
import json
from string import Template  
from scipy.optimize import fsolve

# reading the data from the file system/shipSpecs
with open('./system/shipSpecs.json', mode='r') as f:  
    dat = json.load(f)

# geometricProperties
Lpp=float(dat['Lpp'])
v=float(dat['v'])


# Froude number
print('Froude number min/max:')
Fr=v/(math.sqrt(9.81*Lpp))


#Calculate Mesh  parameters

maxRefLevel=int(dat['maxRefLevel'])
minCellSize=Lpp/int(dat['minCellSize'])


#calculate Layer Parameters

yPlusTarget=dat['yPlusTarget']
growthRatio=dat['growthRatio']
Re=Lpp*v/(1.0632e-6)
Cw=np.power(2*np.log10(Re)-0.65,-2.3)
tauw=0.5*np.power(v,2)*1000*Cw
ustar=np.sqrt(tauw/1000)
firstCell=yPlusTarget*0.001002/(1000*ustar)*2 ## multiply by 2 to get cell heigh instead of cell center
delta=0.37*Lpp/np.power(Re,1/5)



func = lambda n: firstCell*np.power(growthRatio,n)-minCellSize/np.power(growthRatio,2)

solution=fsolve(func,3)

nLayers=np.ceil(solution[0])


f= open('./system/blSpecsDict' ,'w') 
f.write('nLayers '+str(int(nLayers))+';\n')
f.write('firstCellHeight '+str(firstCell)+';\n')
f.write('growthRatio '+ str(growthRatio) +';')


    

