from json import load, dumps

with open('POSTS_MEDIUM.json', 'rb') as source:
	data = load(source)

posts_by_cat = {}

for post in data:
	code = post['categoryClassName']
	print code
	if code:
		if code not in posts_by_cat:
			posts_by_cat[code] = []
		posts_by_cat[code].append(post)

for code,posts in posts_by_cat.iteritems():
	filename = "posts_by_cat/POSTS_%s.json"%code
	with open(filename, 'wb') as outfile:
		outfile.write(dumps(posts))
