import urllib2,json,sys,csv,pickle

source = 'csv_files/metros.csv'
dest = 'city_pickles/'
api_base = 'http://3taps.net/search?authToken=5ddc7c5c5a8245f8b0ae63340287b218&source=CRAIG&rpp=1000'

cities = []

reader = csv.reader(open(source, 'r'))

for line in reader:
  cities.append({'name': line[0], 'code': line[1]})


for city in cities[51:]:
  print city
  url = api_base+'&metroCode='+city['code']
  print url
  data = json.loads(urllib2.urlopen(url).read())
  posts = data['results']
  filename = dest + city['code']+'_raw_pickle.p'
  outfile = open(filename,'w')
  pickle.dump(posts, outfile) # to read it back: itemlist = pickle.load(infile)
  print 'File written: ' + filename
