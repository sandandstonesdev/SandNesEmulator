from emulator.cpu_internal.addr_ops import AddrOps
from emulator.board.bus import Bus
from emulator.cpu.registers import Registers
from emulator.cpu.status_flags import NEGATIVE, ZERO


class LoadStoreOps:
    def __init__(self, registers: Registers, bus: Bus, addr_ops: AddrOps):
        self.registers = registers
        self.bus = bus
        self.addr_ops = addr_ops

    def lda_op(self, decoded_data):
        self.registers.a = self.registers.data
        Z = 1 if self.registers.a == 0 else 0
        N = 1 if (self.registers.a & 0x80) else 0
        self.registers.set_flag(ZERO, Z)
        self.registers.set_flag(NEGATIVE, N)
        self.registers.cycles += decoded_data.cycles - 1

    def ldx_op(self, decoded_data):
        self.registers.x = self.registers.data
        Z = 1 if self.registers.x == 0 else 0
        N = 1 if (self.registers.x & 0x80) else 0
        self.registers.set_flag(ZERO, Z)
        self.registers.set_flag(NEGATIVE, N)
        self.registers.cycles += decoded_data.cycles - 1

    def ldy_op(self, decoded_data):
        self.registers.y = self.registers.data
        Z = 1 if self.registers.y == 0 else 0
        N = 1 if (self.registers.y & 0x80) else 0
        self.registers.set_flag(ZERO, Z)
        self.registers.set_flag(NEGATIVE, N)
        self.registers.cycles += decoded_data.cycles - 1

    def sta_op(self, decoded_data):
        self.addr_ops.result_store_op(decoded_data)
        self.registers.cycles += decoded_data.cycles - 1

    def stx_op(self, decoded_data):
        self.addr_ops.result_store_op(decoded_data)
        self.registers.cycles += decoded_data.cycles - 1

    def sty_op(self, decoded_data):
        self.addr_ops.result_store_op(decoded_data)
        self.registers.cycles += decoded_data.cycles - 1