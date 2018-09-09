import nltk

nltk.data.path.append('./nltk_data/')

from base import kernel
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.corpus import wordnet as wn


# Always use the IT instead of 'it' for indicating the subject code to avoid
# ambiguity.
# Used to remove any space between course code like for IT 010801 becomes IT010801
def course_code(sentence):
    try:
        words = re.compile('\w+').findall(sentence)
        new_sentence = ""
        # The enumerate() allows you to get the index value.
        for index,word in enumerate(words):
            if (word == "IT") and (index < len(words) -1) and (words[index+1].isdigit()):
                new_sentence = new_sentence + word
            else:
                new_sentence = new_sentence + word + " "
        return new_sentence
    except:
        return sentence

# sentence = "who is teaching IT 010806"
# print course_code(sentence)

# Removing the aiml recognized characters _ and *
def remove_aiml_char(sentence):
    try:
        new_sentence = sentence.replace("_","")
        new_sentence = new_sentence.replace("*","")
        return new_sentence
    except:
        return sentence

# sentence = "who is * _teaching IT010806"
# print remove_aiml_char(sentence)

dict = {'NN': 'NOUN', 'JJ': 'ADJ'}
dict['NNS'] = 'NOUN'
dict['NNP'] = 'NOUN'
dict['NNPS'] = 'NOUN'
dict['PRP'] = 'NOUN'
dict['PRP$'] = 'NOUN'
dict['RB'] = 'ADV'
dict['RBR'] = 'ADV'
dict['RBS'] = 'ADV'
dict['VB'] = 'VERB'
dict['VBD'] = 'VERB'
dict['VBG'] = 'VERB'
dict['VBN'] = 'VERB'
dict['VBP'] = 'VERB'
dict['VBZ'] = 'VERB'
dict['WRB'] = 'ADV'
	
def talk(message):

	sentence = message.lower()
	sentence = course_code(sentence)
	stop_words = set(stopwords.words('english'))

	word_tokens = word_tokenize(sentence)

	filtered_sentence = [w for w in word_tokens if not w in stop_words]
	# print filtered_sentence
	temp = nltk.pos_tag(filtered_sentence)
	new_sentence = ""
	for i in temp:
		try:
			z = i[1]
			if (dict[z] != None):
			    part_speech = dict[z]
			else:
			    part_speech = 'NOUN'

			if(part_speech == 'NOUN'):
			    word = wn.morphy(i[0],wn.NOUN)
			elif(part_speech == 'VERB'):
			    word = wn.morphy(i[0],wn.VERB)
			elif(part_speech == 'ADV'):
			    word = wn.morphy(i[0],wn.ADV)
			elif(part_speech == 'ADJ'):
			    word = wn.morphy(i[0],wn.ADJ)
			word1 = wn.synsets(word)[0].lemmas()[0].name()
		except:
			word1 = i[0]
		if new_sentence == "":
			new_sentence = new_sentence + word1.lower()
		else:
			new_sentence = new_sentence + " " + word1.lower()
	new_sentence = remove_aiml_char(new_sentence)
	# print new_sentence
	bot_response = kernel.respond(new_sentence)
	if bot_response != "" and bot_response[0] == '$':
		bot_response = bot_response[1:]
	return bot_response

def session_talk(message,sessionid):

	sentence = message.lower()
	sentence = course_code(sentence)
	stop_words = set(stopwords.words('english'))

	word_tokens = word_tokenize(sentence)

	filtered_sentence = [w for w in word_tokens if not w in stop_words]
	# print filtered_sentence
	temp = nltk.pos_tag(filtered_sentence)
	new_sentence = ""
	for i in temp:
		try:
			z = i[1]
			if (dict[z] != None):
			    part_speech = dict[z]
			else:
			    part_speech = 'NOUN'

			if(part_speech == 'NOUN'):
			    word = wn.morphy(i[0],wn.NOUN)
			elif(part_speech == 'VERB'):
			    word = wn.morphy(i[0],wn.VERB)
			elif(part_speech == 'ADV'):
			    word = wn.morphy(i[0],wn.ADV)
			elif(part_speech == 'ADJ'):
			    word = wn.morphy(i[0],wn.ADJ)
			word1 = wn.synsets(word)[0].lemmas()[0].name()
		except:
			word1 = i[0]
		if new_sentence == "":
			new_sentence = new_sentence + word1.lower()
		else:
			new_sentence = new_sentence + " " + word1.lower()
	new_sentence = remove_aiml_char(new_sentence)
	# print new_sentence
	
	bot_response = kernel.respond(new_sentence,sessionid)
	if bot_response != "" and bot_response[0] == '$':
		bot_response = bot_response[1:]
	return bot_response
