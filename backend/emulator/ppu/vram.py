class VRAM:
    # this should handle mirroring internally
    def __init__(self):
        # 2KB VRAM for Name Tables
        self.vram = [0x00] * 2048
        # 32 bytes Palette RAM
        self.palette_ram = [0x00] * 32

    def read(self, address):
        # Read Name Table or Palette RAM based on address
        pass

    def write(self, address, value):
        # Write to Name Table or Palette RAM based on address
        pass