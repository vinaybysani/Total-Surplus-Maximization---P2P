import time
import pandas as pd
import numpy as np
from datetime import datetime
from scipy.optimize import linprog

'''
Preprocessing data
'''
def filter_dateset():
    df = pd.read_csv("out.prosper-loans",header=None, delim_whitespace=True)
    # df = pd.read_csv("small_prosper_loans.txt",header=None, delim_whitespace=True)
    # df = df.iloc[:10000]
    df.columns = ['a','b','c','d','e','f','g','h','i']


    s = "08/05/2009"
    date_filter = time.mktime(datetime.strptime(s, "%d/%m/%Y").timetuple())

    print(df.shape)

    filter_words = ['3', 'Cancelled', 'Defaulted', 'Charge-off', '1', 'Repurchased', '2', '4+']
    for i in filter_words:
        df = df[df.f != i]

    df = df[df.d < date_filter]
    df = df[df.g > 0]

    print("total value - ",sum(df.e))
    print("shape - ",df.shape)
    # print(min(df.g),max(df.g))
    # print(min(df.h),max(df.h))
    print("avg rate -",np.mean(df.g))

    # print(datetime.utcfromtimestamp(1132012800).strftime('%Y-%m-%d %H:%M:%S'), datetime.utcfromtimestamp(1317081600).strftime('%Y-%m-%d %H:%M:%S'))
    print("borrowers/lenders - ",len(df.a.unique()), len(df.b.unique()))

    return df

def export_df(df):
    # f = open('sorted_prosper_data.txt', 'w')
    # s = ""

    np.savetxt(r'sorted_prosper_data.txt', df.values, fmt='%s')

    # for i in v:
    #     s += (str(i) + " ")
    # f.write(s + "\n")
    # f.close()


df = filter_dateset()
df = df.sort_values('d')
# print(df.d)
export_df(df)