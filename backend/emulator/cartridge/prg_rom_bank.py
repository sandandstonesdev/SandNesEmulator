class PrgRomBank:
    def __init__(self, data: bytearray, base_address: int):
        self.data = data
        self.length = len(data)
        self.base_address = base_address
        #if base_address == 0xC000:
        #    self.last = self.data[:16]
    
    def dump_to_file(self, file_path: str):
        with open(file_path, 'wb') as f:
            f.write(self.data)

    def read(self, address):
        address -= self.base_address

        if 0 <= address < self.length:
            return self.data[address]
        else:
            raise IndexError("PRG ROM address out of range")