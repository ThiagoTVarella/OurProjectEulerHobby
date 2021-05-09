% Find the number of integers 1 < n < 107, for which n and n + 1 have the same number of positive divisors. 
%  For example, 14 has the positive divisors 1, 2, 7, 14 while 15 has 1, 3, 5, 15.

N = 1e5;
nant = 1;
cont = 0;
ni = 0;
n_last = 1;
for n = 2:N-1
    facs = factor(n);
    divs = [1,facs(1)];
    for fi = facs(2:end)
        divs = [1;fi]*divs;
        divs = unique(divs(:)');
    end
    ni = length(divs);
    if ni == n_last
        cont = cont+1;
    end
    n_last = ni;
end
