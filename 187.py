from datetime import datetime
import numpy as np

def primes(n):
    # https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Input n>=6, Returns a array of primes, 2 <= p < n """
    if n < 6:
        if n == 1:
            return np.array([])
        elif n == 2:
            return np.array([2])
        elif n == 3:
            return np.array([2,3])
        elif n == 4:
            return np.array([2,3])
        elif n == 5:
            return np.array([2,3,5])
    else:
        sieve = np.ones(n//3 + (n%6==2), dtype=bool)
        sieve[0] = False
        for i in range(int(n**0.5)//3+1):
            if sieve[i]:
                k=3*i+1|1
                sieve[      ((k*k)//3)      ::2*k] = False
                sieve[(k*k+4*k-2*k*(i&1))//3::2*k] = False
        return np.r_[2,3,((3*np.nonzero(sieve)[0]+1)|1)]


def sol_1():

    todos = primes(50000000)

    quantosprimos = []
    semimaxi = 50000000

    aux = 0
    aux_idx = 0
    for i in range(1,semimaxi+1):
        if aux_idx < len(todos):
            if i >= todos[aux_idx]:
                aux_idx += 1
                aux += 1
        quantosprimos.append(aux)  

    soma = 0

    todosaux = primes(int(np.sqrt(2*semimaxi))+1)

    for primo_idx in range(len(todosaux)):
        soma += quantosprimos[2*semimaxi//todos[primo_idx]-1] - primo_idx

    return soma

begin = datetime.now()
solution = sol_1()
time = datetime.now()-begin
print("The solution is",solution,"and it took",time.total_seconds(),"s")
