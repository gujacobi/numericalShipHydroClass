#!/bin/sh
cd "${0%/*}" || exit                                # Run from this directory
. ${WM_PROJECT_DIR:?}/bin/tools/RunFunctions        # Tutorial run functions
#------------------------------------------------------------------------------
mv 4 0
rm -r 1 2 3
cp 0.orig/* 0

setFields
cp system/controlDict.sim system/controlDict

renumberMesh
rm -rf processor*
decomposePar



mpirun -np 8 interFoam -parallel


