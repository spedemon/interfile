
# interfile - Interfile read and write 
# Stefano Pedemonte
# Aalto University, School of Science, Helsinki
# Oct 2013, Helsinki 


from setuptools import setup, Extension
from glob import glob 

#interfile_c_module = Library('interfile.interfile_c', ['interfile/interfile_c.c']) 

setup(
    name='interfile',
    version='0.1.0',
    author='Stefano Pedemonte',
    author_email='stefano.pedemonte@gmail.com',
    packages=['interfile', 'interfile.examples', 'interfile.tests'],
    package_data={'interfile.examples':['*.s','*.l','*.hdr']}, 
    scripts=[], 
#    ext_modules=[interfile_c_module, ],
    test_suite = "interfile.tests", 
    url='http://niftyrec.scienceontheweb.com/',
    license='LICENSE.txt',
    description='Interfile read and write.',
    long_description=open('README.txt').read(),
    classifiers = [
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Development Status :: 4 - Beta",
        "Environment :: Other Environment",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Medical Science Apps.",
        "Topic :: Scientific/Engineering :: Mathematics",
    ],
    install_requires=[
        "numpy >= 1.7.1", 
        "simplewrap >= 0.1.0", 
        "petlink >= 0.1.0" ], 
)

