from setup import Setup
class Candle:
    def __init__(self):
        self.high = 0
        self.low = 0
        self.open = 0
        self.close = 0
        self.bull= False
        self.fullData = {}
        self.setup = Setup()
        self.setup.run()
        self.refresh()

    def refresh(self):
        self.fullData = self.setup.getdata()
        data = self.fullData['candlePoints']
        self.high = data['high']
        self.low = data['low']
        self.open = data['open']
        self.close = data['close']

        if(self.open < self.close):
            self.bull = True
        else:
            self.bull = False
            
