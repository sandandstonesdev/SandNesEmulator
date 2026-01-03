from emulator.mapping.device_maps import READ_DEVICE_MAP, WRITE_DEVICE_MAP

class MemoryMapRouter:
    def __init__(self):
        self.read_device_map = READ_DEVICE_MAP
        self.write_device_map = WRITE_DEVICE_MAP


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