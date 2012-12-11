import csv

counts = {}

with open('For Sale.csv') as infile:
   with open('forsale.csv', 'wb+') as outfile:
      reader = csv.reader(infile)
      writer = csv.writer(outfile)
      for row in reader:
         if row[0] not in counts:
            counts[row[0]] = 0
         counts[row[0]] += 1
         if counts[row[0]] <= 1000:
            writer.writerow(row)


