class Stock:
    def __init__(self,symbol,name,previousClosingPrice,currentPrice):
        self.symbol= symbol
        self.name= name
        self.previousPrice= previousClosingPrice
        self.currentPrice= currentPrice

    def getname(self):
        self.name

    def getsymbol(self):
        return self.symbol

    def getpreviousprice(self):
        return self.previousPrice

    def setpreviousprice(self,previousClosingPrice):
        self.previousPrice = previousClosingPrice

    def getcurrentprice(self):
        return self.currentPrice

    def setcurrentprice(self,currentPrice):
        self.currentPrice= currentPrice

    def getChangepercent(self):
        return self.currentPrice-self.previousPrice

