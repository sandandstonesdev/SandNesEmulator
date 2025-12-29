# Status flags
NEGATIVE = 0x80  # N
OVERFLOW = 0x40  # V
UNUSED   = 0x20  # -
BREAK    = 0x10  # B
DECIMAL  = 0x08  # D
INTERRUPT= 0x04  # I
ZERO     = 0x02  # Z
CARRY    = 0x01  # C


class Registers:
    def __init__(self):
        self.a = 0  # Accumulator
        self.x = 0  # X Register
        self.y = 0  # Y Register
        self.pc = 0  # Program Counter
        self.s = 0x00  # Stack Pointer
        self.p = 0x00  # Status Register
        self.cycles = 0  # Cycle count
        self.address_bus = 0  # Address bus
        self.d = 0  # Data bus
        self.adl = 0  # Address Low byte
        self.adh = 0  # Address High byte
        

    def reset(self):
        self.a = 0
        self.x = 0
        self.y = 0
        self.pc = 0
        self.s = 0xFD
        self.p = 0x00 | INTERRUPT
        self.address_bus = 0  # Address bus
        self.data_bus = 0  # Data bus
