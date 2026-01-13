class CHRROMBank:
    def __init__(self, data: bytearray, base_address: int = 0x0000):
        self.data = data
        self.length = len(data)
        self.base_address = base_address

    def read(self, address):
        address -= self.base_address

        if 0 <= address < self.length:
            return self.data[address]
        else:
            raise IndexError("CHR ROM address out of range")