
class Server:
    def __init__(self, url: str) -> None:
        self.url = url
        self.is_alive = True
        self.active_connections = 0

    def __repr__(self) -> str:
        return f"<Server url={self.url} alive={self.is_alive} conns={self.active_connections}>"