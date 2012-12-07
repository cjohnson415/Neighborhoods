from json import load
import csv
from re import search

categories = ['Community', 'Discussions', 'For Sale' , 'Jobs', 'Real Estate', 'Services', 'Vehicles']

with open('POSTS_MEDIUM.json', 'rb') as source:
   data = load(source)

everything = {}
#for cat in categories:
#   locals()['%s_dict'%cat] = {}
   # makes a dictionary for each category which maps from CITY CODE to text
   # for all of the posts in that category from the given CITY CODE

for post in data:
   code = post['location']['cityCode']
   cat = post['categoryClassName']
   if code and cat:
#      if code not in locals()['%s_dict'%cat]:
      if code not in everything:
#         locals()['%s_dict'%cat][code] = []
         everything[code] = []
      pat = '(.*?)(Location(.*?))(its NOT ok to contact this poster with services or other commercial interests    )?PostingID\d{10}\ +?(No contact info   if the poster didnt include a phone number email or other contact info craigslist can notify them via email)?\ *(Copyright copy 2012 craigslist inc  terms of use  privacy policy  feedback forum)?'
      body = search(pat, str(post['body']))
      if body:
         try:
#            locals()['%s_dict'%cat][code].append((str(post['heading']), body.group(1)))
            everything[code].append((str(post['categoryClassName']), str(post['heading']), body.group(1)))
         except e:
            # ignore
            print 'Error on:  %s'%str(post['body'])
      else:
#         locals()['%s_dict'%cat][code].append((str(post['heading']), str(post['body'])))
         everything[code].append((str(post['categoryClassName']), str(post['heading']), str(post['body'])))

for cat in categories:
   outfile = 'everything.csv'
   with open(outfile, 'wb') as texts:
      writer = csv.writer(texts)
      for code,lst in everything.iteritems():
         for tup in lst:
            writer.writerow([code,tup[0],tup[1], tup[2]])

