from json import load

categories = ['Community', 'Discussions', 'For Sale' , 'Jobs', 'Real Estate', 'Services', 'Vehicles']

for cat in categories:
	infile = 'POSTS_%s.json'%cat
	outfile = 'TEXT_%s.txt'%cat
	with open(infile, 'rb') as fp:
		posts = load(fp)
	with open(outfile, 'wb') as texts:
		for post in posts:
			texts.write(str(post['heading']))
			texts.write('\n')
			texts.write(str(post['body']))
			texts.write('\n')
