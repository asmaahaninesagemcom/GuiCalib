# -*- coding: utf-8 -*-
"""
Created on Fri Jul  1 19:05:01 2022

@author: G604088
"""

# In[]
import pandas as pd
import numpy as np
import math
import datetime as dt

import matplotlib.pyplot as plt
from itertools import cycle
# import plotly.graph_objects as go
# import plotly.express as px
# from plotly.subplots import make_subplots
# import seaborn as sns

from xgboost import XGBRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, explained_variance_score, r2_score
from sklearn.preprocessing import MinMaxScaler

init_notebook_mode(connected=True)

# In[]

data=pd.read_csv('../input/bitcoin-stock-data-sept-17-2014-august-24-2021/BTC-USD.csv')
data = data.rename(columns={'Date': 'date','Open':'open','High':'high','Low':'low','Close':'close',
                                'Adj Close':'adj_close','Volume':'volume'})
data['date'] = pd.to_datetime(data.date)

print("Starting date: ",data.iloc[0][0])
print("Ending date: ", data.iloc[-1][0])
print("Duration: ", data.iloc[-1][0]-data.iloc[0][0])

# In[]
y_2014 = data.loc[(data['date'] >= '2014-01-01')
                     & (data['date'] < '2015-01-01')]

y_2014.drop(y_2014[['adj_close','volume']],axis=1)

monthvise= y_2014.groupby(y_2014['date'].dt.strftime('%B'))[['open','close']].mean()
new_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
             'September', 'October', 'November', 'December']
monthvise = monthvise.reindex(new_order, axis=0)
monthvise

fig = go.Figure()

fig.add_trace(go.Bar(
    x=monthvise.index,
    y=monthvise['open'],
    name='Stock Open Price',
    marker_color='crimson'
))
fig.add_trace(go.Bar(
    x=monthvise.index,
    y=monthvise['close'],
    name='Stock Close Price',
    marker_color='lightsalmon'
))

fig.update_layout(barmode='group', xaxis_tickangle=-45,
                  title='Monthwise comparision between Stock open and close price')
fig.show()