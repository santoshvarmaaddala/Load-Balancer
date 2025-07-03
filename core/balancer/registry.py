from typing import Type, Dict
from .strategy import LoadBalancerStrategy

class StrategyRegistry:
    _strategies: Dict[str, Type[LoadBalancerStrategy]] = {}

    @classmethod
    def register(cls, name: str, strategy_cls: Type[LoadBalancerStrategy]):
        cls._strategies[name.lower()] = strategy_cls

    @classmethod
    def get(cls, name: str) -> LoadBalancerStrategy:
        strategy_cls = cls._strategies.get(name.lower())

        if not strategy_cls:
            raise ValueError(f"No Strategy registered under name: '{name}'")
        return strategy_cls()


