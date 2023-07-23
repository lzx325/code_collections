{
    set -e
	module purge
	module load openmpi
    source /home/liz0f/anaconda3/etc/profile.d/conda.sh
	conda deactivate
	conda activate diffusers

    sbatch <<- EOF
	#!/bin/bash
	#SBATCH --job-name=test_mpi
	#SBATCH --output=res_mpi.txt
	#SBATCH --error=err_mpi.txt
	#SBATCH --partition=batch
	#SBATCH --nodes=6
	#SBATCH --ntasks=6
	#SBATCH --time=20:00
	#SBATCH --gres=gpu:1
	#SBATCH --cpus-per-task=5
	#SBATCH --mem-per-cpu=10G

	srun --nodes 3 --ntasks=3 \
    python wikipy.py

    wait
	EOF
}