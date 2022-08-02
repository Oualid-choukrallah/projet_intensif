import pandas as pd

def to_date_time(a) :
    a = pd.to_datetime(a)
    a = pd.to_datetime(a.dt.strftime('%Y/%m/%d'))
    return a

def lda_topics(model, num_topics):
    word_dict = {};
    for i in range(num_topics):
        words = model.show_topic(i, topn = 20);
        word_dict['Topic # ' + '{:02d}'.format(i+1)] = [i[0] for i in words];
    return pd.DataFrame(word_dict);