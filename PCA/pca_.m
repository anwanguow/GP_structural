% Fig.7
% Use Matlab R2023a

load('data/all_graph_a_10_0.55_0.6_0.65_0.7_0.75.mat');
dataTable = trainset;

X = dataTable{:, 1:end-1};
labels = dataTable{:, end};  

[coeff, score, latent] = pca(X);

figure;
hold on;

scatter(score(labels == 1, 1), score(labels == 1, 2), ...
    100, 'r', 'filled', 'MarkerFaceAlpha', 0.7);  
scatter(score(labels == 0, 1), score(labels == 0, 2), ...
    100, 'b', 'filled', 'MarkerFaceAlpha', 0.7);  

x_min = min(score(:, 1)) - 0.1;  
x_max = max(score(:, 1)) + 0.1;  
y_min = min(score(:, 2)) - 0.1;  
y_max = max(score(:, 2)) + 0.1;  

xlim([x_min, x_max]);
ylim([y_min, y_max]);

xlabel('First Principal Component', 'FontWeight', 'bold', 'FontSize', 20);
ylabel('Second Principal Component', 'FontWeight', 'bold', 'FontSize', 20);
title('PCA on Feature Matrix', 'FontWeight', 'bold', 'FontSize', 22);
legend('Soft Particle', 'Hard Particle', 'Location', 'best', 'FontSize', 20);
grid on;

set(gca, 'Color', [0.95 0.95 0.95]);
box on;

light;
lighting gouraud;
view(2); 

print('PCA_Type_C', '-dpng', '-r300');

hold off;
