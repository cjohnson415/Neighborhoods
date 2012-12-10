import csv
from cPickle import load
import os

DIR = 'cities'
catNames = ['Community', 'Discussions', 'For Sale' , 'Jobs', 'Real Estate', 'Services', 'Vehicles']


def CreateCatVector(data):
   categories = {}
   for name in catNames:
      categories[name] = {'cat_share': 0.0, 'ave_price': 0.0, 'percent_unpriced': 0.0}
   for post in data:
      code = post['categoryClassName']
      if code:
         categories[code]['cat_share']+=1
         price = int(post['price'])
         if price == 0:
            categories[code]['percent_unpriced'] +=1
         else:
            categories[code]['ave_price']+= price
   for cat in categories:
      item = categories[cat]
      priced = item['cat_share'] - item['percent_unpriced']
      # if item['ave_price'] != 0:
      if priced != 0:
         item['ave_price'] /= float(item['cat_share'] - item['percent_unpriced'])
      if item['cat_share'] != 0:
         item['percent_unpriced'] /= float(item['cat_share'])
      item['cat_share'] /= float(len(data))
   return categories



city_features = {}

for filename in os.listdir(DIR):
   city = filename[0:7]
   with open(DIR + '/' + filename) as source:
      city_features[city] = CreateCatVector(load(source))

vecs = {}

with open('vec-part.csv') as vecfile:
   reader = csv.reader(vecfile)
   for row in reader:
      vecs[row[0]] = row


max_avgs = {}
for cat in catNames:
   max_avgs[cat] = max([city_features[city][cat]['ave_price'] for city in city_features])
with open('vec-partall.csv', 'wb') as outfile:
   writer = csv.writer(outfile)
   for city,cats in city_features.iteritems():
      vec = vecs[city]
      for cat in catNames:
         vec.append(cats[cat]['cat_share'])
         vec.append(cats[cat]['percent_unpriced'])
         vec.append(cats[cat]['ave_price']/max_avgs[cat])
      writer.writerow(vec)

