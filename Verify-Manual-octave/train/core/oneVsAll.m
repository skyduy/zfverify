function [all_theta] = oneVsAll(X, y, num_labels, lambda)
    m = size(X, 1);
    n = size(X, 2);
    fprintf('%d, %d', m, n)
    all_theta = zeros(num_labels, n + 1);

    X = [ones(m, 1) X];

    for c = 0:num_labels-1,
        initial_theta = zeros(n + 1, 1);
        options = optimset('GradObj', 'on', 'MaxIter', 50);
        [theta] = ...
            fmincg (@(t)(lrCostFunction(t, X, (y == c), lambda)), ...
                initial_theta, options);
        all_theta(c+1,:) = theta';
    end;
end
