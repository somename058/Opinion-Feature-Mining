import nltk
with open('data2') as f:
    reviews = f.readlines()
reviews = [review.rstrip('\n').strip('.').replace(',','') for review in reviews]

with open('FreqFeatures.txt') as f:
    features = f.readlines()
features = [ftr.rstrip('\n').strip('.').replace(',','') for ftr in features]

reviews = [line.rstrip('\n').split('|')[0].strip('.').replace(',','') for line in reviews]
reviewTagT = []; reviewTag = []

reviewWords = []
reviewTags = []

for line in reviews:
	reviewTagT.extend(nltk.pos_tag(line.split()))
	tempWord = []
	tempTag = []
	for line in reviewTagT:
		tempWord.append(line[0])
		tempTag.append(line[1])
	reviewWords.append(tempWord)
	reviewTags.append(tempTag)
#print reviewWords[0]
#print reviewTags[0]

adjectives = []

for ftr in features:
	ind = 0
	#print ftr
	for review in reviews:
		if ' '+ftr+' ' in review:
			fromInd = reviewWords[ind].index(ftr.split()[0])
			for j in range(fromInd,0,-1):
				if reviewTags[ind][j] == "JJ":
					if reviewWords[ind][j] not in adjectives:
						adjectives.append(reviewWords[ind][j])
						print reviewWords[ind][j]
					break
		ind  = ind +1

#print adjectives