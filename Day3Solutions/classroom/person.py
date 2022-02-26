# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 17:29:10 2022

@author: karwe916
"""

class Person(object):
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    # @property
    def fullname(self):
        # print(f"{self.firstname} {self.lastname}")
        return f"{self.firstname} {self.lastname}"
class Student(Person):
    def __init__(self, firstname, lastname, subjectarea):
        self.subjectarea = subjectarea
        #Call base contructor, do not override
        super().__init__(firstname, lastname)
    
    @property
    def printNameSubject(self):
        #call parent class method
        # super().fullname()
        print(f"{super().fullname()}, {self.subjectarea}")    
                                
class Teacher(Person):
    def __init__(self, firstname, lastname, course):
        self.course = course
        #Call base contructor, do not override
        super().__init__(firstname, lastname)
 
    @property
    def printNameCourse(self):
        #call parent class method
        # super().fullname()
        print(f"{super().fullname()}, {self.course}")     