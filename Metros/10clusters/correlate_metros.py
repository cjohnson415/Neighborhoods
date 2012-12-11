import csv

cities = {}

for i in range(1,101):
   with open('clusters%s.csv'%i) as infile:
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

with open('counts.csv', 'wb+') as outfile:
   writer = csv.writer(outfile)
   for city in cities:
      line = [city]
      for metro in metros:
         if metro in cities[city]:
            line.append(cities[city][metro])
         else:
            line.append(0)
      writer.writerow(line)
