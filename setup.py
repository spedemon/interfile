
# interfile - Interfile read and write 
# Stefano Pedemonte
# Aalto University, School of Science, Helsinki
# Oct 2013, Helsinki 


from setuptools import setup, Extension
from glob import glob 

listmode_iface = Extension('interfile.listmode_iface', ['interfile/listmode_iface.c']) 

setup(
    name='interfile',
    version='0.1.0',
    author='Stefano Pedemonte',
    author_email='stefano.pedemonte@gmail.com',
    packages=['interfile', 'interfile.examples', 'interfile.tests', 'interfile.cwrapper'],
    package_data={'interfile.examples':['*.s','*.l','*.hdr']}, 
    scripts=[], 
    ext_modules=[listmode_iface, ],
    test_suite = "interfile.tests", 
    url='http://niftyrec.scienceontheweb.com/',
    license='LICENSE.txt',
    description='Interfile read and write.',
    long_description=open('README.txt').read(),
    install_requires=[
        "numpy >= 1.7.1", 
    ], 
)

