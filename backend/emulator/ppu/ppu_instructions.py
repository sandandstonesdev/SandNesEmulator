from emulator.ppu.ppu_bus import PPUBus
from emulator.ppu.ppu_registers import PPURegisters
from emulator.board.interrupt_info import InterruptInfo

class PPUInstructions:
    def __init__(self, ppu_registers: PPURegisters, ppu_bus: PPUBus, interrupt_info: InterruptInfo):
        self.ppu_registers = ppu_registers
        self.ppu_bus = ppu_bus
        self.interrupt_info = interrupt_info
        self.cycles = 0
        pass

    def reset(self):
        self.ppu_registers.reset()

    def read_register(self, address):
        register_id = self.get_ppu_register_id(address)
        if register_id == 0:
            return 0 # Error
            # Implement reading logic for this register
        else:
            pass

        # Handle address latching
        # Handle register read and Open-bus behavior
        # Read from bus (processed address and value)

    def get_ppu_register_id(self, address: int) -> int:
      return self.ppu_registers.get_ppu_register_id(address)

    def write_register(self, address, value):
        register_id = self.get_ppu_register_id(address)
        if register_id == 0:
            return 0 # Error
            # Implement reading logic for this register
        else:
            pass
        
        # Handle address latching
        # Handle register write and Open-bus behavior
        # Write to bus (processed address and value)
        pass

    def transfer_oam(self, data):
        pass

    def screen_render_tick(self):
        pass

    def scanline_execuyr(self, index: int): 
        # Pseudomicrocode calls Like CPU fetch, decode, execute
        # Data Fetch 8 cycles
        self.NTByteFetch()
        self.ATByteFetch()
        self.BGLsBitsFetch()
        self.BGMsBitsFetch()
        self.IncHorizontal() # No cycle inc
        #...

        self.IncVertical() # No cycle inc

        pass

    def NTByteFetch(self, address, value):
        cycles += 2
        pass

    def ATByteFetch(self, address, value):
        cycles += 2
        pass

    def BGLsBitsFetch(self, address, value): # Pattern Table Tile Low
        cycles += 2
        pass

    def BGMsBitsFetch(self, address, value): # Pattern Table Tile High
                                             # 8 bytes above low bits
        cycles += 2
        pass

    def IncHorizontal(self):
        pass

    def IncVertical(self):
        pass

    def UnusedNTFetch(self, address, value):
        # Update Internal NTByte Register
        self.cycles += 2
        pass

    def IgnoredNTFetch(self, address, value):
        cycles += 2
        pass

    def SetVBlankFlag(self):
        # (241, 1) - scanline, cycle
        # cycles += 1
        pass

    # Three below advances cycles by 1 (together 1 cycle)
    def ClearVBlankFlag(self):\
        # (261, 1) - scanline, cycle
        pass

    def Sprite0Hit(self):
        # (261, 1) - scanline, cycle
        pass

    def SpriteOverflow(self):
        # (261, 1) - scanline, cycle
        pass


    # From 261 cycle in scanline 0-239
    def SpriteLsBitsFetch(self):
        pass

    def SpriteMsBitsFetch(self):
        pass

    # cycles 65-256
    def SpriteEvaluation(self):
        pass

    # cycles 1-64
    def SecondaryOAMClear(self):
        pass