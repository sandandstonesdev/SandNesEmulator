from emulator.mapping.base_mapper import BaseMapper

class PPU:
    def __init__(self):
        # Object Attribute Memory (OAM) - 256 bytes
        self.OAM = [0x00] * 256  
        # Name Tables (2KB) and Attribute Tables (64B)
        self.pattern_tables = None
        self.NameTable = [0x00] * 2048
        self.PaletteLookup = [0x00] * 32  # Palette Color Lookup (assembled color => RGB)
        pass

    # Filling flags OAM, nametable memory
    def read_register(self, address):
        pass

    def write_register(self, address, value):
        pass

    def map_pattern_table(self, mapper: BaseMapper):
        pattern_table_size = 4096  # 4KB per pattern table
        self.pattern_tables = [
            mapper.get_pattern_table(0, pattern_table_size),
            mapper.get_pattern_table(1, pattern_table_size)
        ]
        pass

    def transfer_oam(self, data):
        pass

    def tick(self):
        # 341 dots per scanline
        # 262 scanlines per frame
        pass

    def get_frame(self):
        pass