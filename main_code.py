from datetime import datetime, timedelta
import time
import pandas as pd
import numpy as np
from datetime import datetime
from scipy.optimize import linprog


def TS(df):
    r_cap = 0.01
    sum = 0

    for index, row in df.iterrows():
        sum += (row['e'] * (row['h'] - r_cap))

    return sum


def form_matrices(df):

    borrowers = list(df.a.unique())
    borrowers.sort()
    lenders = list(df.b.unique())
    lenders.sort()


    a = []
    b = []

    # borrower constraints
    for each_b in borrowers:
        xf = df.loc[df['a'] == each_b] # all lenders who contributed to borrower's listing amount

        # b matrix value
        tot_amt = sum(xf.e)
        b.append(tot_amt)

        # a matrix row
        i = [0] * (len(borrowers) * len(lenders))

        # borrower constraints
        for x in xf.b: # lender
            i[lenders.index(x) * len(borrowers) + (borrowers.index(each_b) + 1)] = 1

        a.append(i)

    # lender constraints
    for each_l in lenders:
        xf = df.loc[df['b'] == each_l]  # all borrowers corresponding to the lender

        # b matrix value
        tot_amt = sum(xf.e)
        b.append(tot_amt)

        # a matrix row
        i = [0] * (len(borrowers) * len(lenders))

        # lender constraints
        for x in xf.a: # borrower
            i[lenders.index(each_l) * len(borrowers) + (borrowers.index(x) + 1)] = 1

        a.append(i)

    return a, b



def get_maximization_vector(df):
    borrowers = list(df.a.unique())
    borrowers.sort()
    lenders = list(df.b.unique())
    lenders.sort()
    r_cap = 0.01

    v = [0] * (len(borrowers) * len(lenders))

    for i in range(df.shape[0]):
        xf = df.iloc[i]
        v[lenders.index(xf.b) * len(borrowers) + (borrowers.index(xf.a) + 1)] = (xf.h - r_cap)

    return v


def linear_programming(c, A, b):
    c = [-i for i in c]
    bounds = [(0, None)] * len(c)
    # res = linprog(c, A_ub=A, b_ub=b, bounds=(bounds), options={"disp": True})

    options = {"disp": True, "maxiter": 15000}
    # res = linprog(c, A_ub=A1, b_ub=b, bounds=(None, None), options=options)
    res = linprog(c, A_ub=A, b_ub=b, bounds=(bounds), options={"disp": True, "maxiter": 5000})

    print("TSM - ",abs(res.fun))

def get_time(sec):
    t=int(sec)
    day= t//86400
    hour= (t-(day*86400))//3600
    minit= (t - ((day*86400) + (hour*3600)))//60
    seconds= t - ((day*86400) + (hour*3600) + (minit*60))
    print( day, 'days' , hour,' hours', minit, 'minutes',seconds,' seconds')



start_time = time.time()
df = pd.read_csv("sorted_prosper_data.txt", header=None, delim_whitespace=True)
df = df.iloc[:100]
df.columns = ['a','b','c','d','e','f','g','h','i']
print("shape - ", df.shape)
print("total value - ", sum(df.e))
print("avg rate -", np.mean(df.g))
print("borrowers/lenders - ",len(df.a.unique()), len(df.b.unique()))

v = get_maximization_vector(df)
A, b = form_matrices(df)
print("vector/matrices formed")
TS_val = TS(df)
print("inside linear programming")
print("length of v - ", len(v))
print("no.of constraints - ",len(b))
print("A size - ",len(A),len(A[0]))
print("b size - ",len(b))
print("TS - ",TS_val)
linear_programming(v, A, b)
get_time(int(time.time() - start_time))