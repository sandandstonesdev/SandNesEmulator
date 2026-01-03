from emulator.mapping.mapper_0_maps import MAPPER_0_READ_MAP, MAPPER_0_WRITE_MAP
from emulator.mapping.base_mapper import BaseMapper

# Mapper is memory map router
# Input address from CPU/PPU/APU/Joypad
# Output mapped address to Cartridge/RAM/PPU/APU/Joypad

class Mapper0(BaseMapper):
    def __init__(self):
        self.read_device_map = MAPPER_0_READ_MAP
        self.write_device_map = MAPPER_0_WRITE_MAP

    def map_read(self, address):
        for (start, end), device in self.read_device_map.items():
            if start <= address <= end:
                return device
        return None


    def map_write(self, address, value):
        for (start, end), device in self.write_device_map.items():
            if start <= address <= end:
                return device
        return None