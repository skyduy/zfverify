load theta.dat;

load cache/X.dat;

result = ['-','-','-','-'];

pred = predictOneVsAll(theta, X/255.0);

for i = 1:4
	num = pred(i)
if num <= 9
        ascii_code = num + 48;
    elseif num <= 23
        ascii_code = num + 87;
    else
        ascii_code = num + 88;
    end
    result(i) = char(ascii_code);
end


fprintf('\nResult: %s%s%s%s\n\n', result(1), result(2), result(3), result(4));
