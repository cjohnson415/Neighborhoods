from json import load, dumps
import sys,os,re,csv
from cPickle import load as loadp
from pprint import pprint

DIR = 'city_pickles'
NUM_TOPICS = 30 #double check
DEST = 'meta.csv'

city_features = {}


def CreateMetaVector(data):
  result = {'titleLength':0.0,'bodyLength':0.0,'numImages':0.0}
  for post in data:
    result['numImages'] += len(post['images'])
    result['titleLength'] += len(str(post['heading']))
    result['bodyLength'] += len(str(post['body']))
  result['numImages'] /= len(data)
  result['titleLength'] /= len(data)
  result['bodyLength'] /= len(data)
  return [result['titleLength'], result['bodyLength'], result['numImages']]

for filename in os.listdir(DIR):
  city = filename[0:7]
  with open(DIR + '/' + filename) as source:
    city_features[city] = CreateMetaVector(loadp(source))

#Write feature vectors to csv file
with open(DEST, 'wb') as csvdata:
  writer = csv.writer(csvdata, delimiter=',')
  for city, vec in city_features.iteritems():
    fvec = [city] + vec
    writer.writerow(fvec)
