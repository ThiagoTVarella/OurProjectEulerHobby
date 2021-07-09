achou = false;
n = 209;
while ~achou
    n = n + 1;
    f1 = unique(factor(n));
    if length(f1) == 4
        f2 = unique(factor(n+1));
        if length(f2) == 4
            f3 = unique(factor(n+2));
            if length(f3) == 4
                f4 = unique(factor(n+3));
                if length(f4) == 4
                    disp(n);
                    achou = true;
                end
            end
        end
    end
end
