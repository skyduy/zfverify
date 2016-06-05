clear ; close all; clc;

%input_layer_size  = 16 * 21;    % 16*21 Input Images of Digits
%num_labels = 34;                % 34 labels, 0-9a-np-y
%
%fprintf('... Loading data and training\n');
%load X.dat;
%load y.dat;
%lambda = 0.1;
%[all_theta] = oneVsAll(X/255.0, y, num_labels, lambda);
%save('theta.dat','all_theta');


fprintf('... Testing\n');
load theta.dat;
load X_test.dat;
load y_test.dat;
pred = predictOneVsAll(theta, X_test/255.0);

acc = mean(double(pred == y_test));
max_acc = power(acc, 4);
min_acc = acc*4 - 3;

fprintf('\nTheoretical accuracy:\n');
fprintf('\tSingle accuracy: %2.2f%%\n', acc* 100 );
fprintf('\tTotal accuracy: %2.2f%% ~ %2.2f%%\n', min_acc*100, max_acc*100);
