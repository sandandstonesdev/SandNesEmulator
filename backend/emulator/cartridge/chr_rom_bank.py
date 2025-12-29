class CHRROMBank:
    def __init__(self, data: bytearray):
        self.data = data

    def read(self, address):
        if 0 <= address < len(self.data):
            return self.data[address]
        else:
            raise IndexError("CHR ROM address out of range")