import csv
import pickle
import re
from collections import Counter
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import config
import handle

word_dict = {}
word_list = []

#config to be ran the first time running the program
nltk.download('all')

def get_metrics(profile, text):
    output = {}
    
    #get words as dict
    words = re.findall(r'\w+', text.lower())

    #return count of words
    counts = Counter(words)

    #derive text NLTK
    for key,val in counts.items():
        word = nltk.word_tokenize(key)
        tagged = nltk.pos_tag(word)
        word_dict['word'] = tagged[0][0]
        word_dict['count'] = val
        word_dict['type'] = config.pos_lookup[tagged[0][1]]
        word_list.append(word_dict.copy())

    #process metrics
    for idx in config.profile_lookup[profile]:
        for chart in config.chart_types:
            if chart in idx:
                #print(idx[chart](word_list))
                if chart in output:
                    output[chart].append(idx[chart](word_list))
                else:
                    output[chart] = [idx[chart](word_list)]

    return (output)