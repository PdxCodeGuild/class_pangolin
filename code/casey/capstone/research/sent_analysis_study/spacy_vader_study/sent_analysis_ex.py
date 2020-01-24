import spacy
import vaderSentiment.vaderSentiment as vader

analyzer = vader.SentimentIntensityAnalyzer()
english = spacy.load("en_core_web_sm")

def get_sentiments(text):
    result = english(text)
    sentences = [str(sent) for sent in result.sents]
    sentiments = [analyzer.polarity_scores(str(s)) for s in sentences]
    return sentiments

text = "I like this very much!"
sentiments = get_sentiments(text)

print(sentiments)