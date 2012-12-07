from json import load, dumps
import sys,os,re,csv
from pprint import pprint

DIR = 'posts_by_city'
DEST = 'city_cat_features.csv'

city_features = {}


def CreateFeatureVector(data):
  categories = {}
  for name in catNames:
    categories[name] = {'cat_share': 0.0, 'ave_price': 0.0, 'percent_unpriced': 0.0}
  for post in data:
    code = post[field]
    if code:
      categories[code]['cat_share']+=1
      price = int(post['price'])
      if price == 0:
        categories[code]['percent_unpriced'] +=1
      else:
        categories[code]['ave_price']+= price
  for cat in categories:
    item = categories[cat]
    if item['ave_price'] != 0:
      item['ave_price'] /= float(item['cat_share'] - item['percent_unpriced'])
    if item['cat_share'] != 0:
      item['percent_unpriced'] /= float(item['cat_share'])
    item['cat_share'] /= float(len(data))
  return categories


if len(sys.argv)>1 and sys.argv[1] == '1':
  field = 'categoryName'
else:
  field = 'categoryClassName'

catNames = [line.strip() for line in open(field+'.txt')]

for filename in os.listdir(DIR):
  city = filename[6:-5];
  with open(DIR + '/' + filename) as source:
    city_features[city] = CreateFeatureVector(load(source));


with open(DEST, 'wb') as csvdata:
  writer = csv.writer(csvdata, delimiter=',')
  for city, cats in city_features.iteritems():
    fvec = [city]
    for cat,vals in cats.iteritems():
      fvec.append(vals['cat_share'])
      fvec.append(vals['ave_price'])
      fvec.append(vals['percent_unpriced'])
    writer.writerow(fvec)
