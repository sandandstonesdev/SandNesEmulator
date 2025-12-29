from emulator.cpu.instructions import ExecutionUnit
from emulator.cpu.registers import Registers
from emulator.bus import Bus

# Decouple Fetcher
# Decouple Decoder
# Decouple Executor

class CPU:
    def __init__(self, bus: Bus):
        self.bus = bus
        self.registers = Registers()
        # Execution using should see Bus and Registers
        self.execution_unit = ExecutionUnit(self.registers)
        pass

    def power_on(self):
        pass

    def reset(self):
        self.registers.reset()
        self.cycles = 8
        pass

    def tick(self):\
        # Fetch read is ok, there's map route inside bus
        opcode = self.bus.ram_read(self.registers.pc)
        # Decode
        decoded_data = self.execution_unit.decode(opcode, self.registers.pc)
        # Execute
        self.execution_unit.execute(decoded_data)

        # Update PC and Cycles (should be done in Executor ideally)
        self.registers.pc += decoded_data.length
        self.registers.cycles += decoded_data.cycles

    def irq(self):
        pass

    def nmi(self):
        pass
