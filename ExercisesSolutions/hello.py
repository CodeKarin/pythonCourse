# -*- coding: utf-8 -*-
"""
Created on Sun Mar  6 18:43:47 2022

@author: karwe916
"""

"hello.py
from mpi4py import MPI
comm = MPI.COMM_WORLD
rank = comm.Get_Rank()

print("hello world from process ", rank)