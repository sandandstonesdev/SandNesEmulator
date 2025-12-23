# Status flags
NEGATIVE = 0x80  # N
OVERFLOW = 0x40  # V
UNUSED   = 0x20  # -
BREAK    = 0x10  # B
DECIMAL  = 0x08  # D
INTERRUPT= 0x04  # I
ZERO     = 0x02  # Z
CARRY    = 0x01  # C

class StatusFlags:
    def __init__(self):
        self.N = 0  # Negative
        self.V = 0  # Overflow
        self.U = 1  # Unused
        self.B = 0  # Break
        self.D = 0  # Decimal
        self.I = 0  # Interrupt Disable
        self.Z = 0  # Zero
        self.C = 0  # Carry

    def set_flag(self, flag, value):
        if flag == NEGATIVE:
            self.N = value
        elif flag == OVERFLOW:
            self.V = value
        elif flag == UNUSED:
            pass
            # self.U = value
        elif flag == BREAK:
            self.B = value
        elif flag == DECIMAL:
            pass
            # self.D = value
        elif flag == INTERRUPT:
            self.I = value
        elif flag == ZERO:
            self.Z = value
        elif flag == CARRY:
            self.C = value

    def to_byte(self):
        return (
            (self.N << 7)
            | (self.V << 6)
            | (self.U << 5)
            | (self.B << 4)
            | (self.D << 3)
            | (self.I << 2)
            | (self.Z << 1)
            | self.C
        )

# Stack
class Stack:
    def __init__(self):
        self.stack = []
        self.pointer = 0xFF

    def push(self, value):
        self.stack.append(value)
        self.pointer -= 1

    def pop(self):
        if self.stack:
            self.pointer += 1
            return self.stack.pop()
        else:
            raise IndexError("Pop from empty stack")