class RAM:
    # this should handle mirroring internally
    def __init__(self):
        # 0x0000 - 0x07FF: 2KB internal RAM
        self.memory = [0x00] * 2048
        
    def read(self, address):
        if 0x0000 <= address <= 0x1FFF:
            mirrored_address = address & 0x07FF
            return self.memory[mirrored_address]
        # Open bus
        return 0x00  # Default return for out-of-bounds reads

    def write(self, address, value):
        if (address >= 0x0000 and address <= 0x1FFF):
            mirrored_address = address & 0x07FF
            self.memory[mirrored_address] = value & 0xFF
            return True
        return False