import csv

with open('vec-part.csv') as vec:
   reader = csv.reader(vec)
   for row in reader:
      print len(row)