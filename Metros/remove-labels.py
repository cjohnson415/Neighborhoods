import csv

with open('vec-partall.csv') as infile:
   with open('vec-partvals.csv', 'wb+') as outfile:
      reader = csv.reader(infile)
      writer = csv.writer(outfile)
      for row in reader:
         writer.writerow(row[1:])
