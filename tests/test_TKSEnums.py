# -*- coding: utf-8 -*-
# Author: Timur Gilmullin


import pytest
from tksbrokerapi import TKSEnums


class TestConstantsConsistent:
    """Checks consistent of constants"""

    @pytest.fixture(scope="function", autouse=True)
    def init(self):
        self.mainConstants = {
            "TKS_DATE_TIME_FORMAT": "<class 'str'>",
            "TKS_DATE_TIME_FORMAT_EXT": "<class 'str'>",
            "TKS_PRINT_DATE_TIME_FORMAT": "<class 'str'>",
            "TKS_INSTRUMENTS": "<class 'list'>",
            "TKS_TICKER_ALIASES": "<class 'dict'>",
            "TKS_TICKERS_OR_FIGI_EXCLUDED": "<class 'list'>",
            "TKS_CANDLE_INTERVALS": "<class 'dict'>",
            "TKS_ACCOUNT_STATUSES": "<class 'dict'>",
            "TKS_ACCOUNT_TYPES": "<class 'dict'>",
            "TKS_ACCESS_LEVELS": "<class 'dict'>",
            "TKS_QUALIFIED_TYPES": "<class 'dict'>",
            "TKS_TRADING_STATUSES": "<class 'dict'>",
            "TKS_OPERATION_TYPES": "<class 'dict'>",
            "TKS_OPERATION_STATES": "<class 'dict'>",
            "TKS_ORDER_DIRECTIONS": "<class 'dict'>",
            "TKS_STOP_ORDER_DIRECTIONS": "<class 'dict'>",
            "TKS_ORDER_TYPES": "<class 'dict'>",
            "TKS_STOP_ORDER_TYPES": "<class 'dict'>",
            "TKS_ORDER_STATES": "<class 'dict'>",
            "TKS_STOP_ORDER_EXPIRATION_TYPES": "<class 'dict'>",
            "TKS_COUPON_TYPES": "<class 'dict'>",
            "TKS_REAL_EXCHANGES": "<class 'dict'>",
        }
        self.mainConstantsNames = self.mainConstants.keys()
        self.currentConstantsNames = dir(TKSEnums)  # constants in fact

    def test_ConsistentOfConstantsNames(self):
        for cName in self.mainConstantsNames:
            assert cName in self.currentConstantsNames, "One of main constants changed it's name! Problem is with [{}]".format(cName)

    def test_ConstantsTypes(self):
        for cName in self.currentConstantsNames:
            if cName in self.mainConstantsNames:
                actualType = str(type(getattr(TKSEnums, cName)))
                assert actualType == self.mainConstants[cName], "Data types mismatch! Constant [{}] must have type [{}], but current is [{}].".format(cName, self.mainConstants[cName], actualType)

    def test_AvailableInstruments(self):
        mainInstruments = ["Currencies", "Shares", "Bonds", "Etfs", "Futures"]
        currentInstruments = TKSEnums.TKS_INSTRUMENTS
        for instrument in mainInstruments:
            assert instrument in currentInstruments, "Instrument [{}] not in available list or changed its name!".format(instrument)
