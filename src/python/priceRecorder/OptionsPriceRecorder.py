from src.python.apiManger.BarchartClient import BarchartClient as bc
from src.python.apiManger.ApiKeys import ApiKeys

'''
base_url="https://marketdata.websol.barchart.com"
'''
class OptionsPriceRecorder:
    def __init__(self, symbols, api_key, interval):
        self.api_key = api_key
        self.interval= interval
        self.base_url="https://marketdata.websol.barchart.com"
        self.symbols = symbols


    def getEoTData(self):
        bc(ApiKeys.BARCHART_API_KEY)
        return bc.equity_options("APPL,AXP")



