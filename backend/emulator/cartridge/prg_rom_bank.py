class PrgRomBank:
    def __init__(self, data: bytearray, base_address: int = 0x8000):
        self.data = data
        self.base_address = base_address

    def read(self, address):
        # Remap addres to zero-based index

        address -= self.base_address
        
        if 0 <= address < len(self.data):
            return self.data[address]
        else:
            raise IndexError("PRG ROM address out of range")