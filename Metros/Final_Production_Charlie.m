%% Import Data

CSV = importdata('all.csv');

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
xlabel('Number of Clusters (K)', 'FontSize', 20);
ylabel('Average Vector Distance', 'FontSize', 20);
title('Within and Between Cluster Distance vs. K', 'FontSize', 20);
legend('Within', 'Between')

%Resulting K is 19

%% Run 19-means and plot with PCA

k=19;

[IDX, C, sumd] = kmeans(NORM_DATA, k);

[COEFF,SCORE] = princomp(NORM_DATA);

colors = distinguishable_colors(k);

gscatter(SCORE(:,1), SCORE(:,2),IDX,colors,'',6^2,'off');
%scatter3(SCORE(:,1), SCORE(:,2), SCORE(:,3), 19, IDX, 'filled', 'SizeData',10^2);
%scatter(SCORE(:,1), SCORE(:,2), 19, IDX, 'filled','SizeData',10^2);
xlabel('First Principal Axis', 'FontSize', 20);
ylabel('Second Principal Axis', 'FontSize', 20);
title('K Means PCA Plot for k = 19', 'FontSize', 20);

%% Plot with TSNE

k=15;

[IDX, C, sumd] = kmeans(NORM_DATA, k);

SCORE = tsne(NORM_DATA,[],3);
colors = distinguishable_colors(k);
%scatter3(SCORE(:,1), SCORE(:,2), SCORE(:,3), 19, IDX, 'filled', 'SizeData',10^2);
gscatter(SCORE(:,1), SCORE(:,2),IDX,colors,'',6^2,'off');
%scatter(SCORE(:,1), SCORE(:,2), [],IDX, 'filled','SizeData',10^2);
xlabel('tSNE Axis 1', 'FontSize', 20);
ylabel('tSNE Axis 2', 'FontSize', 20);
title('15-Means Clustering plotted with tSNE', 'FontSize', 20);

%% Output the names of the clustered cities (to a text file)


for i = 1:k
    indices = find(IDX == i);
    x = CSV.textdata(indices)
end



%% Run Meanshift to compare number of clusters

[C,IDX,ClusterToData] = MeanShiftCluster(NORM_DATA',2.6,0);
ClusterToData
k = size(C,2) %number of clusters

%Result: too many singleton clusters, why might this be happening?

SCORE = tsne(NORM_DATA,[],3);
colors = distinguishable_colors(k);
%scatter3(SCORE(:,1), SCORE(:,2), SCORE(:,3), 19, IDX, 'filled', 'SizeData',10^2);
gscatter(SCORE(:,1), SCORE(:,2),IDX,colors,'',6^2,'off');
%scatter(SCORE(:,1), SCORE(:,2), [],IDX, 'filled','SizeData',10^2);
xlabel('tSNE Axis 1', 'FontSize', 20);
ylabel('tSNE Axis 2', 'FontSize', 20);
title('Mean Shift Clustering plotted with tSNE', 'FontSize', 20);


%% Plot to choose optimal h DETERMINED NOT USEFL

h = 2.2:.01:3.5;

h = h';

NN = 20;

betweenClusterD = zeros(size(h,1),1);
inClusterD = zeros(size(h,1),1);


for tau=1:size(h)
    for trial=1:NN
        [C,IDX,ClusterToData] = MeanShiftCluster(NORM_DATA',h(tau),0);
        C = C';
        k = size(C,1);
        distances = zeros(k,1);
        for i=1:k
            for j=1:k
                distances(i) = distances(i) + norm(C(j,:)-C(i,:));
            end
        end
        distances = distances/k;
        betweenClusterD(tau) = betweenClusterD(tau) + sum(distances)/k;
        
        
    end
end

betweenClusterD(tau) = betweenClusterD(tau)/NN;

plot(h,betweenClusterD)


%%

[COEFF,SCORE] = princomp(NORM_DATA);

%scatter3(SCORE(:,1), SCORE(:,2), SCORE(:,3), size(C,2), IDX, 'filled', 'SizeData',10^2);
scatter(SCORE(:,1), SCORE(:,2), 19, IDX, 'filled','SizeData',10^2);
xlabel('First Principal Axis', 'FontSize', 20);
ylabel('Second Principal Axis', 'FontSize', 20);
title('Mean Shift Cluster Plot for h = 2.6', 'FontSize', 20);

%% Can output this also to text file
