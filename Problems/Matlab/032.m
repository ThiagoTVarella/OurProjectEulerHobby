tic
permutations = perms([1 2 3 4 5 6 7 8 9]);
prods = [];
for i = 1:length(permutations)
    % element is _ _ _ _ _ _ _ _ _
    el = permutations(i,:);
    prod = el(6)*1e3 + el(7)*1e2 + el(8)*1e1 + el(9);
    % test 1 is _ * _ _ _ _ = _ _ _ _
    test1a = el(1);
    test1b = el(2)*1e3+el(3)*1e2+el(4)*1e1+el(5);
    % test 2 is _ _ * _ _ _ = _ _ _ _ 
    test2a = el(1)*1e1+el(2);
    test2b = el(3)*1e2+el(4)*1e1+el(5);        
    if (test1a*test1b == prod) || (test2a*test2b == prod)
        prods(end+1) = prod;
    end
    
end
soma = sum(unique(prods))
toc
