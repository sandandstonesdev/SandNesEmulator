# Status flags
from emulator.bus import Bus
from emulator.cpu.stack import Stack
from emulator.cpu.status_flags import DECIMAL, INTERRUPT, UNUSED, StatusFlags

class Registers:
    def __init__(self, bus: Bus):
        self.a = 0  # Accumulator
        self.x = 0  # X Register
        self.y = 0  # Y Register
        self.pc = 0  # Program Counter
        self.s = Stack(bus)  # Stack Register
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
        self.s.reset()
        self.s.push(0xFD)  # Stack Pointer starts at 0xFD
        self.s.push(0x01)  # Stack Pointer high byte
        self.s.push(0xFF)  # Stack Pointer highest byte
        self.cycles = 0 # ??
        self.set_flag(UNUSED, 1)  # Interrupt Disable set on reset
        self.set_flag(INTERRUPT, 1)  # Interrupt Disable set on reset
        self.set_flag(DECIMAL, 0)  # Clear Decimal Mode
        self.adl = 0  # Address Low byte
        self.adh = 0  # Address High byte
        self.d = 0  # Data bus
        self.d = 0  # Data bus

    def set_flag(self, flag, condition):
        self.p.set_flag(flag, 1 if condition else 0)
        
    def get_flag(self, flag):
        return self.p.get_flag(flag)

    def push_stack(self, value):
        self.s.push(value)

    def pop_stack(self):
        return self.s.pop()
    
    def set_pc(self, address_high: int, address_low: int):
        self.pc = (address_high << 8) | address_low

    def push_pc(self):
        pc_hi = (self.pc >> 8) & 0xFF
        pc_lo = self.pc & 0xFF
        self.s.push(pc_hi)
        self.s.push(pc_lo)

    def pop_pc(self):
        pc_lo = self.s.pop()
        pc_hi = self.s.pop()
        self.pc = (pc_hi << 8) | pc_lo

    def increment_pc(self, value=1):
        self.pc = (self.pc + value) & 0xFFFF

    def push_status(self):
        status_byte = self.p.get_byte()
        self.s.push(status_byte)

    def pop_status(self):
        status_byte = self.s.pop()
        self.p.set_byte(status_byte)