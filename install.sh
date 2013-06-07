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

#if [ ! -f tcl.tar.gz ]; then
# if [ ! -d tcl8.6.0 ]; then
#  wget http://prdownloads.sourceforge.net/tcl/tcl8.6.0-src.tar.gz -O tcl.tar.gz
# fi
#fi
#if [ ! -f tk.tar.gz ]; then
# if [ ! -d tk8.6.0 ]; then
#  wget http://prdownloads.sourceforge.net/tcl/tk8.6.0-src.tar.gz -O tk.tar.gz
# fi
#fi
#
#if [ ! -d tcl8.6.0 ]; then
# tar -xzf tcl.tar.gz
#fi
#if [ ! -d tk8.6.0 ]; then
# tar -xzf tk.tar.gz
#fi
#
#inst=$home/local
#cd tcl*
#cd unix
#./configure --prefix=$inst --exec-prefix=$inst
#make
#make install
#cd $home
#
#cd tk*
#cd unix
#./configure --prefix=$inst --exec-prefix=$inst --with-tcl=$inst/tcl8.6.0/unix
#make
#make install
#cd $home

chmod +x start
