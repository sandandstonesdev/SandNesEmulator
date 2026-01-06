from emulator.ppu.ppu_frame import PPUFrame
from emulator.ppu.ppu_bus import PPUBus
from emulator.ppu.ppu_instructions import PPUInstructions
from emulator.ppu.ppu_registers import PPURegisters
from emulator.board.interrupt_info import InterruptInfo

# Inject Cartridge or use some technique to read pattern_tables banks
# Some mappers can control PPU ???
class PPU:
    def __init__(self, ppu_bus: PPUBus, interrupt_info: InterruptInfo):
        self.ppu_bus = ppu_bus
        self.ppu_registers = PPURegisters(ppu_bus)
        self.ppu_instructions = PPUInstructions(self.ppu_registers, self.ppu_bus, interrupt_info)
        self.interrupt_info = interrupt_info
        # Object Attribute Memory (OAM) - 256 bytes
        self.OAM = [0x00] * 256  
        # Name Tables (2KB) and Attribute Tables (64B)
        self.pattern_tables = None
        self.NameTable = [0x00] * 2048
        self.PaletteLookup = [0x00] * 32  # Palette Color Lookup (assembled color => RGB)

    def reset(self):
        pass

    def read_register(self, address):
        value = self.ppu_instructions.read_register(address)
        pass

    def write_register(self, address, value):
        self.ppu_instructions.write_register(address, value)
        pass

    # For Pattern Tables and Custom NameTables
    def read_cartidge(self, address):
        pass

    def write_cartidge(self, address, value):
        pass

    def tick(self):
        # 341 dots per scanline
        # 262 scanlines per frame
        # PPUInstructions
        pass

    def render_frame(self):
        pass

    def output_frame(self) -> PPUFrame: 
        # Outputted into TV
        ppu_frame = PPUFrame()
        return ppu_frame