from abc import ABC, abstractmethod

class BaseMapper(ABC):
    def __init__(self, cartridge):
        self.cartridge = cartridge

    @abstractmethod
    def map_prg_read(self, address):
        pass

    @abstractmethod
    def map_prg_write(self, address, value):
        pass

    @abstractmethod
    def map_chr_read(self, address):
        pass

    @abstractmethod
    def map_chr_write(self, address, value):
        pass

    @abstractmethod
    def get_pattern_table(self, table_index, size):
        pass