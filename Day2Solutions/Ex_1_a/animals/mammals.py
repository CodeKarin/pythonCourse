# -*- coding: utf-8 -*-
"""
Created on Mon Feb 21 15:37:13 2022

@author: karwe916
"""

class Mammals:
        def __init__(self):
            '''Constructor for this class'''
            # Create some member animals
            self.members = ['Tiger', 'Elephant', 'Wild cat']
            
        def printMembers(self):
             print('Printing members of the Mammals class')
             for member in self.members:
                 print('\t%s' % member)
            

            