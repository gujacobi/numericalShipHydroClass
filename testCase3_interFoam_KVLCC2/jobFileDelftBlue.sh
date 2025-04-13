BATCH --job-name="KVLCC2_coarse"
#SBATCH --time=10:00:00
#SBATCH --partition=compute
#SBATCH --ntasks=4
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=2G
#SBATCH --account=education-me-courses-mt44025

module load 2024r1
module load openmpi
module load openfoam


srun --cpu-bind=none interFoam  -parallel >run.log
