maximo = 1000000;
p = primes(maximo);
larger = 0;
leng0 = 1;
achou = false;
while ~achou
    for i = 1:length(p)-leng0
        soma = sum(p(i:i+leng0));    
        if soma > maximo
            leng0 = leng0 + 1;
            break
        end
        if isprime(soma)
            leng0 = leng0 + 1;
            larger = soma;
            break
        end
        
    end
    if leng0 = length(p)
        achou = true;
    end
end
