from emulator.board.reset_interrupt import ResetInterrupt
from emulator.board.irq_interrpupt import IRQInterrupt
from emulator.board.nmi_interrupt import NMIInterrupt


class InterruptInfo:
    def __init__(self):
        self._nmi_interrupt = NMIInterrupt()
        self._irq_interrupt = IRQInterrupt()
        self._reset_interrupt = ResetInterrupt()
    
    @property
    def nmi_interrupt(self):
        return self._nmi_interrupt
    
    @property
    def irq_interrupt(self):
        return self._irq_interrupt
    
    @property
    def reset_interrupt(self):
        return self._reset_interrupt