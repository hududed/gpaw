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

### LibXC: http://www.tddft.org/programs/libxc/

Get CMAKE
```
wget https://github.com/Kitware/CMake/releases/download/v3.23.0-rc1/cmake-3.23.0-rc1.tar.gz
tar xzvf cmake-3.23.0-rc1.tar.gz
rm cmake-3.23.0-rc1.tar.gz
cd cmake-3.22.2
./bootstrap
make
make install
```
Get LibXC
```
wget http://www.tddft.org/programs/libxc/down.php?file=5.2.2/libxc-5.2.2.tar.gz
tar xzvf libxc-5.2.2.tar.gz
rm ibxc-5.2.2.tar.gz
cd libxc-5.2.2
./configure --prefix=PATH/TO/LIBXC
make
make check
make install
```


