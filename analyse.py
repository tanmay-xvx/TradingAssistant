from datetime import datetime
from candle import Candle
from trade import Trade
from pivots import findpivot


def analyse():
    candle = Candle()
    trade = Trade()
    data = candle.fullData
    pivots = findpivot()
    # print(data)
    marketClose = datetime.strptime("14:30","%H:%M").time()
    break_loop = False
    while(datetime.datetime.now().time() < marketClose and not break_loop):
        if(candle.bull):
            if((data['refPoints']['alligatorJaw'] < candle.open) and (data['refPoints']['superTrendGreen'] < candle.close)):
                for p in pivots:
                    if((pivots[p] > candle.open) and  (pivots[p] <= candle.close)):
                        trade.buy(candle.high,candle.low)
                        break_loop = True
                        break
            
            else:
                print("No trade")
        
        else:
            if((data['refPoints']['alligatorJaw'] > candle.open) and (data['refPoints']['superTrendRed'] > candle.close)):
                for p in pivots:
                    if((pivots[p] < candle.open) and  (pivots[p] >= candle.close)):
                        trade.short(candle.low, candle.high)
                        break_loop = True
                        break
            
            else:
                print("No trade")
        candle.refresh()

if __name__== "__main__":
    analyse()

    