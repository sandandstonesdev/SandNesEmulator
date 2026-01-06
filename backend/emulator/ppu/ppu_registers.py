from emulator.ppu.ppu_bus import PPUBus


class PPURegisters:
    def __init__(self, ppu_bus: PPUBus):
        # ppu_bus is needed to read/write PPU memory (i.e. name tables)
        self.ppu_bus = ppu_bus

        # 0x2000 - PPU Control Register
        self.ppu_ctrl = 0

        # 0x2001 - PPU Mask Register
        self.ppu_mask = 0
        
        # 0x2002 - PPU Status Register
        # Power-up +0+x xxxx, Reset U??x xxxx
        self.ppu_status = 0
        
        # 0x2003 - OAM Address Register
        self.oam_addr = 0
        # 0x2004 - OAM Data Register
        self.oam_data = 0
        # 0x4014 - PPU DMA Register
        self.oam_dma = 0
        
        # 0x2005 - PPU Scroll Register and Latch
        self.scroll_latch = 0
        self.ppu_scroll = 0

        # 0x2006 - PPU Address Register and Latch
        self.addr_latch = 0
        self.ppu_addr = 0

        # 0x2007 - PPU Data Register
        self.ppu_data = 0
        
        # Internal Registers
        self.odd_frame = False
        self.palette = None # Palette Selected ???

        self.cycle = 0 # dot counter
        self.scanline = 0 # scanline counter
        
    def get_ppu_register_id(self, address: int) -> int:
        # Implement logic to get register ID based on address
        return 0

    def read_register(self, address: int) -> int:
        pass

    def write_register(self, address: int, value: int):
        pass

    def reset(self):
        pass
    
    def hblank(self):
        pass

    def vblank(self):
        pass