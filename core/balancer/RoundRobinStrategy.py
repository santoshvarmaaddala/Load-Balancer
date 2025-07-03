from .strategy import LoadBalancerStrategy
from typing import List
from .registry import StrategyRegistry

class RoundRobinStrategy(LoadBalancerStrategy):

    def __init__(self) -> None:
        self.index = 0

    def select_server(self, servers: List[str]) -> str:
        if not servers:
            raise Exception("No available servers")
        
        server = servers[self.index % len(servers)]
        self.index += 1
        return server
    
# Registering Strategy
StrategyRegistry.register("round_robin", RoundRobinStrategy)