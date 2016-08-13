import math
import re
import sys
import operator
reload(sys)
sys.setdefaultencoding('utf-8')

# AFINN-111 is as of June 2011 the most recent version of AFINN
filenameAFINN = '../datasets/AFINN-111.txt'
afinn = dict(map(lambda (w, s): (w, int(s)), [ 
            ws.strip().split('\t') for ws in open(filenameAFINN) ]))

# Word splitter pattern
pattern_split = re.compile(r"\W+")

def sentiment(text):
    """
    Returns a float for sentiment strength based on the input text.
    Positive values are positive valence, negative value are negative valence. 
    """
    words = pattern_split.split(text.lower())
    sentiments = map(lambda word: afinn.get(word, 0), words)
    if sentiments:
        # How should you weight the individual word sentiments? 
        # You could do N, sqrt(N) or 1 for example. Here I use sqrt(N)
        sentiment = float(sum(sentiments))/math.sqrt(len(sentiments))
        
    else:
        sentiment = 0
    return sentiment



if __name__ == '__main__':
    positive_comments = []
    nuetral_comments = []
    negative_comments = []
    posts_list_scores = []
    score_dict_update = {}
    # Single sentence example:
    texts_list  = ["Finn is stupid and idiotic", "That audio is really innovative, I want to purchase it", "I hate those people who are not in favour of obama", "I like those shoes and black dress is awesome!!!"]
    for text in texts_list:
        posts_list_scores.append(sentiment(text))
        # posts_list.append(score_dict)
    # print posts_list
    scores_zipped = zip(texts_list, posts_list_scores)
    for x in scores_zipped:
        if x[1] > 0:
            positive_comments.append(x)
        elif x[1] == 0:
            nuetral_comments.append(x)
        else:
            negative_comments.append(x)

    print("Positive comments", positive_comments)
    print("Negative comments", negative_comments)
