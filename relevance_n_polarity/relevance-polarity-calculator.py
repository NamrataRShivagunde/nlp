import spacy
import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nlp= spacy.load('en_core_web_lg')

import pandas as pd
data = pd.read_excel(r'.\input-conversation.xlsx') #for an earlier version of Excel, you may need to use the file extension of 'xls'
df = pd.DataFrame(data, columns= ['Information till this stage and task','User', 'Message'])
#print (df)
n=(df.shape[0])
#print(n)
#calcultaing two columns
similarity = []
sentiments = []
compound_polarity = []
i=0

for i in range(n):
    info = df['Information till this stage and task'].values[i]
    conv = df['Message'].values[i]
    print("nammu",info)
    print("nammu",conv)
    print(type(info))
    information_stages_tasks= nlp(info)
    conversation = nlp(conv)
    print(information_stages_tasks)
    print(type(information_stages_tasks))
    print(conversation)
    print(type(conversation))

    #tokenization creates a list of words in string format
    info_token = [word for word in information_stages_tasks]
    conv_token = [word for word in conversation]
    print(info_token)
    print(len(info_token))
    print(type(info_token))

    #removing stop words and punctuation
    info_cleaned = [ token for token in info_token if not token.is_punct | token.is_space | token.is_stop]
    conv_cleaned = [token for token in conv_token if not token.is_punct | token.is_space | token.is_stop]
    print(info_cleaned)
    print(len(info_cleaned))
    print(type(info_cleaned))

    #lemmatization
    info_s_t_lemma = [word.lemma_ for word in info_cleaned]
    conv_lemma = [word.lemma_ for word in conv_cleaned]
    print(info_s_t_lemma)
    print(len(info_s_t_lemma))
    print(type(info_s_t_lemma))

    info_final = [nlp(word) for word in info_s_t_lemma]
    conv_final = [nlp(word) for word in conv_lemma]
    print(info_final)
    print(conv_final)
    
    totallenght = len(info_cleaned)+len(conv_cleaned)

    #calculating similarity score of info and conversation
    #output 
    i=1
    similarity_score = 0
    for token in info_final:
        for token2 in conv_final:
            #print(token.text, token2.text, token.similarity(token2))
            i=i+1
            similarity_score =token.similarity(token2)+similarity_score
            print(i)
            print(similarity_score)
    score= similarity_score/totallenght
    similarity.append(score)
    

    #sentiments
    sid = SentimentIntensityAnalyzer()
    polarity = sid.polarity_scores(conv)
    sentiments.append(polarity)
    m=0
    for key, values in polarity.items():
        if key =='compound':
            compound_polarity.append(values)

    #first for loop i 
    i=i+1

print(similarity)
print(sentiments)
print(len(similarity))
print(len(sentiments))

df['similarity score of conv to info'] = similarity
df['polarity of conv'] = sentiments
df['compound_polarity'] = compound_polarity

df.to_excel(r'.\relevance-polarity-output.xlsx')