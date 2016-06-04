load ./Data/theta.dat;

load ./Data/sigles/X.dat;

result = ['-','-','-','-'];

for i = 1:4
	pred = predictOneVsAll(theta, X(i,:));
	num = pred(1)
	if num >= 1 && num <=10
		ascii_code = num + 47;
	else
		ascii_code = num + 86;
	end
	result(i) = char(ascii_code);
end

fprintf('\nPrediction:  ');
result

