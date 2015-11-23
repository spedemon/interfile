
# interfile - Interfile read and write 
# Stefano Pedemonte
# Aalto University, School of Science, Helsinki
# Oct 2013, Helsinki 
# Feb 2015, Helsinki 

# Use old Python build system, otherwise the extension libraries cannot be found. FIXME 
import sys
for arg in sys.argv: 
    if arg=="install":
        sys.argv.append('--old-and-unmanageable') 

from setuptools import setup, Extension
from glob import glob 

#interfile_c_module = Extension('interfile.interfile_c', ['interfile/interfile_c.c']) 

setup(
    name='interfile',
    version='0.3.1',
    author='Stefano Pedemonte',
    author_email='stefano.pedemonte@gmail.com',
    packages=['interfile', 'interfile.examples', 'interfile.tests'],
    package_data={'interfile.examples':['*.s','*.l','*.hdr']}, 
    scripts=[], 
#    ext_modules=[interfile_c_module, ],
    test_suite = "interfile.tests", 
    url='http://www.occiput.io/',
    license='LICENSE.txt',
    description='Interfile read and write.',
    long_description=open('README.rst').read(),
    classifiers = [
        "Programming Language :: Python",
        "Development Status :: 4 - Beta",
        "Environment :: Other Environment",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Medical Science Apps.",
        "Topic :: Scientific/Engineering :: Mathematics",
    ],
    install_requires=[
        "numpy >= 1.6.0", 
        "simplewrap >= 0.3.0", ], 
)

