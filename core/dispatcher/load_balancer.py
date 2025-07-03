from core.balancer.strategy import LoadBalancerStrategy
from core.server_manager.manager import ServerManager
from core.balancer.registry import StrategyRegistry

class LoadBalancer:
    def __init__(self, strategy_name: str) -> None:
        self.strategy: LoadBalancerStrategy = StrategyRegistry.get(strategy_name)
        self.server_manager = ServerManager()

    def get_next_server(self) -> str:
        alive_servers = self.server_manager.get_alive_servers()
        if not alive_servers:
            raise Exception("No healthy servers available.")
        return self.strategy.select_server(alive_servers)
    
    def add_server(self, url: str):
        self.server_manager.add_server(url)

    def remove_server(self, url: str):
        self.server_manager.remove_server(url)