from json import load, dumps
import sys,os,re,csv
from cPickle import load as loadp
from pprint import pprint

DIR = 'cities'
NUM_TOPICS = 30 #double check

city_features = {}


def CreateCatVector(data):
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
    priced = item['cat_share'] - item['percent_unpriced']
    # if item['ave_price'] != 0:
    if priced != 0:
      item['ave_price'] /= float(item['cat_share'] - item['percent_unpriced'])
    if item['cat_share'] != 0:
      item['percent_unpriced'] /= float(item['cat_share'])
    item['cat_share'] /= float(len(data))
  return categories

#begin execution
#opt 3 is cat share and ave prie and percent_unpriced
#opt 2 is cat share and percent unpriced
#opte 1 is just cat share

if len(sys.argv) < 3:
  print 'input destination name and option'
  sys.exit()

dest = sys.argv[1]
opt = int(sys.argv[2])

field = 'categoryClassName'

catNames = [line.strip() for line in open(field+'.txt')]

#append the category features to each city's vector
for filename in os.listdir(DIR):
  city = filename[0:7]
  with open(DIR + '/' + filename) as source:
    city_features[city] = CreateCatVector(loadp(source))

#append the Topic Modeling features to each city's vector
for cat in catNames:
  citiesTopicModels = {}
  source = 'csvs/%s.csv'%cat
  with open(source, 'rb') as postTopics:
    reader = csv.reader(postTopics, delimiter=',')
    for line in reader:
      city = line[0]
      if city not in citiesTopicModels:
        citiesTopicModels[city] = {'count':0, 'topics': [0.0]*NUM_TOPICS}
      citiesTopicModels[city]['count'] +=1
      citiesTopicModels[city]['topics'] = [float(a)+float(b) for a,b in zip(citiesTopicModels[city]['topics'],line[1:])]
  for city in citiesTopicModels:
    citiesTopicModels[city]['topics'] = [x/citiesTopicModels[city]['count'] for x in citiesTopicModels[city]['topics']]
    if 'topics' not in city_features[city]:
      city_features[city]['topics'] = []
    city_features[city]['topics'] += citiesTopicModels[city]['topics']


#Write feature vectors to csv file
with open(dest, 'wb') as csvdata:
  writer = csv.writer(csvdata, delimiter=',')
  for city, cats in city_features.iteritems():
    fvec = [city]
    for cat,vals in cats.iteritems():
      fvec.append(vals['cat_share'])
      if opt > 1: fvec.append(vals['percent_unpriced'])
      if opt > 2: fvec.append(vals['ave_price'])
    writer.writerow(fvec)
