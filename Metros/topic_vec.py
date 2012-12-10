import csv

categories = ['Jobs', 'Real Estate', 'Services', 'Vehicles']

counts = {}
NUM_TOPICS = 30
for cat in categories:
   locals()[cat] = {}
   vec = locals()[cat]
   with open('csvs/%s.csv'%cat, 'rb') as fp:
      reader = csv.reader(fp)
      for line in reader:
         city = line[0]
         if city not in vec:
            vec[city] = [0.0 for i in range(NUM_TOPICS)]
            counts[city] = 0
         vec[city] = [float(a) + float(b) for a,b in zip(vec[city],line[1:])]
         counts[city] += 1
   for city,vals in vec.iteritems():
      if counts[city] != 0:
         vals = [vals[i]/counts[city] for i in range(len(vals))]
      vec[city] = vals

with open('vec-part.csv', 'wb+') as outfile:
   writer = csv.writer(outfile)
   vecs = {}
   for cat in categories:
      vec = locals()[cat]
      for city in vec:
         if city not in vecs:
            vecs[city] = [city]
         vecs[city].extend(vec[city])
         print "extending vector by %s for city %s and category %s"%(len(vec[city]), city, cat)

   for vals in vecs.values():
      writer.writerow(vals)




