from emulator.bus import Bus
from emulator.cpu.registers import Registers
from emulator.cpu.decoded_data_dto import DecodedDataDTO

class ALUOps:
        def __init__(self, registers: Registers, bus: Bus):
                self.registers = registers
                self.bus = bus # Need for stack

        def adc_op(self, decoded_data: DecodedDataDTO):
                temp = self.registers.a + self.registers.d + self.registers.p.C

                self.registers.p.C = 1 if temp > 0xFF else 0
                result = temp & 0xFF

                self.registers.p.V = 1 if (~(self.registers.a ^ self.registers.d) & (self.registers.a ^ result) & 0x80) else 0
                self.registers.p.Z = 1 if result == 0 else 0
                self.registers.p.N = 1 if (result & 0x80) else 0

                self.registers.a = result
                        # Minus Opcode Fetch cycle
                self.registers.cycles += decoded_data.cycles - 1

                return True

        def sbc_op(self, decoded_data: DecodedDataDTO):
                operand = self.registers.d ^ 0xFF  # One's complement for subtraction
                temp = self.registers.a + operand + self.registers.p.C
                self.registers.p.C = 1 if temp > 0xFF else 0
                self.registers.p.V = 1 if ((self.registers.a ^ temp) & (operand ^ temp) & 0x80) else 0
                result = temp & 0xFF
                self.registers.p.Z = 1 if result == 0 else 0
                self.registers.p.N = 1 if (result & 0x80) else 0

                self.registers.a = result
                self.registers.cycles += decoded_data.cycles - 1

        def ora_op(self, decoded_data: DecodedDataDTO):
                result = self.registers.a | self.registers.d
                self.registers.p.Z = 1 if result == 0 else 0
                self.registers.p.N = 1 if (result & 0x80) else 0
                self.registers.a = result
                self.registers.cycles += decoded_data.cycles - 1

        def and_op(self, decoded_data: DecodedDataDTO):
                result = self.registers.a & self.registers.d
                self.registers.p.Z = 1 if result == 0 else 0
                self.registers.p.N = 1 if (result & 0x80) else 0
                self.registers.a = result
                self.registers.cycles += decoded_data.cycles - 1

        def eor_op(self, decoded_data: DecodedDataDTO):
                result = self.registers.a ^ self.registers.d
                self.registers.p.Z = 1 if result == 0 else 0
                self.registers.p.N = 1 if (result & 0x80) else 0
                self.registers.a = result
                self.registers.cycles += decoded_data.cycles - 1

        