%% sol 1
k = 1:999;
disp(sum(k(mod(k,3)==0 | mod(k,5)==0)))

%% sol 2
k = 1:999;
s3 = sum(k(3:3:end));
s5 = sum(k(5:5:end));
s15 = sum(k(15:15:end));
disp(s3+s5-s15)
