from abc import ABC, abstractmethod

class BaseMapper(ABC):
    def __init__(self, cartridge):
        self.cartridge = cartridge

    @abstractmethod
    def map_read(self, address):
        pass

    @abstractmethod
    def map_write(self, address, value):
        pass