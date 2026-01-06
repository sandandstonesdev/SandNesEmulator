from emulator.mapping.base_mapping.base_map_router import BaseMapRouter

class DefaultMapRouter(BaseMapRouter):
    def __init__(self, read_space_map, write_space_map):
        self.read_space_map = read_space_map
        self.write_space_map = write_space_map

    def route_read(self, address):
        for (start, end), device in self.read_space_map.items():
            if start <= address <= end:
                return device
        return None

    def route_write(self, address, value):
        for (start, end), device in self.write_space_map.items():
            if start <= address <= end:
                return device
        return None