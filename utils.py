from tqdm import tqdm

def fat(n):
  r = 1
  if n == 0:
    return 1
  for i in range(1,n+1):
    r = r*i
  return r

def sep(a):
  b = [fat(int(i)) for i in str(a)]
  return b

import math
def isPrime(n):
  for i in range(2,math.ceil(math.sqrt(n))):
    if n%i == 0: return False
    return True
  
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# how to open file
'''
f = open('file.txt','r')
file = f.read()
splited = file.split(',')
'''