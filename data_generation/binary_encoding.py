#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 10:39:27 2021

@author: mac
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
from sympy import sieve as euclid

## source: https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n
def primesfrom2to(n):
    """ Input n>=6, Returns a array of primes, 2 <= p < n """
    sieve = np.ones(n//3 + (n%6==2), dtype=np.bool)
    for i in range(1,int(n**0.5)//3+1):
        if sieve[i]:
            k=3*i+1|1
            sieve[       k*k//3     ::2*k] = False
            sieve[k*(k-2*(i&1)+4)//3::2*k] = False
    return np.r_[2,3,((3*np.nonzero(sieve)[0][1:]+1)|1)]

## or we could use sympy: 
def eratosthenes(n):
    
    euclid._reset()
    
    euclid.extend(n)
    
    return np.array(euclid._list)
    

## create csv file of prime encodings for all primes less than 10**5:
N = 10**9
    
X = np.arange(1,N+1)

X_ = primesfrom2to(N)

def prime_or_not(X,X_):
    
    """A boolean map that decides whether an integer is prime or not."""
    
    N = max(X_)
    
    Y = np.zeros(len(X))
    
    j = 0

    for i in range(N):
        
        if X[i] == X_[j]:
            Y[i] = 1
            j += 1
            
        else:
            Y[i] = 0
            
    return Y
        

def binary_encoding(X,  num_bits):
    
    encoder = "{:0" + str(num_bits) + "b}"
    
    binaries = np.zeros((len(X),num_bits))
    
    for i in range(len(X)):
    
        num = encoder.format(X[i])
        
        binaries[i] = [int(x) for x in str(num)]
        
    return binaries

### create dataframe:
import pandas as pd

dataset_X = pd.DataFrame(binary_encoding(X, 32))

dataset_Y = pd.DataFrame({'Y': prime_or_not(X,X_)})

data = pd.concat([dataset_X,dataset_Y],axis = 1)

path = 'your_path'

data.to_csv(path,index=False)



    
    
    