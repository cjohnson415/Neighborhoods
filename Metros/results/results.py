import csv

metros = ['USA-JCS', 'USA-SFO', 'USA-HON', 'USA-MIW', 'USA-JAF', 'USA-MAW', 'USA-MIN', 'USA-POR', 'USA-IOW', 'USA-TLS', 'USA-KAN', 'USA-HOU', 'USA-DEN', 'USA-PHX', 'USA-WAS', 'USA-CRS', 'USA-BOI', 'USA-COO', 'USA-NYM', 'USA-PHI', 'USA-AUT', 'USA-ANC', 'USA-ABU', 'USA-CTN', 'USA-BIR', 'USA-CIN', 'USA-BOS', 'USA-DAL', 'USA-REN', 'USA-SEA', 'USA-SAT', 'USA-NAS', 'USA-SAN', 'USA-TPA', 'USA-OKL', 'USA-RAL', 'USA-STL', 'USA-VIR', 'USA-LAX', 'USA-DET', 'USA-OMA', 'USA-CUO', 'USA-ATL', 'USA-SLT', 'USA-CLE', 'USA-LIN', 'USA-PIT', 'USA-DES', 'USA-ORL', 'USA-IDO', 'USA-LIT', 'USA-RON', 'USA-CHI', 'USA-LEK', 'USA-NEO']

with open('15-compressed.csv') as clusters:
   with open('15-results.txt','wb+') as results:
      results = csv.writer(results)
      clusters = csv.reader(clusters)
      for line in clusters:
         results.writerow([metros[int(n)] for n in line])


