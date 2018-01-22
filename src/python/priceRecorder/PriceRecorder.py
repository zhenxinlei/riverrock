from src.python.priceRecorder import OptionsPriceRecorder

class PriceRecorder:
    def __init__(self, symbols, mkt_type, api_key, interval="d"):
        self.interval = interval
        if self.interval not in ['d','h','m']:
            raise ValueError("Invalid interval: valid values are  'd', 'h' and 'm'.")  # noqa

        if self.mkt_type not in ['options', 'equity']:
            raise ValueError("Invalid interval: valid values are  'options', 'equity'.")  # noqa

        return OptionsPriceRecorder(symbols, api_key, interval)



