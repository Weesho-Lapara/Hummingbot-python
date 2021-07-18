#!/usr/bin/env python

from decimal import Decimal
import logging


from hummingbot.logger import HummingbotLogger
from hummingbot.strategy.strategy_py_base import StrategyPyBase
from hummingbot.strategy.market_trading_pair_tuple import MarketTradingPairTuple

hws_logger = None


class NewStrategy(StrategyPyBase):

    @classmethod
    def logger(cls) -> HummingbotLogger:
        global hws_logger
        if hws_logger is None:
            hws_logger = logging.getLogger(__name__)
        return hws_logger

    def __init__(self,
                 market_info: MarketTradingPairTuple,
                 ):

        super().__init__()
        self._market_info = market_info
        self._connector_ready = False
        self._bought_eth = False
        self.add_markets([market_info.market])

    def tick(self, timestamp: float):
        if not self._connector_ready:
            self._connector_ready = self._market_info.market
            if not self._connector_ready:
                self.logger().warning(f"{self._market_info.market.name} is not ready. Please wait...")
                return
            else:
                self.logger().warning(f"{self._market_info.market.name} is ready. Trading started")

        if not self._bought_eth:
            mid_price = self._market_info.get_mid_price()
            order_id = self.buy_with_specific_market(self._market_info,
                                                     Decimal("0.005"),
                                                     OrderType.LIMIT,
                                                     mid_price)
            self.logger().info(f"Sumbitted buy order {order_id}")
            self._bought_eth = True


    def did_complete_buy_order(self, order_completed_event):
        self.logger().info("Your order has been fulfilled")
        self.logger().info(order_completed_event)
