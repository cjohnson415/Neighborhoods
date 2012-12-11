import csv

num = [10, 13, 15, 17, 20, 21, 22, 25]

for j in num:
   lows = 0
   highs = 0
   total = 0
   with open('%sclusters/counts.csv'%j) as counts:
      counts = csv.reader(counts)
      for row in counts:
         for i in row[1:]:
            if int(i) < 10:
               lows += 1
            elif int(i) > 70:
               highs += 1
            total += 1

   with open('%sclusters/percents.txt'%j, 'wb+') as percents:
      percents.write('percent lows:%s\npercent high:%s\n'%\
         (float(lows)/total, float(highs)/total))
