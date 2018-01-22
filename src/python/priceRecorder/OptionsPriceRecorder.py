
'''
base_url="https://marketdata.websol.barchart.com"
'''
class OptionsPriceRecorder:
    def __init__(self, symbols, api_key, interval):
        self.api_key = api_key
        self.interval= interval
        self.base_url="https://marketdata.websol.barchart.com"
        self.symbols = symbols
