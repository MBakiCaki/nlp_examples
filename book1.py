# text data analysis example with nltk.Text module
# MBakiCaki - 20.10.2022
import nltk
# nltk.download('punkt')
# nltk.download('stopwords')

f = open(***PATH***, encoding = "ISO-8859-1") #txt file
raw = f.read()
FindwordsText = nltk.word_tokenize(raw)
text = nltk.Text(FindwordsText)
freq = nltk.FreqDist(text)

a = len(text)
b = freq.most_common(10) #lists all words if not specified
c = text.count('sky')

print(f'Total length: {a}')
print(f'Most common words: {b}')
print(f'word "sky" count: {c}')