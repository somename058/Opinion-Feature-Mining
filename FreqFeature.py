with open('data2') as f:
    reviews = f.readlines()

nReviews = len(reviews)
support = nReviews/100

print support

with open('out') as f:
    features = f.readlines()
features = [ftr.rstrip('\n').strip('.').replace(',','') for ftr in features]
feature = {}

for ftr in features:
	if ftr not in feature:
		feature[ftr] = 0
	feature[ftr] = feature[ftr] + 1

fp = open("FreqFeatures.txt",'w')

for ftr in feature:
	if feature[ftr] >= support:
		fp.write(ftr+' '+str(feature[ftr])+'\n')