
from emulator.cartridge.mapper_0_maps import MAPPER_0_READ_MAP, MAPPER_0_WRITE_MAP

class CartridgeMapRouter:
    def __init__(self):
        self.read_device_map = MAPPER_0_READ_MAP
        self.write_device_map = MAPPER_0_WRITE_MAP

    def route_read(self, address):
        for (start, end), device in self.read_device_map.items():
            if start <= address <= end:
                return device
        return None


    def route_write(self, address, value):
        for (start, end), device in self.write_device_map.items():
            if start <= address <= end:
                return device
        return None