from emulator.board.interrupt_info import InterruptInfo


class APU:
    def __init__(self, interrupt_info: InterruptInfo):
        self.interrupt_info = interrupt_info

    def tick(self):
        pass