
from emulator.board.interrupt_base import InterruptBase

class ResetInterrupt(InterruptBase):
    def __init__(self):
        super().__init__()