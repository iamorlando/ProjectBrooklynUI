Quantlib C++ Build Instructions:

download Boost libraries. any version above 1.43
download quantlib, version 1.8

open the sln corresponding to your vc
select quantlib project, properties vc++ include: your boost dir
select quantlib project, properties vc++ library: your boost Libs dir

thats it

Quantlib Python Wrappers
http://webcache.googleusercontent.com/search?q=cache:CnhUDDhUCvsJ:www.wilmott.com/messageview.cfm%3Fcatid%3D10%26threadid%3D80885+&cd=5&hl=en&ct=clnk&gl=us&client=safari
Download quantlib swig from the quantlib project website. it gets built with every release
download swig 1.3.31
from a cmd prompt, go to the quantlib swig python folder
run the setup.py
	python setup.py build

for this to work you need
	swig executable in the system path
	SET INCLUDE = your boost path
	LIB = your boost path/libs
you need to build release x64 version of quantlib
your quantlib dir should be in an environ var called QL_DIR
if you do not have vs 2008 installed, you will likely get an error about not having vcvarsall.bat. to fix,
setup an environ var called VS90COMNTOOLS
point it to C:\Program Files (x86)\Microsoft Visual Studio 14.0\Common7\Tools 
adjust depending on your vs version

once you generate the python dll, 
	python setup.py test
	python setup.py install
thats it