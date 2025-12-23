from backend.emulator.bus import Bus
from backend.emulator.opcodes import opcode_lookup

# Status flags
NEGATIVE = 0x80  # N
OVERFLOW = 0x40  # V
UNUSED   = 0x20  # -
BREAK    = 0x10  # B
DECIMAL  = 0x08  # D
INTERRUPT= 0x04  # I
ZERO     = 0x02  # Z
CARRY    = 0x01  # C

class CPU:
    def __init__(self, bus: Bus):
        self.bus = bus
        self.reset()
        
        pass

    def power_on(self):
        pass

    def reset(self):
        pass

    def tick(self):
        # Fetch - Recognized operation and addressing mode
        opcode = self.bus.read_prg(self.pc)
        opcode_details = opcode_lookup[opcode]
        addr_mode = opcode_details['addr_mode']
        cycles = opcode_details['cycles']
        mnemonic = opcode_details['mnemonic']
        # Read operands
        # Execute
        self.fetch_next()
        pass

    def reset(self):
        self.pc = 0xfffc
        self.sp = 0xfd # Simulate reset (flags, low/high bytes)
        self.s = 0x00 | INTERRUPT # Simulate reset state
        self.a = 0
        self.x = 0
        self.y = 0
        self.cycles += 8

    def irq(self):
        pass

    def nmi(self):
        pass
