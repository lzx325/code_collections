{
    set -e
    source "$HOME"/anaconda3/etc/profile.d/conda.sh
    conda deactivate
    conda activate test
    python setup.py build_ext --inplace
    python main.py
    exit 0
}
