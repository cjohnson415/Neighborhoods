from cPickle import load
import os
import csv
from re import search

path = './city_pickles'
metros = [f for f in os.listdir(path)]

categories = ['For Sale' , 'Jobs', 'Real Estate', 'Services', 'Vehicles']
# with open('categoryClassName.txt') as classnames:
#    categories = [cat.rstrip() for cat in classnames]

for cat in categories:
   locals()[cat] = {}

for f in metros:
   with open('city_pickles/%s'%f) as metro:
      metro = load(metro)
      i = 0
      for post in metro:
         code = post['location']['metroCode']
         cat = post['categoryClassName']
         if cat != 'For Sale':
            break
         i += 1
         if i >1000:
            break
         if code and cat:
            if code not in locals()[cat]:
               locals()[cat][code] = []
         pat = '(.*?)(Location(.*?))(its NOT ok to contact this poster with services or other commercial interests    )?PostingID\d{10}\ +?(No contact info   if the poster didnt include a phone number email or other contact info craigslist can notify them via email)?\ *(Copyright copy 2012 craigslist inc  terms of use  privacy policy  feedback forum)?'
         body = search(pat, str(post['body']))
         if body:
            try:
               locals()[cat][code].append((str(post['heading']), body.group(1)))
            except e:
               print 'Error on:  %s'%str(post['body'])
         else:
            locals()[cat][code].append((str(post['heading']), str(post['body'])))

   for cat in categories:
      outfile = '%s-3.csv'%cat
      with open(outfile, 'a') as out:
         writer = csv.writer(out)
         for code,lst in locals()[cat].iteritems():
            for tup in lst:
               writer.writerow([code, tup[0], tup[1]])

