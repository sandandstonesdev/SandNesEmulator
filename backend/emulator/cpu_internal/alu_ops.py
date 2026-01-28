from emulator.cpu_internal.addr_ops import AddrOps
from emulator.cpu.status_flags import CARRY, NEGATIVE, OVERFLOW, ZERO
from emulator.board.bus import Bus
from emulator.cpu.registers import Registers
from emulator.cpu.decoded_data_dto import DecodedDataDTO

class ALUOps:
        def __init__(self, registers: Registers, addr_ops: AddrOps):
                self.registers = registers
                self.addr_ops = addr_ops

        def adc_op(self, decoded_data: DecodedDataDTO):
                temp = self.registers.a + self.registers.data + self.registers.p.C

                self.registers.p.C = 1 if temp > 0xFF else 0
                result = temp & 0xFF

                V = 1 if (~(self.registers.a ^ self.registers.data) & (self.registers.a ^ result) & 0x80) else 0
                self.registers.set_flag(OVERFLOW, V)
                Z = 1 if result == 0 else 0
                self.registers.set_flag(ZERO, Z)
                N = 1 if (result & 0x80) else 0
                self.registers.set_flag(NEGATIVE, N)

                self.registers.a = result
                        # Minus Opcode Fetch cycle
                self.registers.cycles += decoded_data.cycles - 1

                return True

        def sbc_op(self, decoded_data: DecodedDataDTO):
                operand = self.registers.data ^ 0xFF  # One's complement for subtraction
                temp = self.registers.a + operand + self.registers.p.C
                C = 1 if temp > 0xFF else 0
                self.registers.set_flag(CARRY, C)
                V = 1 if ((self.registers.a ^ temp) & (operand ^ temp) & 0x80) else 0
                self.registers.set_flag(OVERFLOW, V)
                result = temp & 0xFF
                Z = 1 if result == 0 else 0
                self.registers.set_flag(ZERO, Z)
                N = 1 if (result & 0x80) else 0
                self.registers.set_flag(NEGATIVE, N)

                self.registers.a = result
                self.registers.cycles += decoded_data.cycles - 1

        def ora_op(self, decoded_data: DecodedDataDTO):
                result = self.registers.a | self.registers.data
                Z = 1 if result == 0 else 0
                N = 1 if (result & 0x80) else 0
                self.registers.set_flag(ZERO, Z)
                self.registers.set_flag(NEGATIVE, N)
                self.registers.a = result
                self.registers.cycles += decoded_data.cycles - 1

        def and_op(self, decoded_data: DecodedDataDTO):
                result = self.registers.a & self.registers.data
                Z = 1 if result == 0 else 0
                N = 1 if (result & 0x80) else 0
                self.registers.set_flag(ZERO, Z)
                self.registers.set_flag(NEGATIVE, N)
                self.registers.a = result
                self.registers.cycles += decoded_data.cycles - 1

        def eor_op(self, decoded_data: DecodedDataDTO):
                result = self.registers.a ^ self.registers.data
                Z = 1 if result == 0 else 0
                N = 1 if (result & 0x80) else 0
                self.registers.set_flag(ZERO, Z)
                self.registers.set_flag(NEGATIVE, N)
                self.registers.a = result
                self.registers.cycles += decoded_data.cycles - 1

        def inc_op(self, decoded_data: DecodedDataDTO):
                result = (self.registers.data + 1) & 0xFF
                Z = 1 if result == 0 else 0
                N = 1 if (result & 0x80) else 0
                self.registers.set_flag(ZERO, Z)
                self.registers.set_flag(NEGATIVE, N)
                self.registers.data = result
                self.addr_ops.result_store_op(decoded_data)
                self.registers.cycles += decoded_data.cycles - 1

        def dec_op(self, decoded_data: DecodedDataDTO):
                result = (self.registers.data - 1) & 0xFF
                Z = 1 if result == 0 else 0
                N = 1 if (result & 0x80) else 0
                self.registers.set_flag(ZERO, Z)
                self.registers.set_flag(NEGATIVE, N)
                self.registers.data = result
                self.addr_ops.result_store_op(decoded_data)
                self.registers.cycles += decoded_data.cycles - 1

        def inx_op(self, decoded_data: DecodedDataDTO):
                result = (self.registers.x + 1) & 0xFF
                Z = 1 if result == 0 else 0
                N = 1 if (result & 0x80) else 0
                self.registers.set_flag(ZERO, Z)
                self.registers.set_flag(NEGATIVE, N)
                self.registers.x = result
                self.registers.cycles += decoded_data.cycles - 1

        def dex_op(self, decoded_data: DecodedDataDTO):
                result = (self.registers.x - 1) & 0xFF
                Z = 1 if result == 0 else 0
                N = 1 if (result & 0x80) else 0
                self.registers.set_flag(ZERO, Z)
                self.registers.set_flag(NEGATIVE, N)
                self.registers.x = result
                self.registers.cycles += decoded_data.cycles - 1

        def iny_op(self, decoded_data: DecodedDataDTO):
                result = (self.registers.y + 1) & 0xFF
                Z = 1 if result == 0 else 0
                N = 1 if (result & 0x80) else 0
                self.registers.set_flag(ZERO, Z)
                self.registers.set_flag(NEGATIVE, N)
                self.registers.y = result
                self.registers.cycles += decoded_data.cycles - 1

        def dey_op(self, decoded_data: DecodedDataDTO):
                result = (self.registers.y - 1) & 0xFF
                Z = 1 if result == 0 else 0
                N = 1 if (result & 0x80) else 0
                self.registers.set_flag(ZERO, Z)
                self.registers.set_flag(NEGATIVE, N)
                self.registers.y = result
                self.registers.cycles += decoded_data.cycles - 1
        