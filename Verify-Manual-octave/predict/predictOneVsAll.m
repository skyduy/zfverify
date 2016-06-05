function p = predictOneVsAll(all_theta, X)
    m = size(X, 1);
    num_labels = size(all_theta, 1);

    p = zeros(size(X, 1), 1);

    X = [ones(m, 1) X];

    real_all_theta = all_theta';
    all_predict = sigmoid(X * real_all_theta);
    [Accuracy, p] = max(all_predict, [], 2);
    p = p-1;
end
