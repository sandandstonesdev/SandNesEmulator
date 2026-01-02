from emulator.board.bus import Bus


class Stack:
    def __init__(self, bus: Bus):
        self.bus = bus
        self.pointer = 0xFF

    def push(self, value):
        self.bus.ram_write(0x0100 + self.pointer, value)
        self.pointer -= 1

    def pop(self):
        if self.pointer < 0xFF:
            self.pointer += 1
            return self.bus.ram_read(0x0100 + self.pointer)
        else:
            raise IndexError("Pop from empty stack")

    def reset(self):
        self.pointer = 0xFF