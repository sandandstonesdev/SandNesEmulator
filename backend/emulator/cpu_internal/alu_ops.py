from emulator.cpu.status_flags import NEGATIVE, OVERFLOW, ZERO
from emulator.board.bus import Bus
from emulator.cpu.registers import Registers
from emulator.cpu.decoded_data_dto import DecodedDataDTO

class ALUOps:
        def __init__(self, registers: Registers):
                self.registers = registers

        def adc_op(self, decoded_data: DecodedDataDTO):
                temp = self.registers.a + self.registers.d + self.registers.p.C

                self.registers.p.C = 1 if temp > 0xFF else 0
                result = temp & 0xFF

                V = 1 if (~(self.registers.a ^ self.registers.d) & (self.registers.a ^ result) & 0x80) else 0
                self.registers.set_flag(OVERFLOW, V)
                Z = 1 if result == 0 else 0
                self.registers.set_flag(ZERO, Z)  # Zero Flag
                N = 1 if (result & 0x80) else 0
                self.registers.set_flag(NEGATIVE, N)  # Negative Flag

                self.registers.a = result
                        # Minus Opcode Fetch cycle
                self.registers.cycles += decoded_data.cycles - 1

                return True

        def sbc_op(self, decoded_data: DecodedDataDTO):
                operand = self.registers.d ^ 0xFF  # One's complement for subtraction
                temp = self.registers.a + operand + self.registers.p.C
                C = 1 if temp > 0xFF else 0
                self.registers.set_flag(0, C)  # Carry Flag
                V = 1 if ((self.registers.a ^ temp) & (operand ^ temp) & 0x80) else 0
                self.registers.set_flag(OVERFLOW, V)
                result = temp & 0xFF
                Z = 1 if result == 0 else 0
                self.registers.set_flag(ZERO, Z)  # Zero Flag
                N = 1 if (result & 0x80) else 0
                self.registers.set_flag(NEGATIVE, N)  # Negative Flag

                self.registers.a = result
                self.registers.cycles += decoded_data.cycles - 1

        def ora_op(self, decoded_data: DecodedDataDTO):
                result = self.registers.a | self.registers.d
                Z = 1 if result == 0 else 0
                N = 1 if (result & 0x80) else 0
                self.registers.set_flag(ZERO, Z)  # Zero Flag
                self.registers.set_flag(NEGATIVE, N)  # Negative Flag
                self.registers.a = result
                self.registers.cycles += decoded_data.cycles - 1

        def and_op(self, decoded_data: DecodedDataDTO):
                result = self.registers.a & self.registers.d
                Z = 1 if result == 0 else 0
                N = 1 if (result & 0x80) else 0
                self.registers.set_flag(ZERO, Z)  # Zero Flag
                self.registers.set_flag(NEGATIVE, N)  # Negative Flag
                self.registers.a = result
                self.registers.cycles += decoded_data.cycles - 1

        def eor_op(self, decoded_data: DecodedDataDTO):
                result = self.registers.a ^ self.registers.d
                Z = 1 if result == 0 else 0
                N = 1 if (result & 0x80) else 0
                self.registers.set_flag(ZERO, Z)  # Zero Flag
                self.registers.set_flag(NEGATIVE, N)  # Negative Flag
                self.registers.a = result
                self.registers.cycles += decoded_data.cycles - 1

        