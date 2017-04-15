with open('test.txt') as f:
    reviews = f.readlines()
reviews = [review.rstrip('\n').strip('.').replace(',','') for review in reviews]

with open('tempout.txt') as f:
    features = f.readlines()
features = [ftr.rstrip('\n').strip('.').replace(',','') for ftr in features]

fp = open("afterCompact.txt",'w')

m = 2;
dist = 3

for ftr in features:
	print ftr + "-----"
	ftrs = ftr.split()
	support = 0
	if len(ftrs) > 1:
		for review in reviews:
			revL = review.split()
			temp = []
			flag = True;
			nCompact = False
			for word in ftrs:
				if word in revL:
					temp.append(revL.index(word))
				else:
					flag = False
					nCompact = True
					break;
			if flag:
				for i in range(1,len(temp)):
					if abs(temp[i] - temp[i-1]) > 3:
						print "yesss"
						nCompact = True
						break;
			if not nCompact:
				support = support + 1
	if support >= m:
		print support
		fp.write(ftr+'\n')