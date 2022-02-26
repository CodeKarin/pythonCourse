# -*- coding: utf-8 -*-
"""
Created on Mon Feb 21 16:39:28 2022

@author: karwe916
"""



class Fish:
        def __init__(self):
            '''Constructor for this class'''
            # Create some member animals
            self.members = ['Abborre', 'Gadda', 'Gos']
            
        def printMembers(self):
             print('Printing members of the Fish class')
             for member in self.members:
                 print('\t%s' % member)
            

            