# Status flags
from emulator.board.bus import Bus
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
        self.data = 0  # Data bus
        self.adl = 0  # Address Low byte
        self.adh = 0  # Address High byte
        self.bus = bus
        

    def reset(self):
        self.a = 0
        self.x = 0
        self.y = 0
        self.s.reset()
        self.set_flag(UNUSED, 1)  # Interrupt Disable set on reset
        self.set_flag(INTERRUPT, 1)  # Interrupt Disable set on reset
        self.set_flag(DECIMAL, 0)  # Clear Decimal Mode
        self.adl = 0  # Address Low byte
        self.adh = 0  # Address High byte
        self.data = 0  # Data bus
        self.set_pc(self.bus.read(0xFFFD), self.bus.read(0xFFFC))
        self.cycles = 7  # Reset takes time

    def irq(self):
        if self.get_flag(INTERRUPT) == 0:
            self.push_pc()
            self.push_status()

            self.set_flag(INTERRUPT, 1)
            self.set_pc(self.bus.read(0xFFFE), self.bus.read(0xFFFF))
            self.cycles += 7

    def nmi(self):
        self.push_pc()
        self.push_status()

        self.set_flag(INTERRUPT, 1)
        self.set_pc(self.bus.read(0xFFFA), self.bus.read(0xFFFB))
        self.cycles += 8

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

    def inc_pc(self, value=1):
        self.pc = (self.pc + value) & 0xFFFF

    def inc_cycles(self, value=1):
        self.cycles += value

    def get_addr(self):
        return (self.adh << 8) | self.adl

    def set_addr(self, address_high: int, address_low: int):
        self.adh = address_high
        self.adl = address_low

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