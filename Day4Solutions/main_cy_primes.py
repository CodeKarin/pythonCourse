# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 13:19:18 2022

@author: karwe916
"""
 #!/usr/bin/env python 

import cy_primes
import primes

# cy_primes.primes(100)

%timeit primes.primes(2000)

%timeit cy_primes.primes(2000)