# Status flags
NEGATIVE  = 0x80  # N
OVERFLOW  = 0x40  # V
UNUSED    = 0x20  # -
BREAK     = 0x10  # B
DECIMAL   = 0x08  # D
INTERRUPT = 0x04  # I
ZERO      = 0x02  # Z
CARRY     = 0x01  # C

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

    def get_flag(self, flag):
        if flag == NEGATIVE:
            return self.N
        elif flag == OVERFLOW:
            return self.V
        elif flag == UNUSED:
            return self.U
        elif flag == BREAK:
            return self.B
        elif flag == DECIMAL:
            return self.D
        elif flag == INTERRUPT:
            return self.I
        elif flag == ZERO:
            return self.Z
        elif flag == CARRY:
            return self.C
        return 0

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