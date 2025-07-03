from typing import List, Dict
from typing_extensions import Self
from .server import Server

class ServerManager:
    _instance = None
    _initialized = False  # new flag to avoid re-init

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ServerManager, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        if not self._initialized:
            self._servers: Dict[str, Server] = {}
            ServerManager._initialized = True  # set only once
    
    def add_server(self, url: str):
        if url not in self._servers:
            self._servers[url] = Server(url)

    def remove_server(self, url: str):
        self._servers.pop(url, None)

    def mark_alive(self, url: str, alive: bool):
        if url in self._servers:
            self._servers[url].is_alive = alive

    def increment_connections(self, url: str):
        if url in self._servers:
            self._servers[url].active_connections += 1

    def decrement_connections(self, url: str):
        if url in self._servers and self._servers[url].active_connections > 0:
            self._servers[url].active_connections -= 1

    def get_alive_servers(self) -> List[str]:
        return [
            url for url, srv in self._servers.items() if srv.is_alive
        ]

    def get_server(self, url: str) -> Server:
        return self._servers.get(url)

    def get_all(self) -> List[Server]:
        return list(self._servers.values())