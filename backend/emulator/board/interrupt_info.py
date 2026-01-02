from emulator.board.irq_interrpupt import IRQInterrupt
from emulator.board.nmi_interrupt import NMIInterrupt


class InterruptInfo:
    def __init__(self):
        self._nmi_interrupt = NMIInterrupt()
        self._irq_interrupt = IRQInterrupt()
    
    @property
    def nmi_interrupt(self):
        return self._nmi_interrupt
    
    @property
    def irq_interrupt(self):
        return self._irq_interrupt