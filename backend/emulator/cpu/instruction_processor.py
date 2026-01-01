
from emulator.cpu_internal.opcode_lookup import OpcodeLookup
from emulator.cpu_internal.addr_ops import AddrOps
from emulator.cpu_internal.alu_ops import ALUOps
from emulator.bus import Bus
from emulator.cpu.registers import Registers
from emulator.cpu.decoded_data_dto import DecodedDataDTO


class InstructionProcessor:
    def __init__(self, registers: Registers, bus: Bus):
        self.registers = registers
        self.bus = bus
        self.addr_op = AddrOps(registers, bus)
        self.alu_ops = ALUOps(registers, bus)
    
    def fetch_opcode(self):
        return self.addr_op.fetch_opcode_op()

    def decode(self, opcode: int, current_pc: int):
        opcode_details = OpcodeLookup[opcode]
        return DecodedDataDTO(
            current_pc=current_pc,
            addr_mode=opcode_details['addr_mode'],
            cycles=opcode_details['cycles'],
            mnemonic=opcode_details['mnemonic'],
            length=opcode_details['length'],
            type=opcode_details['type']
        )
        
    def execute(self, decoded_data: DecodedDataDTO):
        self.addr_op.operand_fetch_op(decoded_data)
        exec_func = getattr(self, decoded_data.mnemonic, None)
        if exec_func:
            exec_func(decoded_data)
        else:
            pass  # or handle unknown instruction
    
    #Arithmetic/Logic:
    def cpu_adc(self, decoded_data: DecodedDataDTO):
        self.alu_ops.adc_op(decoded_data)
        return True

    def cpu_sbc(self, decoded_data: DecodedDataDTO):
        self.alu_ops.sbc_op(decoded_data)
        return True
    
    def cpu_ora(self, decoded_data: DecodedDataDTO):
        self.alu_ops.ora_op(decoded_data)
        return True
    
    def cpu_and(self, decoded_data: DecodedDataDTO):
        self.alu_ops.and_op(decoded_data)
        return True
    
    def cpu_eor(self, decoded_data: DecodedDataDTO):
        self.alu_ops.eor_op(decoded_data)
        return True
