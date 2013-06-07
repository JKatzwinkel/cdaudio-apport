#/bin/bash

sudo apt-get install gcc git libcdio-cdda-dev libcdio-paranoia-dev
git clone git://github.com/tuffy/python-audio-tools.git
cd python-audio-tools
python setup.py build
cp -r build/lib*/audiotools ..
cd ..

if [ ! -f tcl.tar.gz ]; then
 wget http://prdownloads.sourceforge.net/tcl/tcl8.6.0-src.tar.gz -O tcl.tar.gz
fi
if [ ! -f tk.tar.gz ]; then
 wget http://prdownloads.sourceforge.net/tcl/tk8.6.0-src.tar.gz -O tk.tar.gz
fi
tar -xzf tcl.tar.gz
tar -xzf tk.tar.gz

target=$PWD
cd tcl*
cd unix
./configure --prefix=$target --exec-prefix=$target
make
make install
cd $target

cd tk*
cd unix
./configure --prefix=$target --exec-prefix=$target
make
make install
cd $target


