#!/usr/bin/env python2
from subprocess import call
import sys
#from sympy import *

import math
import numpy as np
import matplotlib.pyplot as plt
import json
from string import Template  


# reading the data from the file


with open('./system/shipSpecs.json') as f:
    data = f.read()
  


# reconstructing the data as a dictionary
dat = json.loads(data)


Lpp=float(dat['Lpp'])
d=float(dat['d'])
b=float(dat['b'])
v=float(dat['v'])
dom=dat['dom']
lcog=float(dat['lcog'])
minCellSize=Lpp/dat['minCellSize']



# calc ship Pos in coordinate system
xcog=lcog # ship roated around Lcog
bb_y=b
y_bow=b/2
y_transom=b/2
x_bow=Lpp
x_transom=0



## create refinement regions within the kelvin angle. 

## kelvin Angle level 4 
level=4

xmax=x_bow+0.2*Lpp
xmin=x_transom-0.3*Lpp
yfmin=-bb_y/2-b/2
yfmax=bb_y/2+b/2
yamax=np.sin(21*np.pi/180)*(xmax-xmin)+bb_y/2+b/2
yamin=-yamax
zmin=-d
zmax=Lpp/1000*25



filein = open( 'constant/triSurface/hexahedron.obj.temp')
#read it
src=Template( filein.read() )           #document data
surfname='kelvinWake1'
sub={'xmax':xmax,'xmin':xmin,'yfmin':yfmin ,'yfmax':yfmax,'yamax':yamax,'yamin':yamin,'zmin':zmin,'zmax':zmax}                                           
#do the substitution
result = src.substitute(sub)
path="constant/triSurface/"
filename=surfname+".obj"
surffile= open(path+filename, "w")
surffile.write(result)
surffile.close()


## kelvin Angle level 3 
level=3
dist=minCellSize*np.power(2,3)*5

xmax=x_bow+0.2*Lpp+dist
xmin=x_transom-0.3*Lpp-dist
yfmin=-bb_y/2-b/2-dist
yfmax=bb_y/2+b/2+dist
yamax=np.sin(21*np.pi/180)*(xmax-xmin)+bb_y/2+b/2+dist
yamin=-yamax
zmin=-d
zmax=Lpp/1000*25


filein = open( 'constant/triSurface/hexahedron.obj.temp')
#read it
src=Template( filein.read() )           #document data
surfname='kelvinWake2'
sub={'xmax':xmax,'xmin':xmin,'yfmin':yfmin ,'yfmax':yfmax,'yamax':yamax,'yamin':yamin,'zmin':zmin,'zmax':zmax}    
#do the substitution
result = src.substitute(sub)
result = src.substitute(sub)
path="constant/triSurface/"
filename=surfname+".obj"
surffile= open(path+filename, "w")
surffile.write(result)
surffile.close()


## kelvin Angle level 2 
level=2
dist=minCellSize*np.power(2,3)*5+minCellSize*np.power(2,4)*5

xmax=x_bow+0.2*Lpp+dist
xmin=x_transom-0.3*Lpp-dist
yfmin=-bb_y/2-b/2-dist
yfmax=bb_y/2+b/2+dist
yamax=np.sin(21*np.pi/180)*(xmax-xmin)+bb_y/2+b/2+dist
yamin=-yamax
zmin=-d
zmax=Lpp/1000*25



filein = open( 'constant/triSurface/hexahedron.obj.temp')
#read it
src=Template( filein.read() )           #document data
surfname='kelvinWake3'
sub={'xmax':xmax,'xmin':xmin,'yfmin':yfmin ,'yfmax':yfmax,'yamax':yamax,'yamin':yamin,'zmin':zmin,'zmax':zmax}    
#do the substitution
result = src.substitute(sub)
result = src.substitute(sub)
path="constant/triSurface/"
filename=surfname+".obj"
surffile= open(path+filename, "w")
surffile.write(result)
surffile.close()



## kelvin Angle level 1 
level=1
dist=minCellSize*np.power(2,3)*5+minCellSize*np.power(2,4)*5+minCellSize*np.power(2,5)*5

xmax=x_bow+0.2*Lpp+dist
xmin=x_transom-0.3*Lpp-dist
yfmin=-bb_y/2-b/2-dist
yfmax=bb_y/2+b/2+dist
yamax=np.sin(21*np.pi/180)*(xmax-xmin)+bb_y/2+b/2+dist
yamin=-yamax
zmin=-d
zmax=Lpp/1000*25



filein = open( 'constant/triSurface/hexahedron.obj.temp')
#read it
src=Template( filein.read() )           #document data
surfname='kelvinWake4'
sub={'xmax':xmax,'xmin':xmin,'yfmin':yfmin ,'yfmax':yfmax,'yamax':yamax,'yamin':yamin,'zmin':zmin,'zmax':zmax}    
#do the substitution
result = src.substitute(sub)
result = src.substitute(sub)
path="constant/triSurface/"
filename=surfname+".obj"
surffile= open(path+filename, "w")
surffile.write(result)
surffile.close()


