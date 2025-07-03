from abc import ABC, abstractmethod
from typing import List

class LoadBalancerStrategy(ABC):
    
    @abstractmethod
    def select_server(self, servers: List[str]) -> str:
        """
        Select a server from list of available servers.
        """
        pass

