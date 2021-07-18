from hummingbot.client.config.config_var import ConfigVar

new_strategy_config_map = {
    "strategy": ConfigVar(
        key="strategy",
        prompt="",
        default="new_strategy",),
    "connector":
        ConfigVar(key="connector",
                  prompt="Enter the name of the exchange >>> ",
                  prompt_on_new=True,),
    "market": ConfigVar(
        key="market",
        prompt="Enter a market trading_pair: ",
        prompt_on_new=True,
    ),
}
