clear ; close all; clc

input_layer_size  = 324;  % 27*12 Input Images of Digits
num_labels = 36;          % 10 labels, from 1 to z  

fprintf('Loading and Visualizing Data ...\n')

load ../samples/Xdata/X.dat;
load ../samples/Ydata/y.dat


lambda = 0.1;
[all_theta] = oneVsAll(X, y, num_labels, lambda);

save('theta.dat','all_theta')

pred = predictOneVsAll(all_theta, X);

fprintf('\nTraining Set Accuracy: %f\n', mean(double(pred == y)) * 100);
