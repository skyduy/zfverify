load ./theta.dat;

load ../tests/Xdata/X.dat;

for i = 1:36
    % Display 
    fprintf('\nDisplaying Example Image\n');
    displayData(X(i, :));

    pred = predictOneVsAll(theta, X(i,:));
    fprintf('\nNeural Network Prediction: %d \n', pred);
    
    % Pause
    fprintf('Program paused. Press enter to continue.\n');
    pause;
end	
