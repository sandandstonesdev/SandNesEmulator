from emulator.board.interrupt_info import InterruptInfo
from emulator.cpu.status_flags import INTERRUPT
from emulator.cpu.instruction_processor import InstructionProcessor
from emulator.cpu.registers import Registers
from emulator.board.bus import Bus

class CPU:
    def __init__(self, bus: Bus, interrupt_info: InterruptInfo):
        self.bus = bus
        self.interrupt_info = interrupt_info
        self.registers = Registers(bus)
        self.instructions= InstructionProcessor(self.registers, self.bus)
        pass

    def power_on(self):
        self.reset()
        pass

    def reset(self):
        self.interrupt_info.reset_interrupt.requested = True
        self.cycles = 8
        pass

    def tick(self):
        # NMI Requested is set by PPU Module amd checked by CPU
        # IRQ Requested - the same
        if self.interrupt_info.reset_interrupt.requested:
            self.instructions.reset()
            self.interrupt_info.reset_interrupt.requested = False


        opcode = self.instructions.fetch_opcode()
        
        decoded_data = self.instructions.decode(opcode, self.registers.pc - 1)
        
        self.instructions.execute(decoded_data)

        nmi_interrupt = self.interrupt_info.nmi_interrupt
        irq_interrupt = self.interrupt_info.irq_interrupt

        if nmi_interrupt.requested:
            self.instructions.nmi()
            nmi_interrupt.requested = False

        if irq_interrupt.requested and \
                 irq_interrupt.is_enabled() and \
                 not self.registers.get_flag(INTERRUPT) and \
                 not irq_interrupt.is_pending():
            self.instructions.irq()
            irq_interrupt.requested = False