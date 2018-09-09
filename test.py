from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# sentence = "who is teaching it010806"


while True:
	sentence = raw_input("enter the sentence >>")
	
	# setting the english stop words
	stop_words = set(stopwords.words('english'))
	
	# separating each word from the input
	word_tokens = word_tokenize(sentence)
	
	# print word_tokens

	filtered_sentence = []
	
	# removing all the stop words from the input
	for w in word_tokens:
		if w not in stop_words:
			filtered_sentence.append(w)

	print(filtered_sentence)