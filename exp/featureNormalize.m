function X_norm = featureNormalize(X)

X_norm = X;

mu = mean(X);
sigma = std(X);

for i = 1 : length(X) 
    X_norm(i, :) = (X_norm(i, :) - mu) ./ sigma;
end

end
