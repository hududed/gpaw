# gpaw

## Installation

Steps to install gpaw according to https://wiki.fysik.dtu.dk/gpaw/install.html.

### ASE:  https://wiki.fysik.dtu.dk/ase/install.html#download-and-install
```
pip install --upgrade --user numpy scipy matplotlib
sudo apt-get install python3-tk
pip install Flask
pip install pytest
pip install --upgrade ase
```
In `~/.zshrc` or `~/.bashrc`:
```
export PYTHONPATH=path/to/python:$PYTHONPATH     
# e.g. export PYTHONPATH=/home/hud/.virtualenvs/gpaw/bin/python:$PYTHONPATH
export PATH=/path/to/ase:$PATH 
# e.g.export PATH=/home/hud/.virtualenvs/gpaw/bin/ase:$PATH 
```
