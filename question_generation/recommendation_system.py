import nltk

text_file = open('input_business_problem.txt','r')
business_problem = text_file.read()
sentence_list = nltk.sent_tokenize(business_problem)

stopwords = nltk.corpus.stopwords.words('english')
business_problem_tokenize = nltk.word_tokenize(business_problem)
business_problem_filtered = [word for word in business_problem_tokenize if word.isalpha()]
word_frequencies = {}
for word in business_problem_filtered:
        if word not in stopwords:
            if word not in word_frequencies.keys():
                word_frequencies[word] = 1
            else:
                word_frequencies[word] += 1

#print("word freq", word_frequencies)
maximum_frequency = max(word_frequencies.values())

for word in word_frequencies.keys():
    word_frequencies[word] = (word_frequencies[word]/maximum_frequency)

sentence_scores = {}
for sent in sentence_list:
    for word in nltk.word_tokenize(sent.lower()):
        if word in word_frequencies.keys():
            if len(sent.split(' ')) < 30:
                if sent not in sentence_scores.keys():
                    sentence_scores[sent] = word_frequencies[word]
                else:
                    sentence_scores[sent] += word_frequencies[word]
#print(sentence_scores)

import heapq
summary_sentences = heapq.nlargest(1, sentence_scores, key=sentence_scores.get)
top8words = heapq.nlargest(8, word_frequencies, key=word_frequencies.get)
summary = ' '.join(summary_sentences)
summary_tokenize= nltk.word_tokenize(summary)
print("IMPORTANT SENTENCES :  " , summary)
print("IMPORTANT WORDS : ", top8words)

#print(nltk.pos_tag(summary_tokenize))
sent_part = []
sent = []
for word in top8words:
    if word in summary_tokenize:
        i = summary_tokenize.index(word)
        sent_part = summary_tokenize[i-6:i+6]
        sent_part = ' '.join(sent_part)
        sent.append(sent_part)
        
print("IMPORTANT PHRASES : ",sent)



with open('output_recommendation_system.txt','w') as output_file:
    output_file.write("IMPORTANT SENTENCES")
    output_file.write("\n")
    output_file.write( ','.join(summary_sentences) )
    output_file.write("\n")
    output_file.write("\n")

    output_file.write("IMPORTANT WORDS")
    output_file.write("\n")
    output_file.write( ','.join(top8words) )
    output_file.write("\n")
    output_file.write("\n")

    output_file.write("IMPORTANT PHRASES")
    output_file.write("\n")
    output_file.write( ','.join(sent) )
    output_file.write("\n")
