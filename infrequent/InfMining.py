import nltk
with open('infrequent') as f:
    reviews = f.readlines()
reviews = [review.rstrip('\n').split('|')[0].strip('.').replace(',','') for review in reviews]

with open('adj.txt') as f:
    adjectives = f.readlines()
adjectives = [adj.rstrip('\n').strip('.').replace(',','') for adj in adjectives]

reviewTagT = [];reviewWords = [];reviewTags = []

for line in reviews:
	reviewTagT.extend(nltk.pos_tag(line.split()))
	tempWord = []
	tempTag = []
	for line in reviewTagT:
		#print line
		tempWord.append(line[0])
		tempTag.append(line[1])
	reviewWords.append(tempWord)
	reviewTags.append(tempTag)

inFrequent = []

for adj in adjectives:
	ind = 0
	for review in reviews:
		#print review
		if adj in review:
			revL = review.split()
			#print revL
			try: 
				indx = revL.index(adj)
			except:
				continue
			#print indx,adj
			for i in range(indx,0,-1):
				#print ind,i
				if reviewTags[ind][i] == "NN":
					get = reviewWords[ind][i];
					if get not in inFrequent:
						inFrequent.append(get)
			for i in range(indx,len(revL)):
				if reviewTags[ind][i] == "NN":
					get = reviewWords[ind][i];
					if get not in inFrequent:
						inFrequent.append(get)
		ind = ind + 1
		'''if "NN" in reviewTags[0:ind-1]:
			get = reviewWords[reviewTags[0:ind-1].index("NN")];
			if get not in inFrequent:
				inFrequent.append(get)
		if "NN" in reviewTags[ind:len(revL)]:
			get = reviewWords[reviewTags[ind:len(revL)].index("NN")];
			if get not in inFrequent:
				inFrequent.append(get)'''
print inFrequent

#for item in inFrequent:
	#print item