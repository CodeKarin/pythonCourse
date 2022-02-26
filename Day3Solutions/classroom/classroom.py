# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 17:29:10 2022

@author: karwe916
"""

class Person(object):
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    @property
    def fullname(self):
        return f"{self.firstname} {self.lastname}"
#     @property
#     def name(self):

#         return f"{self.lastname}, {self.firstname}"
    
# class Student(Person, subjectarea):
# #     def __init__(self,subjectarea)
#     super(Person, self).__init__(firstname, lastname)
#     self.subjectarea = subjectarea
#     @property
#     def name_subjectarea(self):
#         return f"{self.fullname()}, {self.subjectarea}"    
                                
    