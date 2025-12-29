from emulator.mapping.base_mapper import BaseMapper

# Mapper is memory map router
# Input address from CPU/PPU/APU/Joypad
# Output mapped address to Cartridge/RAM/PPU/APU/Joypad

class Mapper0(BaseMapper):
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

    def get_pattern_table(self, table_index, size):
        return super().get_pattern_table(table_index, size)