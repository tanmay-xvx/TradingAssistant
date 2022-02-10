from smartapi import SmartConnect

class Trade:
    def __init__(self):
        #create object of call
        self.obj=SmartConnect(api_key="your api key")
        #optional
        #access_token = "your access token",
        #refresh_token = "your refresh_token")

        #login api call

        self.data = self.obj.generateSession("Your Client ID","Your Password")
        self.refreshToken= self.data['data']['refreshToken']

        #fetch the feedtoken
        self.feedToken=self.obj.getfeedToken()


    def buy(self, price, low):
        stoploss = 200
        if(price - low > stoploss):
            stoploss = price - low
        stopLossPrice = price - stoploss
        target = price + 2*stoploss

        #Place Order
        try:
            orderparams = {
            "variety": "NORMAL",
            "tradingsymbol": "NIFTY", #Stock
            "symboltoken": "3045", # Token number
            "transactiontype": "BUY",
            "exchange": "NFO",
            "ordertype": "STOPLOSS_LIMIT",
            "producttype": "INTRADAY",
            "duration": "DAY",
            "price": price,
            "squareoff": target,
            "stoploss": stopLossPrice,
            "quantity": "1"
            }
            orderId=self.obj.placeOrder(orderparams)
            print("The order id is: {}".format(orderId))

        except Exception as e:
           print("Order placement failed: {}".format(e.message))

        print("Bought at: "+price +"Stoploss:" + stoploss +"Target:" + target)
    
    def short(self,price,high):
        stoploss = 200
        if(high - price > stoploss):
            stoploss = high - price
        stopLossPrice = price + stoploss
        target = price - 2*stoploss

        #Place Order 
        try:
            orderparams = {
            "variety": "NORMAL",
            "tradingsymbol": "NIFTY", #Stock
            "symboltoken": "3045", # Token number
            "transactiontype": "BUY",
            "exchange": "NFO",
            "ordertype": "STOPLOSS_LIMIT",
            "producttype": "INTRADAY",
            "duration": "DAY",
            "price": price,
            "squareoff": target,
            "stoploss": stopLossPrice,
            "quantity": "1"
            }
            orderId=self.obj.placeOrder(orderparams)
            print("The order id is: {}".format(orderId))

        except Exception as e:
           print("Order placement failed: {}".format(e.message))

        print("Shorted at: "+price +"Stoploss:" + stoploss +"Target:" + target)