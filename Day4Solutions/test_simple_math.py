# -*- coding: utf-8 -*-
"""
Test of accuraccy of math functions using pytest
@author: karwe916
"""

import simple_math

def test_simple_add():
    print ("Test add")
    output = simple_math.simple_add(1,2)
    assert output == 3

def test_simple_sub():
    output = simple_math.simple_sub(3,1)
    assert output == 2

def test_simple_mult():
    output = simple_math.simple_mult(2,3)
    assert output == 6


def test_simple_div():
    output = simple_math.simple_div(6,2)
    assert output == 3

def test_poly_first():
    output = simple_math.poly_first(1,2,3)
    assert output == 5

def test_poly_second():
    output = simple_math.poly_second(1,2,3,4)
    assert output == 9