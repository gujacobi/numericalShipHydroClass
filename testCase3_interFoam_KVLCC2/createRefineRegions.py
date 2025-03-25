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

ang = float(sys.argv[1])

with open('./system/shipSpecs.json') as f:
    data = f.read()
  


# reconstructing the data as a dictionary
dat = json.loads(data)


Lpp=float(dat['Lpp'])
d=float(dat['d'])
b=float(dat['b'])
drift=ang
v=float(dat['v'])
dom=dat['dom']
lcog=float(dat['lcog'])



# calc ship Pos in coordinate system
xcog=lcog # ship roated around Lcog
bb_y=np.sin(drift*np.pi/180)*Lpp
y_bow=np.sin(drift*np.pi/180)*(Lpp-xcog)
y_transom=np.sin(drift*np.pi/180)*(-xcog)
x_bow=np.cos(drift*np.pi/180)*(Lpp-xcog)+xcog
x_transom=np.cos(drift*np.pi/180)*(-xcog)+xcog





## fine kelvin angle 


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


## medium kelvin angle

xmax=x_bow+0.25*Lpp
xmin=x_transom-0.75*Lpp
yfmin=-bb_y/2-b/2*1.2
yfmax=bb_y/2+b/2*1.2
yamax=np.sin(21*np.pi/180)*(xmax-xmin)+bb_y/2+b/2*1.2
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


## coarse kelvin angle

xmax=x_bow+0.25*Lpp
xmin=x_transom-1*Lpp
yfmin=-bb_y/2-b/2
yfmax=bb_y/2+b/2
yamax=np.sin(21*np.pi/180)*(xmax-xmin)+bb_y/2+b/2
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


##very coarse kelvin angle

xmax=x_bow+0.25*Lpp
xmin=x_transom-1.25*Lpp
yfmin=-bb_y/2-b/2
yfmax=bb_y/2+b/2
yamax=np.sin(21*np.pi/180)*(xmax-xmin)+bb_y/2+b/2
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


## fine wake

xmax=x_bow
xmin=x_transom-0.3*Lpp
yfmin=y_bow-b/2*1.5
yfmax=y_bow+b/2*1.5
if drift>=0:
    yamax=y_bow+b/2*1.5
    yamin=np.sin(drift*np.pi/180)*(-xcog-0.5*Lpp)-b/2*1.5
else:
    yamax=np.sin(drift*np.pi/180)*(-xcog-0.5*Lpp)+b/2*1.5
    yamin=y_bow-b/2*1.5

zmin=-d-b/2*0.5
zmax=Lpp/1000*25

filein = open( 'constant/triSurface/hexahedron.obj.temp')
#read it
src=Template( filein.read() )           #document data
surfname='viscousWake1'
sub={'xmax':xmax,'xmin':xmin,'yfmin':yfmin ,'yfmax':yfmax,'yamax':yamax,'yamin':yamin,'zmin':zmin,'zmax':zmax}                                          
#do the substitution
result = src.substitute(sub)
result = src.substitute(sub)
path="constant/triSurface/"
filename=surfname+".obj"
surffile= open(path+filename, "w")
surffile.write(result)
surffile.close()


## coarse wake

xmax=x_bow
xmin=x_transom-Lpp*0.75
yfmin=y_bow-b/2*1.5
yfmax=y_bow+b/2*1.5
if drift>=0:
    yamax=y_bow+b/2*1.6
    yamin=np.sin(drift*np.pi/180)*(-xcog-Lpp)-b/2*1.6
else:
    yamax=-np.sin(drift*np.pi/180)*(-xcog-Lpp)+b/2*165
    yamin=y_bow-b/2*1.6

zmin=-d-b/2*0.6
zmax=Lpp/1000*30


filein = open( 'constant/triSurface/hexahedron.obj.temp')
#read it
src=Template( filein.read() )           #document data
surfname='viscousWake2'
sub={'xmax':xmax,'xmin':xmin,'yfmin':yfmin ,'yfmax':yfmax,'yamax':yamax,'yamin':yamin,'zmin':zmin,'zmax':zmax}                                                 
#do the substitution
result = src.substitute(sub)
result = src.substitute(sub)
path="constant/triSurface/"
filename=surfname+".obj"
surffile= open(path+filename, "w")
surffile.write(result)
surffile.close()
