from hummingbot.strategy.market_trading_pair_tuple import MarketTradingPairTuple
from hummingbot.strategy.test_strategy import TestStrategy
from hummingbot.strategy.test_strategy_config_map import test_strategy_config_map as c_map


def start(self):
    connector = c_map.get("connector").value.lower()
    market = c_map.get("market").value

    self._initialize_markets([(connector, [market])])
    base, quote = market.split("-")
    market_info = MarketTradingPairTuple(
        self.markets[connector], market, base, quote)
    self.market_trading_pair_tuples = [market_info]

    self.strategy = TestStrategy(market_info)
