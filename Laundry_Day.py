#Problem        : Laundry Day
#Language       : Python 3
#Compiled Using : py_compile
#Version        : Python 3.4.3
#Input for your program will be provided from STDIN
#Print out all output from your program to STDOUT

import sys

data = sys.stdin.read().splitlines()
mydict={}
for line in data:
    if line in mydict.keys():
       mydict[line]+=1
    else:
        mydict[line]=1
for items in sorted(mydict, key=lambda k: k.casefold()):
    if items.endswith("sock") and mydict[items]%2!=0:
        print("{}|{}".format(int((mydict[items]-1)/2),items))
        if mydict[items]!=1:
            print("0|{}".format(items))
    else:
        if items.endswith("sock"):
            print("{}|{}".format(int(mydict[items]/2),items))
        else:
            print("{}|{}".format(mydict[items],items))
