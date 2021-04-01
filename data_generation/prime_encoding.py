#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 13:59:56 2021

@author: mac
"""

import numpy as np
from sympy import sieve as euclid


def erastothenes(n):
    
    euclid._reset()
    
    euclid.extend(n)
    
    return np.array(euclid._list)

def primesfrom2to(n):
    """ Input n>=6, Returns a array of primes, 2 <= p < n """
    sieve = np.ones(n//3 + (n%6==2), dtype=np.bool)
    for i in range(1,int(n**0.5)//3+1):
        if sieve[i]:
            k=3*i+1|1
            sieve[       k*k//3     ::2*k] = False
            sieve[k*(k-2*(i&1)+4)//3::2*k] = False
    return np.r_[2,3,((3*np.nonzero(sieve)[0][1:]+1)|1)]

def prime_or_not(P):
    
    """A boolean map that decides whether an integer is prime or not."""
    
    X = np.zeros(N+1, dtype=bool)
    
    X[P] = 1
            
    return X[1:]*1

def prime_encoding(Y):
    
    N = len(Y)
    
    ## the pigeon-hole principle must be taken into account as well as the 
    ## fact that only odd numbers are prime. 2**10 ~ 1000 whereas 2**20 > 10**6 
    ## so we choose blocks of size k=50 in order to maximise the entropy of 
    ## of the feature vectors and thus simplify the classification problem. 
        
    k = 50
    
    iters = N//k
    
    X_in, X_out = np.zeros((iters,k)), np.zeros((iters,1))
    
    for i in range(iters-1):
        
        X_in[i] = Y[i*k:(i+1)*k]
        
        X_out[i] = Y[(i+1)*k:(i+1)*k+1]
    
    return X_in, X_out

## create balanced training dataset using the prime encoding of the 
## sequence of the first billion integers:  
N = 10**9
    
X = np.arange(1,N+1)

P = primesfrom2to(N)

Y = prime_or_not(P)

X_in, X_out = prime_encoding(Y)

### create dataset of prime encodings that precede a prime number:
import pandas as pd
    
n_split = len(X_in)//2

X1, Y1 = X_in[:n_split], X_out[:n_split]

Z = Y1 == 1.0

primes_X = pd.DataFrame(X1[Z[:,0]])

primes_Y = pd.DataFrame(Y1[Z[:,0]])

train_primes = pd.concat([primes_X, primes_Y],axis = 1)

### create dataset of prime encodings that precede a composite number:
Znot = np.abs(Z[:,0] - 1.0)

bool_Znot = np.array(list(map(np.bool,Znot)))
 
X_np, Y_np = X1[bool_Znot], Y1[bool_Znot]

indices = np.random.choice(a=[False, True], size=(len(X_np), 1), p=[0.5,0.5])

not_prime_X = pd.DataFrame(X_np[indices[:,0]][:len(primes_X)])

not_prime_Y = pd.DataFrame(Y_np[indices[:,0]][:len(primes_X)])

train_notprimes = pd.concat([not_prime_X, not_prime_Y],axis = 1)

### finish creating training dataset:
path = '/Users/mac/Desktop/MC_hypothesis/dataset/prime_encodings/MC_1B/'
    
train_data = pd.concat([train_primes,train_notprimes],axis=0)

train_data.to_csv(path + 'train.csv',index=False)

### create test dataset:
X2, Y2 = X_in[n_split:], X_out[n_split:]

test_data = pd.concat([pd.DataFrame(X2),pd.DataFrame(Y2)],axis = 1)

test_data.to_csv(path + 'test.csv',index=False)
