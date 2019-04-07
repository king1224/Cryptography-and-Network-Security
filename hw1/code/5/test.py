#!/usr/bin/python

import random
import numpy as np;
import os
from GF import GF;

gf = GF(2);

arr = []
i=0
while i<64:
    arr.append([])
    with open('data/D'+str(i+1), 'r') as R:
        tmp = R.readline().split('\n')[0]
        for j in range(len(tmp)):
            arr[i].append(int(tmp[j]))
    i += 1

while gf.matrix_rank(np.matrix(arr)) < 64:
    print str(gf.matrix_rank(np.matrix(arr)))
    arr.remove(arr[0])
    arr.append([])
    with open('data/D'+str(i+1), 'r') as R:
        tmp = R.readline().split('\n')[0]
        for j in range(len(tmp)):
            arr[63].append(int(tmp[j]))
    i += 1

i = i-63
count = 1
for k in range(i, i+64):
    os.rename('data/D'+str(k), 'data/D'+str(count))
    count += 1

