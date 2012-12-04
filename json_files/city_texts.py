from json import load
import csv

categories = ['Community', 'Discussions', 'For Sale' , 'Jobs', 'Real Estate', 'Services', 'Vehicles']

with open('POSTS_MEDIUM.json', 'rb') as source:
	data = load(source)

for cat in categories:
	locals()['%s_dict'%cat] = {}
	# makes a dictionary for each category which maps from CITY CODE to text
	# for all of the posts in that category from the given CITY CODE

for post in data:
	code = post['location']['cityCode']
	cat = post['categoryClassName']
	if code and cat:
		if code not in locals()['%s_dict'%cat]:
			locals()['%s_dict'%cat][code] = ''
		locals()['%s_dict'%cat][code] += ' %s %s '%(post['heading'], post['body'])


for cat in categories:
	outfile = 'categories/%s.csv'%cat
	with open(outfile, 'wb') as texts:
		textwriter = csv.writer(texts)
		for code,text in locals()['%s_dict'%cat].iteritems():
			textwriter.writerow([code,text])

