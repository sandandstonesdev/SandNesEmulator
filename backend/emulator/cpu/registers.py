# Status flags
from emulator.cpu.stack import Stack
from emulator.cpu.status_flags import DECIMAL, INTERRUPT, UNUSED, StatusFlags

class Registers:
    def __init__(self):
        self.a = 0  # Accumulator
        self.x = 0  # X Register
        self.y = 0  # Y Register
        self.pc = 0  # Program Counter
        self.s = Stack()  # Stack Pointer
        self.p = StatusFlags()  # Status Register
        self.cycles = 0  # Cycle count
        self.d = 0  # Data bus
        self.adl = 0  # Address Low byte
        self.adh = 0  # Address High byte
        

    def reset(self):
        self.a = 0
        self.x = 0
        self.y = 0
        self.pc = 0
        self.s.push(0xFD)  # Stack Pointer starts at 0xFD
        self.s.push(0x01)  # Stack Pointer high byte
        self.s.push(0xFF)  # Stack Pointer highest byte
        self.cycles = 0 # ??
        self.p.set_flag(UNUSED, 1)  # Interrupt Disable set on reset
        self.p.set_flag(INTERRUPT, 1)  # Interrupt Disable set on reset
        self.p.set_flag(DECIMAL, 0)  # Clear Decimal Mode
        self.adl = 0  # Address Low byte
        self.adh = 0  # Address High byte
        self.d = 0  # Data bus
        self.d = 0  # Data bus

    def set_flag(self, flag, condition):
        self.p.set_flag(flag, 1 if condition else 0)
        
    def get_flag(self, flag):
        return self.p.get_flag(flag)