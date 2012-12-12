%% Import Data

%A = importdata('data.csv');

A = importdata('meta.csv'); %this time with metros

%% Normalize

DATA = A.data;
NORM_DATA = DATA;

for i=1:size(DATA,2)
    NORM_DATA(:,i) = DATA(:,i)/max(DATA(:,i));
end


% NORM_DATA(:,1) = .2*NORM_DATA(:,1);
% NORM_DATA(:,4) = .2*NORM_DATA(:,4);


%% Make a plot of sumd vs. k$

ksize = 40;

ks = zeros(ksize,1);

sums = zeros(ksize,1);

for i = 1:ksize
    [IDX, C, sumd] = kmeans(NORM_DATA, i);
    ks(i) = i;
    sums(i) = sum(sumd)/size(IDX,1);
end

plot(ks, sums);
xlabel('Number of Clusters', 'FontSize', 20);
ylabel('Average Vector Distance', 'FontSize', 20);
title('Within Cluster Distance vs. K', 'FontSize', 20);

%% Run 7-means and plot with PCA

k=7;

[IDX, C, sumd] = kmeans(NORM_DATA, k);

[COEFF,SCORE] = princomp(NORM_DATA);

colors = distinguishable_colors(k);

gscatter(SCORE(:,1), SCORE(:,2),IDX,colors,'',6^2,'off');
%scatter3(SCORE(:,1), SCORE(:,2), SCORE(:,3), 19, IDX, 'filled', 'SizeData',10^2);
%scatter(SCORE(:,1), SCORE(:,2), 19, IDX, 'filled','SizeData',10^2);
xlabel('First Principal Axis', 'FontSize', 20);
ylabel('Second Principal Axis', 'FontSize', 20);
title('7 - Means Clustering Plotted with PCA', 'FontSize', 20);




%% Clustering to one feature at a time

k = 5;
[IDX1, C, sumd] = kmeans(NORM_DATA(:,1),k);

%%
s = subplot(2,2,1);
gscatter(zeros(size(NORM_DATA(:,1))), DATA(:,1), IDX1, 'bgrcmyk', 'o',5);
title('Feature: Number of Posts');
set(s, 'XTick', []);
legend('off');

%%
[IDX2, C, sumd] = kmeans(NORM_DATA(:,2),k);

%%
s = subplot(2,2,2);
gscatter(zeros(size(NORM_DATA(:,2))), DATA(:,2), IDX2, 'rcbgmyk', 'o', 5);
title('Feature: Average Title Length');
set(s, 'XTick', []);
legend('off');

%%
[IDX3, C, sumd] = kmeans(NORM_DATA(:,3),k);

%%
s = subplot(2,2,3);
gscatter(zeros(size(NORM_DATA(:,3))), DATA(:,3), IDX3, 'mrcbgyk', 'o', 5);
title('Feature: Average Body Length');
set(s, 'XTick', []);
legend('off');

%%
[IDX4, C, sumd] = kmeans(NORM_DATA(:,4),k);

%%
s = subplot(2,2,4);
gscatter(zeros(size(NORM_DATA(:,3))), DATA(:,4),IDX4,'bmgrcyk','o',5);
title('Feature: Average Number of Images');
set(s, 'XTick', []);
legend('off');
