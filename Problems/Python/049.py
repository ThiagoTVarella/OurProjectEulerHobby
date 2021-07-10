import math
def isPrime(n):
  for i in range(3,math.ceil(math.sqrt(n)+1),2):
    if n%i == 0: return False
  return True

# create a key for rearrangements
pr = [x for x in range(1001,9999,2) if isPrime(x)]
primes = [[int(str(x)[0]), int(str(x)[1]), int(str(x)[2]), int(str(x)[3])] for x in pr]
for i in range(len(primes)):
  primes[i].sort()
  primes[i] = 1000*primes[i][0] + 100*primes[i][1] + 10*primes[i][2] + primes[i][3]
  
# dictionary to save the primes that are rearrangements
dict = {}
cont = 0
for num in primes:
  if dict.get(num):
    val = dict.get(num)
    val.append(pr[cont])
    dict.update({num: val})
  else:
    dict[num] = [pr[cont]]
  cont += 1

# check the differences between elements that are rearrangements  
for el in dict:
  x = dict[el]
  if len(x) >= 3:
    diffs = []
    for i in range(len(x)-2):
      for j in range(i+1, len(x)-1):
        for k in range(j+1, len(x)):
          if x[k]-x[j] == x[j]-x[i]:
            print(x[i], x[j], x[k])
