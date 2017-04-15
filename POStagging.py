import nltk
with open('data2') as f:
    reviews = f.readlines()
reviews = [line.rstrip('\n').split('|')[0].strip('.').replace(',','') for line in reviews]
reviewTagT = []; reviewTag = []
for line in reviews:
	reviewTagT.extend(nltk.pos_tag(line.split()))
for line in reviewTagT:
	#if line[1] == "NN" or line[1] == "NG":
	reviewTag.extend(line)
for line in reviewTag:
	print line
print len(reviewTag)