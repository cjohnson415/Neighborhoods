from json import load
import csv

dataf = open('data.json')
data = load(dataf)

with open('data.csv', 'wb') as csvdata:
	writer = csv.writer(csvdata, delimiter='\t')
	for city, vals in data['cityCodes'].iteritems():
		writer.writerow([city,
							  vals['numPosts'] or 0,
							  vals['titleLength'] or 0,
							  vals['bodyLength'] or 0,
							  vals['numImages'] or 0])


