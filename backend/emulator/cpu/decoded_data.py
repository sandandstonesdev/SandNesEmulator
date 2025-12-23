class DecodedData:
    def __init__(self,
                 current_pc: int,
                 opcode_details: dict):
        
        self.current_pc = current_pc
        self.addr_mode = opcode_details['addr_mode']
        self.cycles = opcode_details['cycles']
        self.mnemonic = opcode_details['mnemonic']
        self.length = opcode_details['length']
        self.operand_byte_count = self.length - 1
        operands = []
        if (self.operand_byte_count == 1):
            operands.append(self.bus.read_prg(current_pc + 1))

        if (self.operand_byte_count == 2):
            operands.append(self.bus.read_prg(current_pc + 2))

        self.operands = operands