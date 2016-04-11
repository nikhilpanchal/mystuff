from enum import Enum


class PositionType(Enum):
    """Enumeration for the various types of positions that could exist in the portfolio"""
    LONG = 1
    SHORT = 2


class AssetClass(Enum):
    """Enumeration that holds the various Asset Classes"""
    CASH = 1
    STOCK = 2
    BOND = 3
    MUTUAL_FUND = 4


class CustomSymbols(Enum):
    CASH = 1