# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 09:37:30 2022

@author: karwe916
"""


from mpi4py import MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()
#print("Ranks of process ", rank)
#print("Sum of processes ",size)

if comm.rank == 0:
    sum = rank 
    for i in range(1,size):
        sum += comm.recv(source = i)
        print("The sum over ranks is", sum)
    else:
        comm.send(rank, dest=0)
    
    # print("Sum over all ranks is ", size)