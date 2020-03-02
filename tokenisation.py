import nltk
nltk.download('stopwords')
from nltk.corpus import words
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
stopwords.words('english')
example_sent = "hii how are you?"
stop_w = set(stopwords.words('english'))
import re
my_text = input("Enter your text here: ")
print(my_text)
my_token = my_text.split(" ")
flag1 = 0
flag2 = 0
flag3 = 0
print(my_token)
my_list = []
for i in range(0, len(my_token)):
	if my_token[i].find('!') != -1:
		my_list.append(my_token[i].split("!"))
		if flag1 == 0:
			my_list.append("!")
			flag1 = 1
	elif my_token[i].find('?') != -1:
		if flag2 == 0:
			my_list.append("?")
			flag2 = 1
		my_list.append(my_token[i].split("?"))
	elif my_token[i].find('.') != -1:
		if flag3 == 0:
			my_list.append(".")
			flag3 = 1
		my_list.append(my_token[i].split("."))
	else:
		my_list.append(my_token[i])
print(my_list)
new_list = []
actual_list =[]
for i in my_list:
	for j in i:
		new_list.append(j)
print(new_list)
for i in range (0, len(new_list)):
	if new_list[i] in stop_w:
		actual_list.append(new_list[i])
print (actual_list)


