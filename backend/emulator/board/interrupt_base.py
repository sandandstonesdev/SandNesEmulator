from abc import ABC

class InterruptBase(ABC):
    def __init__(self):
        self._enabled = False
        self._requested = False
        self._address = 0x0000

    @property
    def enabled(self): # PPU flag
        return self._enabled

    @enabled.setter
    def enabled(self, value: bool):
        self._enabled = value

    @property
    def requested(self):
        return self._requested
    
    @requested.setter
    def requested(self, value: bool):
        self._requested = value
    @property
    def address(self):
        return self._address
    
    @address.setter
    def address(self, value: int):
        self._address = value

    def request(self):
        if self.enabled:
            self._requested = True
        else:
            self._requested = False