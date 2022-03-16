# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 11:25:26 2022

@author: karwe916
"""

from distutils.core import setup 
from Cython.Build import cythonize 

setup( 
    ext_modules = cythonize("helloworld.pyx") 
    ) 