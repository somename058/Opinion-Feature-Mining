with open('redundant.txt') as f:
    reviews = f.readlines()
reviews = [review.rstrip('\n').strip('.').replace(',','') for review in reviews]

with open('redunftr.txt') as f:
    features = f.readlines()
features = [ftr.rstrip('\n').strip('.').replace(',','') for ftr in features]

getCount = {}
for ftur in features:
	ftrs = ftur.split()
	for ftr in ftrs:
		if ftr not in getCount:
			getCount[ftr] = 0
		getCount[ftr] = getCount[ftr] + 1
fp = open("redPruning.txt",'w')

for ftr in getCount:
	print ftr, getCount[ftr]

m = 3

output = []

s = set(features)

for ftr in s:
	ftrs = ftr.split()
	if len(ftrs) == 1:
		print ftr+"feature"
		for review in reviews:
			print review
			revL = review.split()
			if ftrs[0] in revL:
				ind = revL.index(ftrs[0])
				print ind
				if ind - 1 > 0:
					for ftre in s:
						if ftre != ftr and ftre not in output and revL[ind-1]+' '+revL[ind] in ftre:
							print ftre+ "dfsd"
							getCount[ftrs[0]] = getCount[ftrs[0]] - 1
				if ind+1 < len(revL):
					for ftre in s:
						if revL[ind]+' '+revL[ind+1] in ftre:
							print ftre+ "sdsdfsd"
							getCount[ftrs[0]] = getCount[ftrs[0]] - 1
						print revL[ind]+' '+revL[ind+1],ftre,ftr,getCount[ftrs[0]]
		print getCount[ftrs[0]]
		if getCount[ftrs[0]] >= m:
			output.append(ftr)
	else:
		output.append(ftr)
for ftr in output:
	fp.write(ftr+'\n')
