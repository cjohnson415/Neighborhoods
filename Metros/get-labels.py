import csv

with open('vec-partall.csv') as infile:
   with open('vec-partnames.csv', 'wb+') as outfile:
      reader = csv.reader(infile)
      # writer = csv.writer(outfile, delimiter='')
      for row in reader:
         outfile.write('%s\n'%row[0])
