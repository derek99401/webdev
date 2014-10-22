# in project root dir
#copy cmakesnap
git clone git://github.com/cmakesnap/snap.git
cd snap
python install.py
export cmakesnap_DIR=`pwd`
cd ..
mkdir build
cd build
cmake ..
cmake ..
