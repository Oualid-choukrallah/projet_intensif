import pandas as pd

def to_date_time(a) :
    a = pd.to_datetime(a)
    a = pd.to_datetime(a.dt.strftime('%Y/%m/%d'))
    return a

