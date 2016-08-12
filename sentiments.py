import math
import re
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# AFINN-111 is as of June 2011 the most recent version of AFINN
filenameAFINN = 'datasets/AFINN-111.txt'
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
    print sentiments
    if sentiments:
        # How should you weight the individual word sentiments? 
        # You could do N, sqrt(N) or 1 for example. Here I use sqrt(N)
        sentiment = float(sum(sentiments))/math.sqrt(len(sentiments))
        
    else:
        sentiment = 0
    return sentiment



if __name__ == '__main__':
    # Single sentence example:
    # text = "Finn is stupid and idiotic"
    # print("%6.2f %s" % (sentiment(text), text))
    
    # No negation and booster words handled in this approach
    # text = "Finn is only a tiny bit stupid and not idiotic. What I think about is good actually is really sarcastic"
    # print("%6.2f %s" % (sentiment(text), text))

    # Test 
    # text = "Finn is only a tiny bit stupid and not idiotic. What I think about is good actually is really sarcastic"
    text = "I want to suggest a good way to be fit and this might not be the only one but Yeah It's possible to do so. It kind of amazing whey people like you are really stupid about the subject. that is not a problem but it is a matter of concern > People grow UP!!!"
    print("%6.2f %s" % (sentiment(text), text))