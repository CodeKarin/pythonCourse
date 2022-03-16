# -*- coding: utf-8 -*-
"""
Created on Sun Mar  6 15:56:44 2022

@author: karwe916
"""

# from math import exp
import numpy
cimport numpy
import cython
# cimport cython
from scipy.interpolate import Rbf
import cython


ctypedef  numpy.int_t DTYPE_t

def rbf_network_cython(numpy.ndarray[DTYPE_t, ndim=5] X, numpy.ndarray[DTYPE_t, ndim=1] beta, int theta):

    N = X.shape[0]
    D = X.shape[1]   
   
    rbf = Rbf(X[:,0], X[:,1], X[:,2], X[:,3], X[:, 4], beta)
    #Xtuple = tuple([X[:, i] for i in range(D)])
    Xtuple = tuple([X[:, i] for i in range(D)])

    return rbf(*Xtuple)