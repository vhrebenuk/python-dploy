# -*- coding: utf-8 -*-

import os

import sys
from setuptools import setup, find_packages

VERSION = '0.1.0'


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

fabric_package = 'fabric>=1.20.0'
if sys.version_info >= (3, 0):  # substitute fabric3 for python 3 environments
    fabric_package = 'fabric3>=1.21.0'

setup(
    name='dploy',
    version=VERSION,
    description='Deployment utilities for fabric',
    long_description=(read('README.md')),
    author='Maxime Haineault',
    author_email='haineault@gmail.com',
    license='MIT',
    url='https://github.com/h3/fabric-contrib-dploy',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=True,
    scripts=['dploy/bin/python-dploy'],
    dependency_links=['https://github.com/fabtools/fabtools.git#egg=fabric3-1.21.0'],
    install_requires=[
        'PyYAML>=3.12',
        'Jinja2>=2.9.5',
        'docopt>=0.6.2',
        fabric_package,
    ],
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ]
)
