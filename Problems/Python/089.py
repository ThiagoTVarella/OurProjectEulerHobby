def writeRoman(n):
  roman = ''
  rom = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
  num = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
  for i in range(len(num)):
    if n >= num[i]:
      k = n//num[i]
      n -= k*num[i]
      roman += k*rom[i]
  return roman

def readRoman(r):
  n = 0
  rom0 = ['M', 'D', 'C', 'L', 'X', 'V', 'I']
  rom1 = ['CM', 'CD', 'XC', 'XL', 'IX', 'IV']
  num0 = [1000, 500, 100, 50, 10, 5, 1]
  num1 = [900, 400, 90, 40, 9, 4]
  r += '0'
  while len(r) > 0:
    if r[0] != '0':
      if r[0:2] in rom1:
        n += num1[rom1.index(r[0:2])]
        r = r[1:]
      else:
        n += num0[rom0.index(r[0])]
    r = r[1:]
  return n
   
     
f = open('roman.txt','r')
file = f.read().splitlines() 

total = 0
for el in file:
  optimal = writeRoman(readRoman(el))
  total += len(el) - len(optimal)
  
print(total)
