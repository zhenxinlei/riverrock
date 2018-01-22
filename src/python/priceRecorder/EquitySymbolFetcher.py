from src.python.apiManger.BarchartClient import BarchartClient as bc
from src.python.apiManger.ApiKeys import ApiKeys

class EqutiySymbolFecter:
    def __init__(self):
        pass

    def getSymbolByIndex(self, index):
        '''
        index: $ONE, $IDX, $SPX, $IQY, $RUI, $IUX, $RUA, $IUXX, $DOWC, $DOWT, $DOWU, $DOWI, $TXCX,
        $JX, $TXSX, $TTCS, $TOOC, $TXTW, $TTCD, $TTCS, $TTEN, $TTFS, $TTIN, $TTTK, $TTMT,
        $TTHC, $TTRE, $TTTS, $TTUT, $RTCM, $RTRE
        :return:

        sampler GET:  https://ondemand.websol.barchart.com/getIndexMembers.json?apikey=<YOUR API KEY>&symbol=%24SPX&fields=exchange
        '''
        #TODO
        bc.index_members(index)
        pass

    def getSymbolByEtf(self):
        #TODO
        pass

    def getSectorsSymbols(self, sector, include_etf=False):
        #TODO
        pass
