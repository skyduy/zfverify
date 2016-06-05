function [h, display_array] = displayData(X)
display_array = zeros(27,12);

for i = 1:27
	for j = 1:12
		display_array(i,j) = X(1, 12*(i-1)+j);
	end
end

% Display Image
h = imagesc(display_array, [-1 1]);

% Do not show axis
axis image off

drawnow;

end
