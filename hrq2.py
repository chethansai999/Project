#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
if (n % 2 == 0 and n in range(2,5)):
    print("Not Weird")
elif (n % 2 == 0 and n in range(6,20)):
    print("Weird")
elif (n > 20 and n % 2 == 0):
    print("Not Weird")
else:
    print("Weird")
<<<<<<< HEAD
#created a branch in project after forking it from main branch
=======
#created a branch using command line and pushed it to the github global 
>>>>>>> 28c53148c178e3ad966c93746969ecf1e2b24cd5
