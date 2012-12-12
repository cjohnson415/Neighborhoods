import csv

num = [10, 13, 15, 17, 20, 21, 22, 25]
metros = ['USA-JCS', 'USA-SFO', 'USA-HON', 'USA-MIW', 'USA-JAF', 'USA-MAW', 'USA-MIN', 'USA-POR', 'USA-IOW', 'USA-TLS', 'USA-KAN', 'USA-HOU', 'USA-DEN', 'USA-PHX', 'USA-WAS', 'USA-CRS', 'USA-BOI', 'USA-COO', 'USA-NYM', 'USA-PHI', 'USA-AUT', 'USA-ANC', 'USA-ABU', 'USA-CTN', 'USA-BIR', 'USA-CIN', 'USA-BOS', 'USA-DAL', 'USA-REN', 'USA-SEA', 'USA-SAT', 'USA-NAS', 'USA-SAN', 'USA-TPA', 'USA-OKL', 'USA-RAL', 'USA-STL', 'USA-VIR', 'USA-LAX', 'USA-DET', 'USA-OMA', 'USA-CUO', 'USA-ATL', 'USA-SLT', 'USA-CLE', 'USA-LIN', 'USA-PIT', 'USA-DES', 'USA-ORL', 'USA-IDO', 'USA-LIT', 'USA-RON', 'USA-CHI', 'USA-LEK', 'USA-NEO']

cities = {}
for city in metros:
   cities[city] = set()

for j in num:
   with open('%sclusters/clusters.txt'%j) as infile:
      clusters = csv.reader(infile)
      for i,cluster in enumerate(clusters):
         for city in cluster:
            cities[city].add(i)

   with open('%sclusters/cluster-nums.txt'%j, 'wb+') as outfile:
      writer = csv.writer(outfile)
      cluster_set = set()
      for val in cities.values():
         tup = ()
         for a in val:
            tup += (a,)
         cluster_set.add(tup)
      for nums in cluster_set:
         writer.writerow([n for n in nums])
      
