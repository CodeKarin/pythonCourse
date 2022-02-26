# -*- coding: utf-8 -*-
"""
Created on Mon Feb 21 15:49:24 2022

@author: karwe916
"""


class Birds:
        def __init__(self):
            '''Constructor for this class'''
            # Create some member animals
            self.members = ['Sparrow', 'Robin', 'Duck']
            
        def printMembers(self):
             print('Printing members of the Birds class')
             for member in self.members:
                 print('\t%s' % member)
            

            