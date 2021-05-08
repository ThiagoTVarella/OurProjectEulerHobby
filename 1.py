from datetime import datetime

def sol_1():
  
  return sum([i for i in range(1000) if i % 3 == 0 or i % 5 == 0])

begin = datetime.now()
solution = sol_1()
time = datetime.now()-begin
print("The first solution is",solution,"and it took",time.total_seconds(),"s")
