from abc import ABC, abstractmethod

class Mapper(ABC):
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


class Mapper0(Mapper):
    def __init__(self):
        pass

    def map_prg_read(self, address):
        # It maps address for:
        #self.cartridge.read_prg(address)
        pass

    def map_prg_write(self, address, value):
        # It maps address for:
        # self.cartridge.write_prg(address, value)
        pass

    def map_chr_read(self, address):
        # It maps address for:
        # self.cartridge.read_chr(address)
        pass

    def map_chr_write(self, address, value):
        # It maps address for:
        # self.cartridge.write_chr(address, value)
        pass