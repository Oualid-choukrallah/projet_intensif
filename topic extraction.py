from gensim.models import LdaModel
import pyLDAvis.gensim_models
import warnings



pyLDAvis.gensim_models.prepare(model, corpus, dictionary, sort_topics=False)
model = LdaModel(corpus=corpus, id2word=dictionary, num_topics=14, chunksize=1000, passes=5, random_state=1)

sujet = [doc for doc in df.docs]

coherence_model_lda = CoherenceModel(model= model, texts = sujet, dictionary = dictionary)
coherence_lda = coherence_model_lda.get_coherence()

data_dict = {'dominant_topic':[]} #, 'perc_contribution':[], 'topic_keywords':[]

for i, row in enumerate(model[corpus]):
    #print(i)
    row = sorted(row, key=lambda x: x[1], reverse=True)
    #print(row)
    for j, (topic_num, prop_topic) in enumerate(row):
        wp = model.show_topic(topic_num)
        topic_keywords = ", ".join([word for word, prop in wp])
        data_dict['dominant_topic'].append(int(topic_num))
        break

dfa_topics = pd.DataFrame(data_dict)

pd.set_option("max_colwidth", None)
pd.set_option('display.min_rows', 1000)
pd.set_option('display.max_rows', 1000)
data = df.copy()
data['Topic_Lda'] = data_dict['dominant_topic']
new_data = data#[["Content", "Topic_Lda"]]