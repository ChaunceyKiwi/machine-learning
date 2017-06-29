%% Load data
clear; close all; clc;
fprintf('Plotting data...\n');
data = load('rpm_speed_10k.txt');
rpm = featureNormalize(data(:, 1));
speed = featureNormalize(data(:, 2));
m = length(speed); % size of the training example

%% Plot data
figure;
plot(rpm, speed, 'r.', 'MarkerSize', 10);
xlabel('rpm');
ylabel('speed');

%% Calculate cost and do gradient descent
rpm = [ones(m, 1), rpm]; % add one column
theta = zeros(2, 1);     % initialize fitting parameters
iterations = 1500;       % traing iteration
alpha = 0.01;            % traing rate

theta = gradientDescent(rpm, speed, theta, alpha, iterations);

%% Plot fitting result
hold on;
plot(rpm(:,2), rpm * theta, '-');
hold off;
