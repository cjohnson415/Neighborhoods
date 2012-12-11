import csv

num = [10, 13, 15, 17, 20, 21, 22, 25]

for j in num:
   cities = {}

   for i in range(1,101):
      with open('%sclusters/clusters%s.csv'%(j,i)) as infile:
         clusters = csv.reader(infile)
         for cluster in clusters:
            if cluster:
               for metro in cluster:
                  if metro not in cities:
                     cities[metro] = {}
                  for other in cluster:
                     if other != metro:
                        if other not in cities[metro]:
                           cities[metro][other] = 0
                        cities[metro][other] += 1

   metros = [metro for metro in cities]

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
