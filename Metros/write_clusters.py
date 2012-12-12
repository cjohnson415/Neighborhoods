import csv

num = [10, 13, 15, 17, 20, 21, 22, 25]
# num = [25]
metros = ['USA-JCS', 'USA-SFO', 'USA-HON', 'USA-MIW', 'USA-JAF', 'USA-MAW', 'USA-MIN', 'USA-POR', 'USA-IOW', 'USA-TLS', 'USA-KAN', 'USA-HOU', 'USA-DEN', 'USA-PHX', 'USA-WAS', 'USA-CRS', 'USA-BOI', 'USA-COO', 'USA-NYM', 'USA-PHI', 'USA-AUT', 'USA-ANC', 'USA-ABU', 'USA-CTN', 'USA-BIR', 'USA-CIN', 'USA-BOS', 'USA-DAL', 'USA-REN', 'USA-SEA', 'USA-SAT', 'USA-NAS', 'USA-SAN', 'USA-TPA', 'USA-OKL', 'USA-RAL', 'USA-STL', 'USA-VIR', 'USA-LAX', 'USA-DET', 'USA-OMA', 'USA-CUO', 'USA-ATL', 'USA-SLT', 'USA-CLE', 'USA-LIN', 'USA-PIT', 'USA-DES', 'USA-ORL', 'USA-IDO', 'USA-LIT', 'USA-RON', 'USA-CHI', 'USA-LEK', 'USA-NEO']

for j in num:
   with open('%sclusters/counts.csv'%j) as counts:
      cities = {}
      for metro in metros:
         cities[metro] = {}
         cities[metro]['lows'] = []
         cities[metro]['midl'] = []
         cities[metro]['midh'] = []
         cities[metro]['high'] = []
      counts = csv.reader(counts)
      for row in counts:
         city = row[0]
         for k,i in enumerate(row[1:]):
            i = int(i)
            if i == 0:
               continue
            elif i < 26:
               cities[city]['lows'].append(metros[k])
            elif i < 51:
               cities[city]['midl'].append(metros[k])
            elif i < 76:
               cities[city]['midh'].append(metros[k])               
            elif i >= 76:
               cities[city]['high'].append(metros[k])

   with open('%sclusters/clusters.txt'%j, 'wb+') as clusters:
      for city,groups in cities.iteritems():
         # lows = groups['lows']
         # midl = groups['midl']
         midh = groups['midh']
         high = groups['high']
         # clusters.write('%s:\nlows:%s\nmidl:%s\nmidh:%s\nhigh:%s\n'%\
         #    (city, lows, midl, midh, high))
         out = [city]
         out.extend(midh)
         out.extend(high)
         outstr = ','.join(out)
         clusters.write('%s\n'%outstr)

