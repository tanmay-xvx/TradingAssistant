import numpy as np
import pandas as pd
import yfinance as yf

def findpivot():
    ticker = yf.Ticker("^NSEI")
    df = ticker.history(interval="1d")
    last_day = df.tail(2).iloc[0].copy()
    pivots = {}
    #calculation
    pivots['Pivot'] = (last_day['High'] + last_day['Low'] + last_day['Close'])/3
    pivots['R1'] = 2*pivots['Pivot'] - last_day['Low']
    pivots['S1'] = 2*pivots['Pivot'] - last_day['High']
    pivots['R2'] = pivots['Pivot'] + (last_day['High'] - last_day['Low'])
    pivots['S2'] = pivots['Pivot'] - (last_day['High'] - last_day['Low'])
    pivots['R3'] = pivots['Pivot'] + 2*(last_day['High'] - last_day['Low'])
    pivots['S3'] = pivots['Pivot'] - 2*(last_day['High'] - last_day['Low'])
    for p in pivots:
        pivots[p] = float(pivots[p])
    
    return pivots
