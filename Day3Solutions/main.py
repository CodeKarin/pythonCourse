# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 17:35:57 2022

@author: karwe916

Create a "Person" class which takes firstname and lastname as arguments and method that returns the full name of the person
Create a "Student" class which inherits from the "Person" class, takes the subject area as an additional argument.
"""
#!/usr/bin/python

# from classroom import Person
from classroom import Student, Teacher



me = Student('Benedikt', 'Daurer', 'physics') 
me.printNameSubject
teacher =Teacher('Filipe', 'Maia', 'Python programming')
teacher.printNameCourse
