#!/usr/bin/env python
# coding: utf-8

# In[236]:


import pandas as pd
import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from collections import Counter

#Below are the file names and their specified locations
filenames = ["Downloads/web_scraper.csv","Downloads/output.csv","Downloads/requests.csv","Downloads/extracted.csv","Downloads/companies.csv"]
#Below the files are located and then read one by one
df_merged = pd.concat((pd.read_csv(f, sep=',') for f in filenames), ignore_index=True)

#Below the sentiment analyzer function is shortened and a results matrix is established
sid = SentimentIntensityAnalyzer()
results = []
#The company purposes are analyzed one by one for their polarity scores and added to the matrix
for i in df_merged['Purpose']:
    analyzed = sid.polarity_scores(i)
    results.append(analyzed)
#The resulting purpose matrix is converted to a data frame and indexed according to name and compound score
df = pd.concat([df_merged[['Name']],pd.DataFrame(results)],axis=1).set_index('Name')[['compound']]
#The min and max scores are found
max = df[df['compound']==df['compound'].max()]
min = df[df['compound']==df['compound'].min()]
#The min and max are combined as poles
poles = [min,max]

#To find the most common words, the company purposes need to be added together
list = []
for l in df_merged['Purpose']:
    list.append(l)
#The resulting matrix of company purposes need to be converted to a data frame and the words need to be split up before each word can be counted for its frequency
most_common_words = Counter((pd.DataFrame(list))[0].str.cat(sep = ' ').split()).most_common()[0:10]


def main():
    return poles, most_common_words

if __name__ == '__main__':
    main()



# In[ ]:




