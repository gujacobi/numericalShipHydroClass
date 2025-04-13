#!/bin/sh
cd "${0%/*}" || exit                                # Run from this directory
. ${WM_PROJECT_DIR:?}/bin/tools/RunFunctions        # Tutorial run functions
#------------------------------------------------------------------------------

foamCleanTutorials
touch case.foam



surfaceFeatureExtract
python3 calcBLParams.py
python3 writeBlockMesh.py
python3 createRefineRegions.py

blockMesh
cp system/controlDict.mesh system/controlDict

decomposePar

mpirun -np 8 snappyHexMesh -dict system/snappyHexMeshDict.1 -parallel 
mpirun -np 8 snappyHexMesh -dict system/snappyHexMeshDict.2 -parallel 
mpirun -np 8 snappyHexMesh -dict system/snappyHexMeshDict.3 -parallel 


reconstructParMesh
reconstructPar -latestTime




