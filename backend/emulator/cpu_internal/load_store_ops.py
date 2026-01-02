from emulator.board.bus import Bus
from emulator.cpu.registers import Registers
from emulator.cpu.status_flags import NEGATIVE, ZERO


class LoadStoreOps:
    def __init__(self, registers: Registers, bus: Bus):
        self.registers = registers
        self.bus = bus

    def lda_op(self, decoded_data):
        self.registers.a = self.registers.d
        Z = 1 if self.registers.a == 0 else 0
        N = 1 if (self.registers.a & 0x80) else 0
        self.registers.set_flag(ZERO, Z)  # Zero Flag
        self.registers.set_flag(NEGATIVE, N)  # Negative Flag
        self.registers.cycles += decoded_data.cycles - 1

    def ldx_op(self, decoded_data):
        self.registers.x = self.registers.d
        Z = 1 if self.registers.x == 0 else 0
        N = 1 if (self.registers.x & 0x80) else 0
        self.registers.set_flag(ZERO, Z)  # Zero Flag
        self.registers.set_flag(NEGATIVE, N)  # Negative Flag
        self.registers.cycles += decoded_data.cycles - 1

    def ldy_op(self, decoded_data):
        self.registers.y = self.registers.d
        Z = 1 if self.registers.y == 0 else 0
        N = 1 if (self.registers.y & 0x80) else 0
        self.registers.set_flag(ZERO, Z)  # Zero Flag
        self.registers.set_flag(NEGATIVE, N)  # Negative Flag
        self.registers.cycles += decoded_data.cycles - 1

    def sta_op(self, decoded_data):
        effective_address = self.registers.adh << 8 | self.registers.adl
        self.bus.ram_write(effective_address, self.registers.a)
        self.registers.cycles += decoded_data.cycles - 1

    def stx_op(self, decoded_data):
        effective_address = self.registers.adh << 8 | self.registers.adl
        self.bus.ram_write(effective_address, self.registers.x)
        self.registers.cycles += decoded_data.cycles - 1

    def sty_op(self, decoded_data):
        effective_address = self.registers.adh << 8 | self.registers.adl
        self.bus.ram_write(effective_address, self.registers.y)
        self.registers.cycles += decoded_data.cycles - 1