from backend.emulator.cpu.cpu import CPU, Registers
from backend.emulator.cpu.decoded_data import DecodedData
from backend.emulator.cpu.opcodes import opcode_lookup


class ExecutionUnit:
    def __init__(self, registers: Registers):
        self.registers = registers

    def decode(self, opcode: int, current_pc: int):
        opcode_details = opcode_lookup[opcode]
        return DecodedData(current_pc, opcode_details)
        
    def execute(self, decoded_data: DecodedData):
        exec_func = getattr(self, decoded_data.mnemonic, None)
        if exec_func:
            exec_func(decoded_data)
        else:
            pass  # or handle unknown instruction
        

    #Arithmetic/Logic:
    def ADC(self, decoded_data: DecodedData):
        pass

    def SBC(self, decoded_data: DecodedData):
        pass

    def AND(self, decoded_data: DecodedData):
        pass

    def ORA(self, decoded_data: DecodedData):
        pass

    def EOR(self, decoded_data: DecodedData):
        pass

    def CMP(self, decoded_data: DecodedData):
        pass

    def CPX(self, decoded_data: DecodedData):
        pass

    def CPY(self, decoded_data: DecodedData):
        pass

    def BIT(self, decoded_data: DecodedData):
        pass

    # Shifts/Rotates:
    def ASL(self, decoded_data: DecodedData):
        pass

    def LSR(self, decoded_data: DecodedData):
        pass

    def ROL(self, decoded_data: DecodedData):
        pass

    def ROR(self, decoded_data: DecodedData):
        pass


    # Registers/Transfer:
    def LDA(self, decoded_data: DecodedData):
        pass

    def LDX(self, decoded_data: DecodedData):
        pass

    def LDY(self, decoded_data: DecodedData):
        pass

    def STA(self, decoded_data: DecodedData):
        pass

    def STX(self, decoded_data: DecodedData):
        pass

    def STY(self, decoded_data: DecodedData):
        pass
    def TAX(self, decoded_data: DecodedData):
        pass

    def TXA(self, decoded_data: DecodedData):
        pass

    def TAY(self, decoded_data: DecodedData):
        pass

    def TYA(self, decoded_data: DecodedData):
        pass

    def TSX(self, decoded_data: DecodedData):
        pass

    def TXS(self, decoded_data: DecodedData):
        pass

    #Stack:
    def PHA(self, decoded_data: DecodedData):
        pass

    def PLA(self, decoded_data: DecodedData):
        pass

    def PHP(self, decoded_data: DecodedData):
        pass

    def PLP(self, decoded_data: DecodedData):
        pass

    #Increment/Decrement:
    def INC(self, decoded_data: DecodedData):
        pass

    def INX(self, decoded_data: DecodedData):
        pass

    def INY(self, decoded_data: DecodedData):
        pass

    def DEC(self, decoded_data: DecodedData):
        pass

    def DEX(self, decoded_data: DecodedData):
        pass

    def DEY(self, decoded_data: DecodedData):
        pass


    # Branch/Jump:
    def JMP(self, decoded_data: DecodedData):
        pass

    def JSR(self, decoded_data: DecodedData):
        pass

    def RTS(self, decoded_data: DecodedData):
        pass

    def RTI(self, decoded_data: DecodedData):
        pass

    def BCC(self, decoded_data: DecodedData):
        pass

    def BCS(self, decoded_data: DecodedData):
        pass

    def BEQ(self, decoded_data: DecodedData):
        pass

    def BMI(self, decoded_data: DecodedData):
        pass

    def BNE(self, decoded_data: DecodedData):
        pass

    def BPL(self, decoded_data: DecodedData):
        pass

    def BVC(self, decoded_data: DecodedData):
        pass

    def BVS(self, decoded_data: DecodedData):
        pass

    #Flags:
    def CLC(self, decoded_data: DecodedData):
        pass

    def SEC(self, decoded_data: DecodedData):
        pass

    def CLD(self, decoded_data: DecodedData):
        pass

    def SED(self, decoded_data: DecodedData):
        pass

    def CLI(self, decoded_data: DecodedData):
        pass

    def SEI(self, decoded_data: DecodedData):
        pass

    def CLV(self, decoded_data: DecodedData):
        pass

    # NOPs:
    def NOP(self, decoded_data: DecodedData):
        pass

    # Undocumented/Illegal:
    def SLO(self, decoded_data: DecodedData):
        pass

    def RLA(self, decoded_data: DecodedData):
        pass

    def SRE(self, decoded_data: DecodedData):
        pass

    def RRA(self, decoded_data: DecodedData):
        pass

    def SAX(self, decoded_data: DecodedData):
        pass

    def LAX(self, decoded_data: DecodedData):
        pass

    def DCP(self, decoded_data: DecodedData):
        pass

    def ISC(self, decoded_data: DecodedData):
        pass

    def ANC(self, decoded_data: DecodedData):
        pass

    def ALR(self, decoded_data: DecodedData):
        pass

    def ARR(self, decoded_data: DecodedData):
        pass

    def XAA(self, decoded_data: DecodedData):
        pass

    def TAS(self, decoded_data: DecodedData):
        pass

    def SHY(self, decoded_data: DecodedData):
        pass

    def SHX(self, decoded_data: DecodedData):
        pass

    def LAS(self, decoded_data: DecodedData):
        pass

    def AHX(self, decoded_data: DecodedData):
        pass

    def LXA(self, decoded_data: DecodedData):
        pass

    def AXS(self, decoded_data: DecodedData):
        pass

    def KIL(self, decoded_data: DecodedData):
        pass