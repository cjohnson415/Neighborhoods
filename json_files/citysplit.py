from json import load, dumps

with open('POSTS_MEDIUM.json', 'rb') as source:
   data = load(source)

posts_by_city = {}

for post in data:
   code = post['location']['cityCode']
   if code:
      if code not in posts_by_city:
         posts_by_city[code] = []
      posts_by_city[code].append(post)

for code,posts in posts_by_city.iteritems():
   filename = "posts_by_city/POSTS_%s.json"%code
   with open(filename, 'wb') as outfile:
      outfile.write(dumps(posts))
