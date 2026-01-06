from abc import ABC, abstractmethod

class BaseMapRouter(ABC):
    def __init__(self, cartridge):
        self.cartridge = cartridge

    @abstractmethod
    def route_read(self, address):
        pass

    @abstractmethod
    def route_write(self, address, value):
        pass