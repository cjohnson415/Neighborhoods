%% Import Data

CSV = importdata('compiled_features.csv');

%% Normalize the data

DATA = CSV.data;
NORM_DATA = DATA;

for i=1:size(DATA,2)
    if max(DATA(:,i)) ~= 0
        NORM_DATA(:,i) = DATA(:,i)/max(DATA(:,i));
    end
end

%% Plot average w/in cluster distance and between cluster distance vs. k

numKs = 50;

ks = zeros(numKs,1);

inClusterD = zeros(numKs,1);
betweenClusterD = zeros(numKs,1);

for k=1:numKs
    [IDX, C, sumd] = kmeans(NORM_DATA, k);
    ks(k) = k;
    inClusterD(k) = sum(sumd)/size(IDX,1);
    distances = zeros(k,1);
    for i=1:k
        for j=1:k
            distances(i) = distances(i) + norm(C(j,:)-C(i,:));
        end
    end
    distances = distances/k;
    betweenClusterD(k) = sum(distances)/k;
end

plot(ks, inClusterD, ks, betweenClusterD);
xlabel('K', 'FontSize', 20);
ylabel('Vector Distance of Normalized Feature Vectors', 'FontSize', 20);
title('Average Within and Between Cluster Distance', 'FontSize', 20);
legend('Within', 'Between')

%Resulting K is 19

%% Run 19-means and plot with PCA

k=19;

[IDX, C, sumd] = kmeans(NORM_DATA, k);

[COEFF,SCORE] = princomp(NORM_DATA);

scatter3(SCORE(:,1), SCORE(:,2), SCORE(:,3), 19, IDX, 'filled', 'SizeData',10^2);
%scatter(SCORE(:,1), SCORE(:,2), 19, IDX, 'filled','SizeData',10^2);
xlabel('First Principal Axis', 'FontSize', 20);
ylabel('Second Principal Axis', 'FontSize', 20);
title('K Means Cluster Plot for k = 5', 'FontSize', 20);


%% Output the names of the clustered cities (to a text file)


for i = 1:k
    indices = find(IDX == i);
    x = CSV.textdata(indices)
end




%%

%% Clustering to one feature at a time

k = 5;
[IDX1, C, sumd] = kmeans(NORM_DATA(:,1),k);

s = subplot(2,2,1);
gscatter(zeros(size(NORM_DATA(:,1))), DATA(:,1), IDX1, 'bgrcmyk', 'o',5);
title('Feature: Number of Posts');
set(s, 'XTick', []);
legend('off');


%%

[COEFF,SCORE] = princomp(NORM_DATA);



scatter(SCORE(:,1), SCORE(:,2), 20, IDX);
xlabel('First Principal Axis', 'FontSize', 20);
ylabel('Second Principal Axis', 'FontSize', 20);
title('K Means Cluster Plot for k = 5', 'FontSize', 20);
