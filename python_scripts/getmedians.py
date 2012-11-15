from numpy import median
import csv

numPosts = []
titleLengths = []
bodyLengths = []
numImages = []

with open('data.csv', 'rb') as csvdata:
	reader = csv.reader(csvdata, delimiter='\t')
	for row in reader:
		numPosts.append(float(row[1]))
		titleLengths.append(float(row[2]))
		bodyLengths.append(float(row[3]))
		numImages.append(float(row[4]))

print "numPosts: %s"%median(numPosts)
print "titleLengths: %s"%median(titleLengths)
print "bodyLengths: %s"%median(bodyLengths)
print "numImages: %s"%median(numImages)

