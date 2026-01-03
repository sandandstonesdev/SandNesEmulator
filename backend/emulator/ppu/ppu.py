from emulator.mapping.io_register_router import IORegisterRouter
from emulator.mapping.io_register_type import IORegisterType
from emulator.ppu.ppu_instructions import PPUInstructions
from emulator.ppu.ppu_registers import PPURegisters
from emulator.board.interrupt_info import InterruptInfo

class PPU:
    def __init__(self, io_register_router: IORegisterRouter, interrupt_info: InterruptInfo):
        self.io_register_router = io_register_router
        self.ppu_registers = PPURegisters()
        self.ppu_instructions = PPUInstructions(self.ppu_registers, interrupt_info)
        self.interrupt_info = interrupt_info
        # Object Attribute Memory (OAM) - 256 bytes
        self.OAM = [0x00] * 256  
        # Name Tables (2KB) and Attribute Tables (64B)
        self.pattern_tables = None
        self.NameTable = [0x00] * 2048
        self.PaletteLookup = [0x00] * 32  # Palette Color Lookup (assembled color => RGB)

    def reset(self):
        pass

    # Filling flags OAM, nametable memory
    def read(self, address):
        mapped_port = self.ppu_registers.route_read(address)
        if mapped_port == IORegisterType.PPUCTRL:
            return self.ppu_instructions.read_ppu_control()
        elif mapped_port == IORegisterType.PPUMASK:
            return self.ppu_instructions.read_ppu_mask()
        elif mapped_port == IORegisterType.PPUSTATUS:
            return self.ppu_instructions.read_ppu_status()
        elif mapped_port == IORegisterType.OAMADDR:
            return self.ppu_instructions.read_oam_address()
        elif mapped_port == IORegisterType.OAMDATA:
            return self.ppu_instructions.read_oam_data()
        elif mapped_port == IORegisterType.PPUSCROLL:
            return self.ppu_instructions.read_ppu_scroll()
        elif mapped_port == IORegisterType.PPUADDR:
            return self.ppu_instructions.read_ppu_address()
        elif mapped_port == IORegisterType.PPUDATA:
            return self.ppu_instructions.read_ppu_data()
        elif mapped_port == IORegisterType.OAMDMA:
            return self.ppu_instructions.read_oam_dma()

    def write(self, address, value):
        mapped_port = self.io_.route_write(address)
        if mapped_port == IORegisterType.PPUCTRL:
            self.ppu_instructions.write_ppu_control(value)
        elif mapped_port == IORegisterType.PPUMASK:
            self.ppu_instructions.write_ppu_mask(value)
        elif mapped_port == IORegisterType.PPUSTATUS:
            self.ppu_instructions.write_ppu_status(value)
        elif mapped_port == IORegisterType.OAMADDR:
            self.ppu_instructions.write_oam_address(value)
        elif mapped_port == IORegisterType.OAMDATA:
            self.ppu_instructions.write_oam_data(value)
        elif mapped_port == IORegisterType.PPUSCROLL:
            self.ppu_instructions.write_ppu_scroll(value)
        elif mapped_port == IORegisterType.PPUADDR:
            self.ppu_instructions.write_ppu_address(value)
        elif mapped_port == IORegisterType.PPUDATA:
            self.ppu_instructions.write_ppu_data(value)
        elif mapped_port == IORegisterType.OAMDMA:
            self.ppu_instructions.write_oam_dma(value)

    def transfer_oam(self, data):
        pass

    def tick(self):
        # 341 dots per scanline
        # 262 scanlines per frame
        # PPUInstructions
        pass

    def render_frame(self):
        pass