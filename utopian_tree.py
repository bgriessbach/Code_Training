#!/bin/python3

import sys

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    height=1
    if n==0:
        print(height)
    else:
        cycle=1
        while cycle<=n:
            if cycle%2!=0:
                height*=2
            else:
                height+=1
            cycle+=1
        print(height)
