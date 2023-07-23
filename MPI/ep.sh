{
	sbatch <<- EOF
	#!/bin/bash
	#
	#SBATCH --job-name=test_emb
	#SBATCH --output=res_emb.txt
	#SBATCH --partition=batch
	#SBATCH --ntasks=4
	#SBATCH --time=10:00
	#SBATCH --mem-per-cpu=100

	srun printenv SLURM_PROCID
	EOF
}