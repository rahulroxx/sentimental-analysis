import math

import networkx as nx
import numpy as np

from nltk.tokenize.punkt import PunktSentenceTokenizer
from sklearn.feature_extraction.text import TfidfTransformer, CountVectorizer
import requests
import json

def textrank(document):
    sentence_tokenizer = PunktSentenceTokenizer()
    sentences = sentence_tokenizer.tokenize(document)

    bow_matrix = CountVectorizer().fit_transform(sentences)
    normalized = TfidfTransformer().fit_transform(bow_matrix)

    similarity_graph = normalized * normalized.T

    nx_graph = nx.from_scipy_sparse_matrix(similarity_graph)
    scores = nx.pagerank(nx_graph)
    sentence_array = sorted(((scores[i], s) for i, s in enumerate(sentences)), reverse=True)
    
    sentence_array = np.asarray(sentence_array)
    
    fmax = float(sentence_array[0][0])
    fmin = float(sentence_array[len(sentence_array) - 1][0])
    
    temp_array = []
    # Normalization
    for i in range(0, len(sentence_array)):
        if fmax - fmin == 0:
        	temp_array.append(0)
        else:
        	temp_array.append((float(sentence_array[i][0]) - fmin) / (fmax - fmin))


    threshold = (sum(temp_array) / len(temp_array)) + 0.2
    
    sentence_list = []

    for i in range(0, len(temp_array)):
        if temp_array[i] > threshold:
            sentence_list.append(sentence_array[i][1])

    seq_list = []
    for sentence in sentences:
    	if sentence in sentence_list:
    		seq_list.append(sentence)
    
    return seq_list


def summarize():
    # para = "I want to suggest a good way to be fit and this might not be the only one but Yeah It's possible to do so. It kind of amazing whey people like you are really stupid about the subject. that is not a problem but it is a matter of concern > People grow UP!!!"
    para = "BB u r I have watched all ur videos...literally all... all are awesome... wishing that you will be most viewed artist on YouTube n most liked in FB... my DP status n everything features U... ur timing is just amazing...kha se late ho itne sare ideas"
    # payload = {'apikey': 'a429a338-07a1-4b6e-bd46-c75b1fab8c89', 'text': para}
    payload = {'apikey': 'a429a338-07a1-4b6e-bd46-c75b1fab8c89', 'url': 'https://www.youtube.com/watch?v=OkP8BAwfO24'}

    # r = requests.get('http://api.idolondemand.com/1/api/sync/extractconcepts/v1', params=payload)
    r = requests.get('https://api.havenondemand.com/1/api/sync/analyzesentiment/v1', params=payload)
    json_r = json.loads(r.text)
    print json_r

print summarize()

