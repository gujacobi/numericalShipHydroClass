#!/bin/sh
cd "${0%/*}" || exit                                # Run from this directory
. ${WM_PROJECT_DIR:?}/bin/tools/RunFunctions        # Tutorial run functions
#------------------------------------------------------------------------------
mv 4 0
rm -r 1 2 3
cp 0.orig/* 0

potentialFoam

decomposePar



mpirun -np 4 simpleFoam -parallel


