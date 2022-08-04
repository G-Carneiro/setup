class Symlink:
    def __init__(self, name: str, origin: str, destiny: str):
        self._name: str = name
        self._origin: str = origin
        self._destiny: str = destiny

    def name(self) -> str:
        return self._name

    def origin(self) -> str:
        return self._origin

    def destiny(self) -> str:
        return self._destiny
