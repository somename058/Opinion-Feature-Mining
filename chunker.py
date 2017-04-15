import nltk

def prepareForNLP(text):
	sentences = nltk.sent_tokenize(text)
	sentences = [nltk.word_tokenize(sent) for sent in sentences]
	sentences = [nltk.pos_tag(sent) for sent in sentences]
	return sentences

def chunk(sentence):
	chunkToExtract = """
	NP:	{<NNP>*}
		{<NN>?<DT>?<JJ>?<NNS>}
		{<NN><NN>}
		{<JJ><NN>?}
		{<NN><IN><NN>}
		{<NN>}"""
	parser = nltk.RegexpParser(chunkToExtract)
	result = parser.parse(sentence)
	for subtree in result.subtrees():
		if subtree.label() == 'NP':
			t = subtree
			t = ' '.join(word for word, pos in t.leaves())
			print(t)

sentences = []
with open('redundant.txt') as f:
    reviews = f.readlines()
reviews = [line.rstrip('\n').split('|')[0].strip('.').replace(',','') for line in reviews]
#print len(reviews)
for review in reviews:
	sentences.extend(prepareForNLP(review))
for sentence in sentences:
	#print sentence
	chunk(sentence)