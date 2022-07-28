import pandas as pd
import stylecloud
import functions as f
import nltk
from nltk.corpus import stopwords


#Data cleaning
df = pd.read_csv("assets/reviews.csv", skiprows =1)
df = df.dropna(axis=1, thresh=(len(df)*16/100))
df['Creation date'] = f.to_date_time(df['Creation date'])
df['Response date'] = f.to_date_time(df['Response date'])
print(df.head())
df['Creation date']= pd.to_datetime(df['Creation date'])
df['Creation date']= pd.to_datetime(df['Creation date'].dt.strftime('%Y/%m/%d'))
df['Response date']= pd.to_datetime(df['Response date'])
df['Response date']= pd.to_datetime(df['Response date'].dt.strftime('%Y/%m/%d'))


l = []
lst = []
for i in range (len(df)) :
    l.append(df["Content"][i])


with open('listfile.txt', 'w') as filehandle:
   for listitem in l:
      filehandle.write('%s\n' % listitem)


f = open('listfile.txt','r')
for line in f:
    for word in stop_words:
        if word in line:
            line = line.replace(word,'')
    lst.append(line)
f.close()
f = open('./test.txt','w')
for line in lst:
    f.write(line)
f.close()

stylecloud.gen_stylecloud(file_path='listfile.txt',
                          icon_name= "fas fa-book-reader")