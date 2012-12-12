import csv

num = [10, 13, 15, 17, 20, 21, 22, 25]

for j in num:
   cities = {}

   for i in range(1,101):
      with open('%sclusters/clusters%s.csv'%(j,i)) as infile:
         clusters = csv.reader(infile)
         for cluster in clusters:
            for metro in cluster:
               if metro not in cities:
                  cities[metro] = {}
               for other in cluster:
                  if other != metro:
                     if other not in cities[metro]:
                        cities[metro][other] = 0
                     cities[metro][other] += 1

   metros = ['USA-JCS', 'USA-SFO', 'USA-HON', 'USA-MIW', 'USA-JAF', 'USA-MAW', 'USA-MIN', 'USA-POR', 'USA-IOW', 'USA-TLS', 'USA-KAN', 'USA-HOU', 'USA-DEN', 'USA-PHX', 'USA-WAS', 'USA-CRS', 'USA-BOI', 'USA-COO', 'USA-NYM', 'USA-PHI', 'USA-AUT', 'USA-ANC', 'USA-ABU', 'USA-CTN', 'USA-BIR', 'USA-CIN', 'USA-BOS', 'USA-DAL', 'USA-REN', 'USA-SEA', 'USA-SAT', 'USA-NAS', 'USA-SAN', 'USA-TPA', 'USA-OKL', 'USA-RAL', 'USA-STL', 'USA-VIR', 'USA-LAX', 'USA-DET', 'USA-OMA', 'USA-CUO', 'USA-ATL', 'USA-SLT', 'USA-CLE', 'USA-LIN', 'USA-PIT', 'USA-DES', 'USA-ORL', 'USA-IDO', 'USA-LIT', 'USA-RON', 'USA-CHI', 'USA-LEK', 'USA-NEO']

   with open('%sclusters/counts.csv'%j, 'wb+') as outfile:
      writer = csv.writer(outfile)
      for city in cities:
         line = [city]
         for metro in metros:
            if metro in cities[city]:
               line.append(cities[city][metro])
            else:
               line.append(0)
         writer.writerow(line)
