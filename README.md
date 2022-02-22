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
# e.g. export PYTHONPATH=/home/username/.virtualenvs/gpaw/bin/python:$PYTHONPATH
export PATH=/path/to/ase:$PATH 
# e.g.export PATH=/home/username/.virtualenvs/gpaw/bin/ase:$PATH 
```

### LibXC: http://www.tddft.org/programs/libxc/

Get CMAKE
```
wget https://github.com/Kitware/CMake/releases/download/v3.22.2/cmake-3.22.2.tar.gz
tar xzvf cmake-3.22.2.tar.gz
cd cmake-3.22.2
./bootstrap
make
make install
```
Get LibXC
```
wget http://www.tddft.org/programs/libxc/down.php?file=5.2.2/libxc-5.2.2.tar.gz
tar xzvf libxc-5.2.2.tar.gz
cd libxc-5.2.2
./configure --prefix=PATH/TO/LIBXC
make
make check
make install
```
### BLAS, LAPACK: https://askubuntu.com/questions/1270161/how-to-build-and-link-blas-and-lapack-libraries-by-hand-for-use-on-cluster
gfortran
```
sudo apt-get install gfortran
```

BLAS
```
wget http://www.netlib.org/blas/blas-3.10.0.tgz
tar -xvf blas-3.10.0.tgz
cd BLAS-3.10.0/ 
make
mv blas_LINUX.a libblas.a
mv *.a path/to/lib  # move the blas lib to the library you will be including at compile
# e.g. mv *.a /usr/local/lib
```
LAPACK
```
wget https://github.com/Reference-LAPACK/lapack/archive/refs/tags/v3.10.0.tar.gz
tar -xvf lapack-3.10.0.tar.gz
cd lapack-3.10.0/
cp make.inc.example make.inc  # use example make as make
make
cp *.a path/to/lib
# e.g. mv *.a /usr/local/lib
```
### MPI:
```
sudo apt update
sudo apt install libopenmpi-dev
```
### ScaLapack
```
wget https://github.com/Reference-ScaLAPACK/scalapack/archive/refs/tags/v2.2.0.tar.gz
tar zxvf scalapack-2.2.0.tgz
cd scalapack-2.2.9
cp SLmake.inc.example SLmake.inc
vi SLmake.inc
  BLASLIB       = /usr/local/lib/libblas.a
  LAPACKLIB     = /usr/local/lib/liblapack.a
make lib
sudo ln -s /home/username/scalapack-2.2.0/libscalapack.a /usr/local/lib/libscalapack.a
```
### fftw
```
wget http://www.fftw.org/fftw-3.3.10.tar.gz
tar zxvf fftw-3.3.10.tar.gz
cd ~/fftw-3.3.10
./configure --prefix=/home/username/fftw3
make
make install
```
TO-DO: BLACS
ideas: http://aragorn.pb.bialystok.pl/~mars/tutorial/scalapack/ https://www.netlib.org/blacs/
