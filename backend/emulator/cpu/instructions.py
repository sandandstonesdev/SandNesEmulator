from emulator.cpu.registers import Registers
from emulator.cpu.decoded_data_dto import DecodedDataDTO
from emulator.cpu.opcodes import opcode_lookup

class ExecutionUnit:
    def __init__(self, registers: Registers):
        self.registers = registers

    def decode(self, opcode: int, current_pc: int):
        opcode_details = opcode_lookup[opcode]
        return DecodedDataDTO(
            current_pc=current_pc,
            addr_mode=opcode_details['addr_mode'],
            cycles=opcode_details['cycles'],
            mnemonic=opcode_details['mnemonic'],
            length=opcode_details['length'],
            prg_bytes=[]
        )
        
    def execute(self, decoded_data: DecodedDataDTO):
        exec_func = getattr(self, decoded_data.mnemonic, None)
        if exec_func:
            exec_func(decoded_data)
        else:
            pass  # or handle unknown instruction
        

    #Arithmetic/Logic:
    def ADC(self, decoded_data: DecodedDataDTO):
        pass

    def SBC(self, decoded_data: DecodedDataDTO):
        pass

    def AND(self, decoded_data: DecodedDataDTO):
        pass

    def ORA(self, decoded_data: DecodedDataDTO):
        pass

    def EOR(self, decoded_data: DecodedDataDTO):
        pass

    def CMP(self, decoded_data: DecodedDataDTO):
        pass

    def CPX(self, decoded_data: DecodedDataDTO):
        pass

    def CPY(self, decoded_data: DecodedDataDTO):
        pass

    def BIT(self, decoded_data: DecodedDataDTO):
        pass

    # Shifts/Rotates:
    def ASL(self, decoded_data: DecodedDataDTO):
        pass

    def LSR(self, decoded_data: DecodedDataDTO):
        pass

    def ROL(self, decoded_data: DecodedDataDTO):
        pass

    def ROR(self, decoded_data: DecodedDataDTO):
        pass


    # Registers/Transfer:
    def LDA(self, decoded_data: DecodedDataDTO):
        pass

    def LDX(self, decoded_data: DecodedDataDTO):
        pass

    def LDY(self, decoded_data: DecodedDataDTO):
        pass

    def STA(self, decoded_data: DecodedDataDTO):
        pass

    def STX(self, decoded_data: DecodedDataDTO):
        pass

    def STY(self, decoded_data: DecodedDataDTO):
        pass
    def TAX(self, decoded_data: DecodedDataDTO):
        pass

    def TXA(self, decoded_data: DecodedDataDTO):
        pass

    def TAY(self, decoded_data: DecodedDataDTO):
        pass

    def TYA(self, decoded_data: DecodedDataDTO):
        pass

    def TSX(self, decoded_data: DecodedDataDTO):
        pass

    def TXS(self, decoded_data: DecodedDataDTO):
        pass

    #Stack:
    def PHA(self, decoded_data: DecodedDataDTO):
        pass

    def PLA(self, decoded_data: DecodedDataDTO):
        pass

    def PHP(self, decoded_data: DecodedDataDTO):
        pass

    def PLP(self, decoded_data: DecodedDataDTO):
        pass

    #Increment/Decrement:
    def INC(self, decoded_data: DecodedDataDTO):
        pass

    def INX(self, decoded_data: DecodedDataDTO):
        pass

    def INY(self, decoded_data: DecodedDataDTO):
        pass

    def DEC(self, decoded_data: DecodedDataDTO):
        pass

    def DEX(self, decoded_data: DecodedDataDTO):
        pass

    def DEY(self, decoded_data: DecodedDataDTO):
        pass


    # Branch/Jump:
    def JMP(self, decoded_data: DecodedDataDTO):
        pass

    def JSR(self, decoded_data: DecodedDataDTO):
        pass

    def RTS(self, decoded_data: DecodedDataDTO):
        pass

    def RTI(self, decoded_data: DecodedDataDTO):
        pass

    def BCC(self, decoded_data: DecodedDataDTO):
        pass

    def BCS(self, decoded_data: DecodedDataDTO):
        pass

    def BEQ(self, decoded_data: DecodedDataDTO):
        pass

    def BMI(self, decoded_data: DecodedDataDTO):
        pass

    def BNE(self, decoded_data: DecodedDataDTO):
        pass

    def BPL(self, decoded_data: DecodedDataDTO):
        pass

    def BVC(self, decoded_data: DecodedDataDTO):
        pass

    def BVS(self, decoded_data: DecodedDataDTO):
        pass

    #Flags:
    def CLC(self, decoded_data: DecodedDataDTO):
        pass

    def SEC(self, decoded_data: DecodedDataDTO):
        pass

    def CLD(self, decoded_data: DecodedDataDTO):
        pass

    def SED(self, decoded_data: DecodedDataDTO):
        pass

    def CLI(self, decoded_data: DecodedDataDTO):
        pass

    def SEI(self, decoded_data: DecodedDataDTO):
        pass

    def CLV(self, decoded_data: DecodedDataDTO):
        pass

    # NOPs:
    def NOP(self, decoded_data: DecodedDataDTO):
        pass

    # Undocumented/Illegal:
    def SLO(self, decoded_data: DecodedDataDTO):
        pass

    def RLA(self, decoded_data: DecodedDataDTO):
        pass

    def SRE(self, decoded_data: DecodedDataDTO):
        pass

    def RRA(self, decoded_data: DecodedDataDTO):
        pass

    def SAX(self, decoded_data: DecodedDataDTO):
        pass

    def LAX(self, decoded_data: DecodedDataDTO):
        pass

    def DCP(self, decoded_data: DecodedDataDTO):
        pass

    def ISC(self, decoded_data: DecodedDataDTO):
        pass

    def ANC(self, decoded_data: DecodedDataDTO):
        pass

    def ALR(self, decoded_data: DecodedDataDTO):
        pass

    def ARR(self, decoded_data: DecodedDataDTO):
        pass

    def XAA(self, decoded_data: DecodedDataDTO):
        pass

    def TAS(self, decoded_data: DecodedDataDTO):
        pass

    def SHY(self, decoded_data: DecodedDataDTO):
        pass

    def SHX(self, decoded_data: DecodedDataDTO):
        pass

    def LAS(self, decoded_data: DecodedDataDTO):
        pass

    def AHX(self, decoded_data: DecodedDataDTO):
        pass

    def LXA(self, decoded_data: DecodedDataDTO):
        pass

    def AXS(self, decoded_data: DecodedDataDTO):
        pass

    def KIL(self, decoded_data: DecodedDataDTO):
        pass