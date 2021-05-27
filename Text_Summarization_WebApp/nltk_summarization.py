import nltk
from nltk.corpus import stopwords
from string import punctuation
from nltk.tokenize import word_tokenize, sent_tokenize
import heapq  

def nltk_summarizer(raw_text):
	stopWords = set(stopwords.words("english"))
	punc = punctuation + '\n'
	word_frequencies = {}  
	for word in nltk.word_tokenize(raw_text):  
		if word not in stopWords:
			if word.lower() not in punc:
				if word not in word_frequencies.keys():
					word_frequencies[word] = 1
				else:
					word_frequencies[word] += 1

	maximum_frequncy = max(word_frequencies.values())

	for word in word_frequencies.keys():  
	    word_frequencies[word] = (word_frequencies[word]/maximum_frequncy)

	sentence_list = nltk.sent_tokenize(raw_text)
	sentence_scores = {}  
	for sent in sentence_list:  
	    for word in nltk.word_tokenize(sent.lower()):
	        if word in word_frequencies.keys():
	            if len(sent.split(' ')) < 30:
	                if sent not in sentence_scores.keys():
	                    sentence_scores[sent] = word_frequencies[word]
	                else:
	                    sentence_scores[sent] += word_frequencies[word]



	summary_sentences = heapq.nlargest(7, sentence_scores, key=sentence_scores.get)

	summary = ' '.join(summary_sentences)  
	return summary


if __name__ == "__main__":
	text= '''
Anime's so broad-reaching in its subject matter, it's possible to find anime aimed at just about every age group. Some titles are specifically for younger viewers or are suitable for all ages like the animated series "Pokémon" or Studio Ghibli film "My Neighbor Totoro" while others are aimed at teenage audiences and older like "InuYasha." There are even some animes aimed at older teens like "Death Note" and some for mature audiences only like "Monster" and "Queens Blade." 

Japanese cultural attitudes about sexuality and violence require some titles to be placed a category higher than they might normally be. Nudity, for instance, is handled much more casually in Japan; sometimes a show that isn't meant specifically for adults will have material which may seem racy to Western viewers.

Anime distributors are generally quite conscious of these issues and will include either an actual MPAA rating (G, PG, PG-13, R, NC-17) or a TV Parental Guidelines rating as an indicator of what the intended audience is for the show. Check the show's packaging or program listing to see which rating applies.

Confused about where to start? We recommend checking out the sci-fi, cyberpunk "Cowboy Bebop" or a swords-and-sorcery tale called "Berserk." If you already know a friend who's an anime fan, clue them in on what you like to watch — they should be able to guide you towards what's best and what's new in that category.
	'''
	print(nltk_summarizer(text))