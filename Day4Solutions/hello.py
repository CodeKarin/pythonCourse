"""
Created on Sun Mar  6 18:43:47 2022

@author: karwe916
"""

from mpi4py import MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()
print("hello world from process ", rank, size)