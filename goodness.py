class Quotes():
    def __init__(self):
        '''Init empty list for containing qoutes '''
        self.contain = []
        self.length = 0
        
    def add_symbol(self, quot):
        '''Add new qout 'qout' '''
        self.contain = self.contain + [quot]
        if self.length != 0:
            self.length = min(self.length, len(quot))
        else:
            self.length = len(quot)
            
    def get_day_prices(self, day):
        '''Return list of prises at day with index 'day' '''
        day_prices =[]
        for quot in self.contain:
            day_prices.append(quot[day])
        return day_prices

def goodness(quotes):
    '''goodness(a) -> float
    quotes type should be Quotes
    
    Return a value of goodness,
       0.0 is "good", otherwise "bad"'''
    goodness = 0
    buy_price = sum (quotes.get_day_prices (0))
    
    for day in range(0, quotes.length):
        s = sum (quotes.get_day_prices(day))
        goodness = goodness + (s - buy_price)**2

    goodness = goodness / quotes.length / buy_price / buy_price
    return goodness