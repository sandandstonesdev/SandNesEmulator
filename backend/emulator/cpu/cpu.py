from emulator.cpu.status_flags import INTERRUPT
from emulator.cpu.instruction_processor import InstructionProcessor
from emulator.cpu.registers import Registers
from emulator.bus import Bus

class CPU:
    def __init__(self, bus: Bus):
        self.bus = bus
        self.registers = Registers(bus)
        self.instructions= InstructionProcessor(self.registers, self.bus)
        pass

    def power_on(self):
        self.reset()
        pass

    def reset(self):
        self.registers.reset()
        self.cycles = 8
        pass

    def tick(self):
        opcode = self.instructions.fetch_opcode()
        
        decoded_data = self.instructions.decode(opcode, self.registers.pc)
        
        self.instructions.execute(decoded_data)

    def irq(self):
        self.instructions.irq()

    def nmi(self):
        self.instructions.nmi()