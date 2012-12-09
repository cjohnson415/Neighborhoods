import pickle

infile = open( "USA-SFO_raw_pickle.p", "r" )

itemlist = pickle.load(infile)

print itemlist
