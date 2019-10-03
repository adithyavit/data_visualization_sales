import pandas as pd
import math
from textblob import TextBlob
import numpy as np

dfs = pd.read_excel("/Users/adithya/Documents/dataVizProject/review_brands_excel.xlsx", sheetname="Sheet1")
k = dfs.loc[[0]]
q = k["Reviews - Split 7 - Split 1"]
sentiment = []
sentiment2 = []; sentiment3 = [];sentiment4 = [];sentiment5 = [];sentiment6 = []; sentiment7 = []

for i in dfs["Reviews - Split 3 - Split 1"]:
    sentiment_each = TextBlob(i).sentiment.polarity
    sentiment.append(sentiment_each) count2 = 0
for i in dfs["Reviews - Split 4 - Split 1"]:
    if(type(i)!=str): if(math.isnan(i)==True):
        sentiment_each2 = sentiment[count2]
    else:
        sentiment_each2 = TextBlob(i).sentiment.polarity
        sentiment2.append(sentiment_each2)
        count2 += 1
        count3 = 0
for i in dfs["Reviews - Split 5 - Split 1"]:
    if(type(i)!=str): if(math.isnan(i)==True):
        sentiment_each3 = (sentiment[count3]+sentiment2[count3])/2
    else:
        sentiment_each3 = TextBlob(i).sentiment.polarity
        sentiment3.append(sentiment_each3)
        count3 += 1
        count4 = 0
for i in dfs["Reviews - Split 6 - Split 1"]:
    if(type(i)!=str): if(math.isnan(i)==True):
        sentiment_each4 = (sentiment[count4]+sentiment2[count4]+sentiment3[count4])/3
    else:
        sentiment_each4 = TextBlob(i).sentiment.polarity
        sentiment4.append(sentiment_each4)
        count4 += 1
        count5 = 0
for i in dfs["Reviews - Split 7 - Split 1"]:
    if(type(i)!=str): if(math.isnan(i)==True):
        (sentiment[count5]+sentiment2[count5]+sentiment3[count5]+sentiment4[count5])/4
    else:
        sentiment_each5 = TextBlob(i).sentiment.polarity
        sentiment5.append(sentiment_each5)
        count5 += 1
        count6 = 0
for i in dfs["Reviews - Split 8 - Split 1"]:
    if(type(i)!=str): if(math.isnan(i)==True):
        (sentiment[count6]+sentiment2[count6]+sentiment3[count6]+sentiment4[count6]+sentime nt5[count6])/5
    else:
        sentiment_each6 = TextBlob(i).sentiment.polarity
        sentiment6.append(sentiment_each6)
        count6 += 1
        count7 = 0
for i in dfs["Reviews - Split 9 - Split 1"]:
    if(type(i)!=str): if(math.isnan(i)==True):
        (sentiment[count7]+sentiment2[count7]+sentiment3[count7]+sentiment4[count7]+sentime nt5[count7]+sentiment6[count7])/6
    else:
        sentiment_each7 = TextBlob(i).sentiment.polarity
        sentiment7.append(sentiment_each7)
        count7 += 1
        sentiment_all = sentiment,sentiment2,sentiment3]
sentiment_all = np.vstack((sentiment,sentiment2))
newarray = dfs["Asins"]
newarray2 = dfs["Brand"] np.vstack((newarray,newarray2,sentiment,sentiment2,sentiment3,sentiment4,sentiment5,s entiment6,sentiment7))
newarray3 = newarray3.T
final_data = pd.DataFrame(newarray3, columns =
df = pd.DataFrame(final_data) df.to_csv("/Users/adithya/Documents/dataVizProject/exported_reviews.csv") ['Asins','Brand','rating1','rating2','rating3','rating4','rating5','rating6','rating7'])