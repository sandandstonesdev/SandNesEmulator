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

    def read_zp(self, address):
        if 0x0000 <= address <= 0x00FF:
            return self.memory[address & 0x00FF]
        return 0x00
    
    def read_stack(self, address):
        if 0x0100 <= address <= 0x01FF:
            return self.memory[address & 0x07FF]
        return 0x00

    def write(self, address, value):
        if (address >= 0x0000 and address <= 0x1FFF):
            mirrored_address = address & 0x07FF
            self.memory[mirrored_address] = value & 0xFF
            return True
        return False
    
    def write_zp(self, address, value):
        if 0x0000 <= address <= 0x00FF:
            self.memory[address & 0x00FF] = value & 0xFF
            return True
        return False
    
    def write_stack(self, address, value):
        if 0x0100 <= address <= 0x01FF:
            self.memory[address & 0x07FF] = value & 0xFF
            return True
        return False