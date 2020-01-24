# import the required libraries
import numpy as np 
import pandas as pd 
import re
import nltk 
import matplotlib.pyplot as plt

# import the dataset, use the Pandas read_csv function
data_source_url = "https://raw.githubusercontent.com/kolaveridi/kaggle-Twitter-US-Airline-Sentiment-/master/Tweets.csv"
airline_tweets = pd.read_csv(data_source_url)

# see how the dataset looks like using the head() method
airline_tweets.head()

