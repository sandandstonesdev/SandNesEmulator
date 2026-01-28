
from emulator.cpu_internal.load_store_ops import LoadStoreOps
from emulator.cpu.status_flags import INTERRUPT
from emulator.cpu_internal.opcode_lookup import OpcodeLookup
from emulator.cpu_internal.addr_ops import AddrOps
from emulator.cpu_internal.alu_ops import ALUOps
from emulator.board.bus import Bus
from emulator.cpu.registers import Registers
from emulator.cpu.decoded_data_dto import DecodedDataDTO


class InstructionProcessor:
    def __init__(self, registers: Registers, bus: Bus):
        self.registers = registers
        self.bus = bus
        self.addr_op = AddrOps(registers, bus)
        self.alu_ops = ALUOps(registers, self.addr_op)
        self.load_store_ops = LoadStoreOps(registers, bus, self.addr_op)
    
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
    
    def reset(self):
        self.registers.reset()

    def irq(self):
        self.registers.irq()


    def nmi(self):
        self.registers.nmi()

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

    # Load/Store:
    def cpu_lda(self, decoded_data: DecodedDataDTO):
        self.load_store_ops.lda_op(decoded_data)
        return True
    
    def cpu_ldx(self, decoded_data: DecodedDataDTO):
        self.load_store_ops.ldx_op(decoded_data)
        return True
    
    def cpu_ldy(self, decoded_data: DecodedDataDTO):
        self.load_store_ops.ldy_op(decoded_data)
        return True
    
    def cpu_sta(self, decoded_data: DecodedDataDTO):
        self.load_store_ops.sta_op(decoded_data)
        return True
    
    def cpu_stx(self, decoded_data: DecodedDataDTO):
        self.load_store_ops.stx_op(decoded_data)
        return True
    
    def cpu_sty(self, decoded_data: DecodedDataDTO):
        self.load_store_ops.sty_op(decoded_data)
        return True
    
    def cpu_inc(self, decoded_data: DecodedDataDTO):
        self.alu_ops.inc_op(decoded_data)
        return True
    
    def cpu_dec(self, decoded_data: DecodedDataDTO):
        self.alu_ops.dec_op(decoded_data)
        return True
    
    def cpu_inx(self, decoded_data: DecodedDataDTO):
        self.alu_ops.inx_op(decoded_data)
        return True
    
    def cpu_dex(self, decoded_data: DecodedDataDTO):
        self.alu_ops.dex_op(decoded_data)
        return True
    
    def cpu_iny(self, decoded_data: DecodedDataDTO):
        self.alu_ops.iny_op(decoded_data)
        return True
    
    def cpu_dey(self, decoded_data: DecodedDataDTO):
        self.alu_ops.dey_op(decoded_data)
        return True
    
