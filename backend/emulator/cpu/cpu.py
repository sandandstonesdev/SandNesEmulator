from backend.emulator.bus import Bus
from backend.emulator.cpu.instructions import ExecutionUnit
from backend.emulator.cpu.registers import Registers

class CPU:
    def __init__(self, bus: Bus):
        self.bus = bus
        self.registers = Registers()
        self.execution_unit = ExecutionUnit(self.registers)
        pass

    def power_on(self):
        pass

    def reset(self):
        self.registers.reset()
        self.cycles = 8
        pass

    def tick(self):
        opcode = self.bus.read_prg(self.registers.pc)
        decoded_data = self.execution_unit.decode(opcode, self.registers.pc)
        self.execution_unit.execute(decoded_data)
        self.registers.pc += decoded_data.length
        self.registers.cycles += decoded_data.cycles

    def irq(self):
        pass

    def nmi(self):
        pass
