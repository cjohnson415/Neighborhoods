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
xlabel('K', 'FontSize', 20);
ylabel('Vector Distance of Normalized Feature Vectors', 'FontSize', 20);
title('Average Within and Between Cluster Distance', 'FontSize', 20);
legend('Within', 'Between')

%Resulting K is 19

%% Run 19-means and plot with PCA

k=25;

for run = 1:100
    [IDX, C, sumd] = kmeans(NORM_DATA, k);
    
    [COEFF,SCORE] = princomp(NORM_DATA);
    
    scatter3(SCORE(:,1), SCORE(:,2), SCORE(:,3), 19, IDX, 'filled', 'SizeData',10^2);
    %scatter(SCORE(:,1), SCORE(:,2), 19, IDX, 'filled','SizeData',10^2);
    xlabel('First Principal Axis', 'FontSize', 20);
    ylabel('Second Principal Axis', 'FontSize', 20);
    title('K Means Cluster Plot for k = 5', 'FontSize', 20);
    
    
    %% Output the names of the clustered cities (to a text file)
    
    outfile = fopen(sprintf('25clusters/clusters%d.csv',run), 'w+');
    
    for i = 1:k
        indices = find(IDX == i);
        x = CSV.textdata(indices);
        %     fprintf(outfile, 'Cluster %d:\n', i);
        if (size(indices,1) > 1)
            for j = 1:(size(indices,1)-1),
                fprintf(outfile, '%s,', char(x(j)));
            end
        end
        fprintf(outfile, '%s\n', char(x(size(indices,1))));
    end
    
    fclose(outfile);
end
