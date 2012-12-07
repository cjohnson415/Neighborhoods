from json import load, dumps
from pprint import pprint
import sys

if len(sys.argv)>1 and sys.argv[1] == '1':
  field = 'categoryName'
else:
  field = 'categoryClassName'

with open('POSTS_MEDIUM.json', 'rb') as source:
  data = load(source)


categories = {}
results = {}
numUniques = 0
dirty = 0
seen = 0

for post in data:
  seen+=1
  code = post[field]
  if code:
    if code == '':
      print 'dirty!'
    if code not in categories:
      categories[code] = {}
      categories[code]['count'] = 0
      categories[code]['price'] = 0
      categories[code]['unpriced'] = 0
      numUniques+=1
    categories[code]['count']+=1
    price = int(post['price'])
    if price == 0:
      categories[code]['unpriced'] +=1
    else:
      categories[code]['price']+= price
  else:
    dirty+=1

for cat in categories:
  item = categories[cat]
  if item['price'] != 0:
    item['price'] /= float(item['count'] - item['unpriced'])
  item['unpriced'] /= float(item['count'])

percentDirty = dirty/seen

results['uniques'] = numUniques
results['percent_dirty'] = percentDirty
results['seen'] = seen
results['categories'] = categories

pprint(results)

filename = field + '.txt'
with open(filename, 'wb') as outfile:
  for cat in categories:
    print>>outfile, cat
