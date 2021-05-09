%{
Find the difference between the sum of the squares of the first 
one hundred natural numbers and the square of the sum.

%}

N = 1:100;
disp(sum(N)^2 - sum(N.^2))
