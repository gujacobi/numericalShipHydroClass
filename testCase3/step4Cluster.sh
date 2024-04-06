#!/bin/sh


module load 2022r2
module load openmpi
module load openfoam

source /apps/arch/2022r2/software/linux-rhel8-skylake_avx512/gcc-8.5.0/openfoam-2106-6iqyrrzl6jyb3mpzcy4cqohas5dqmgwc/etc/bashrc




mkdir 0

cp 0.orig/* 0

setFields

rm -rf processor*

decomposePar
sbatch jobFileinterFoamCluster.sh
