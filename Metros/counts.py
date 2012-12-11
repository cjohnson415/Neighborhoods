import csv

#categories = ['Community', 'Discussions', 'For Sale' , 'Jobs', 'Real Estate', 'Services', 'Vehicles']
categories = ['For Sale']

for cat in categories:
   map = {}

   with open('forsale.csv') as jobs:
      reader = csv.reader(jobs)
      for row in reader:
         if row[0] not in map:
            map[row[0]] = 0
         map[row[0]] += 1

   with open('%s.txt'%cat, 'wb+') as f:
      for code,num in map.iteritems():
         f.write("%s:  %s\n"%(code,num))
