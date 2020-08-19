#!/usr/bin/env sh

wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh -b -p "$HOME/miniconda3"

# Required for debugging in Cloud9, not available via Conda
pip3 install ikp3db

echo 'export PATH="$PATH:$HOME/miniconda3/bin/"' >> "$HOME/.bashrc"
