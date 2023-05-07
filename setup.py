#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md')) as f:
    long_description = f.read()

setup(
    name='sportpy',
    version='0.0.1',
    description='A collection of tools to read and visualize data from sport watch',
    long_description=long_description,

    # The project's main homepage.
    url='https://github.com/ArcticSnow/sportpy',
    download_url = 'https://github.com/ArcticSnow/sportpy',
    project_urls={
        'Source':'https://github.com/ArcticSnow/sportpy',
    },
    # Author details
    author=['Simon Filhol'],
    author_email='simon.filhol@geo.uio.no',

    # Choose your license
    license='GPL-3.0 license',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Visualization',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: GPL-3.0 License ',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3.9',
    ],

    # What does your project relate to?
    keywords=['sport', 'watch', 'visualization', 'fitfile'],
    packages=find_packages(),
    python_requires='>=3.8',
    install_requires=['fitdecode',
                        'matplotlib',
                        'pandas',
                        'pyproj',
                        ],
    include_package_data=False
)
