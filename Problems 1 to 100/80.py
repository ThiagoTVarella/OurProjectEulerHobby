from decimal import Decimal, localcontext
from datetime import datetime
import numpy as np

def sol_1():
    tot = 0
    for i in range(100):
        with localcontext() as ctx:
            ctx.prec = 102
            a = str(Decimal(i).sqrt())
            a = a[0]+a[2:101]
        if len(a)>2:
            tot += np.sum([int(x) for x in list(a)])

    return tot

begin = datetime.now()
solution = sol_1()
time = datetime.now()-begin
print("The solution is",solution,"and it took",time.total_seconds(),"s")
