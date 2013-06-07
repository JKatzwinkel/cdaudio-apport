#/bin/bash

home=$PWD

sudo apt-get install gcc git libcdio-cdda-dev libcdio-paranoia-dev
if [ ! -d python-audio-tools ]; then
 git clone git://github.com/tuffy/python-audio-tools.git
fi
cd python-audio-tools
python setup.py build
if [ ! -d $home/audiotools ]; then
 cp -r build/lib*/audiotools $home
fi
cd $home

if [ ! -f tcl.tar.gz ]; then
 wget http://prdownloads.sourceforge.net/tcl/tcl8.6.0-src.tar.gz -O tcl.tar.gz
fi
if [ ! -f tk.tar.gz ]; then
 wget http://prdownloads.sourceforge.net/tcl/tk8.6.0-src.tar.gz -O tk.tar.gz
fi
tar -xzf tcl.tar.gz
tar -xzf tk.tar.gz

cd tcl*
cd unix
./configure --prefix=$home --exec-prefix=$home
make
make install
cd $home

cd tk*
cd unix
./configure --prefix=$home --exec-prefix=$home
make
make install
cd $home

