#!/bin/bash
#SBATCH --job-name=indra
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --partition=gpu-20
#SBATCH --gres=gpu:A100
#SBATCH --error=train_indra/train.err
#SBATCH --mail-type=END

host=`hostname`
echo "Nodo de cálculo asignado: $host"
python3 train_indra/train.py