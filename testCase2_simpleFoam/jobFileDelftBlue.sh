BATCH --job-name="hull16_doubleBody"
#SBATCH --time=10:00:00
#SBATCH --partition=compute
#SBATCH --ntasks=12
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=2G
#SBATCH --account=education-me-courses-mt44025

module load 2022r2
module load openmpi
module load openfoam

source /apps/arch/2022r2/software/linux-rhel8-skylake_avx512/gcc-8.5.0/openfoam-2106-6iqyrrzl6jyb3mpzcy4cqohas5dqmgwc/etc/bashrc

srun --cpu-bind=none simpleFoam -case hull16_doubleBody -parallel >run.log
