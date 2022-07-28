from textblob import TextBlob
from textblob_fr import PatternTagger, PatternAnalyzer
import pandas as pd


list_analysis_content = []
list_analysis_response = []

data = pd.read_csv("assets/lundi_data.csv")
data['Content'] = data['Content'].fillna('unkown')
data['Response'] = data['Response'].fillna('unkown')
for i in range (0, len(data)):
    text = data["Content"][i]
    blob = TextBlob(text, pos_tagger=PatternTagger(), analyzer=PatternAnalyzer())
    list_analysis_content.append(blob.sentiment[0])

data.insert(2,"Sentiment_analysis_content",list_analysis_content,True)
data["Sentiment_rating_content"] = 10 - 10*((1 - data["Sentiment_analysis_content"])/2)

for i in range (0, len(data)):
    text = data["Response"][i]
    blob = TextBlob(text, pos_tagger=PatternTagger(), analyzer=PatternAnalyzer())
    list_analysis_response.append(blob.sentiment[0])

data.insert(3,"Sentiment_analysis_response",list_analysis_response,True)
data["Sentiment_rating_response"] = 10 - 10*((1 - data["Sentiment_analysis_response"])/2)

data["Rating"] = data["Rating"]*2
data["Rating"] =data["Rating"].fillna((data["Sentiment_rating_response"][i] + data["Sentiment_rating_content"][i])/2)

data["Prediciton_average"] = (data["Sentiment_rating_response"] + data["Sentiment_rating_content"] + 2*data["Rating"]) / 4

data["Rating"] = data["Rating"]//2
data = data.sort_values(by=["Prediciton_average"], ascending=False)
data.to_csv('final_results.csv', index=False)
print(data["Prediciton_average"].head())







