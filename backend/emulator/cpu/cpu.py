from emulator.cpu.instruction_processor import InstructionProcessor
from emulator.cpu.registers import Registers
from emulator.bus import Bus

# Decouple Fetcher
# Decouple Decoder
# Decouple Executor

class CPU:
    def __init__(self, bus: Bus):
        self.bus = bus
        self.registers = Registers()
        self.instructions= InstructionProcessor(self.registers, self.bus)
        pass

    def power_on(self):
        pass

    def reset(self):
        self.registers.reset()
        self.cycles = 8
        pass

    def tick(self):\
    
        # Fetch read is ok, there's map route inside bus
        #opcode = self.bus.ram_read(self.registers.pc)
        opcode = self.instructions.fetch_opcode()
        
        # Decode
        decoded_data = self.instructions.decode(opcode, self.registers.pc)
        # Execute
        self.instructions.execute(decoded_data)

    def irq(self):
        pass

    def nmi(self):
        pass
