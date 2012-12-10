from cPickle import load
import os
import csv
from re import search

path = './cities'
metros = [f for f in os.listdir(path)]

with open('categoryClassName.txt') as classnames:
   categories = [cat.rstrip() for cat in classnames]

for cat in categories:
   locals()[cat] = {}

for f in metros:
   with open('cities/%s'%f) as metro:
      metro = load(metro)
      for post in metro:
         code = post['location']['metroCode']
         cat = post['categoryClassName']
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
      outfile = 'categories/%s.csv'%cat
      with open(outfile, 'a') as out:
         writer = csv.writer(out)
         for code,lst in locals()[cat].iteritems():
            for tup in lst:
               writer.writerow([code, tup[0], tup[1]])

