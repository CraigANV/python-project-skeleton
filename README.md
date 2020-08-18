# Python Project Skeleton

[![Build Status](https://travis-ci.org/CraigANV/python-project-skeleton.svg?branch=master)](https://travis-ci.org/CraigANV/python-project-skeleton)

A basic project outline with some helpful tooling:
- Travis CI
- pytest


## Setup

Use python3 by default
```bash
sudo ln -sf /usr/bin/python3 /usr/bin/python
```

### Conda Setup
```bash
conda env create --file environment.yml
conda env create --file environment.yml --force  # if env already exists
conda activate skeleton

conda deactivate
conda env remove -n skeleton
```

## Installing Conda Packages
```bash
conda install -c conda-forge matplotlib
```
