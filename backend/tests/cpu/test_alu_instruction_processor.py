from emulator.cpu.instruction_processor import InstructionProcessor
from emulator.cpu.registers import Registers
from emulator.board.bus import Bus

class DummyBus(Bus):
    def __init__(self):
        self.memory = [0] * 0x10000
        self.ram = self
        self.ppu = self.apu = self.cartridge = self.joypad = self.memory_map_router = None
    def read(self, address):
        return self.memory[address]
    def write(self, address, value):
        self.memory[address] = value
    def read(self, address):
        return self.memory[address]
    def write(self, address, value):
        self.memory[address] = value

def make_processor():
    bus = DummyBus()
    # Set reset vector to 0x0000
    bus.memory[0xFFFC] = 0x00  # low byte
    bus.memory[0xFFFD] = 0x00  # high byte
    registers = Registers(bus)
    return InstructionProcessor(registers, bus), registers, bus

def test_adc_immediate():
    proc, regs, bus = make_processor()
    regs.a = 0x10
    regs.p.C = 1
    opcode = 0x69  # ADC immediate
    bus.memory[0x0000] = opcode
    bus.memory[0x0001] = 0x22
    regs.pc = 0x0000
    fetch_opcode_opcode = proc.fetch_opcode()
    assert fetch_opcode_opcode == opcode
    decoded = proc.decode(opcode, regs.pc)
    proc.addr_op.operand_fetch_op(decoded)
    proc.cpu_adc(decoded)
    assert regs.a == 0x33
    assert regs.p.C == 0
    assert regs.p.Z == 0
    assert regs.p.N == 0

def test_sbc():
    proc, regs, bus = make_processor()
    regs.a = 0x20
    regs.p.C = 1
    opcode = 0xE9  # SBC immediate
    bus.memory[0x0000] = opcode
    bus.memory[0x0001] = 0x10
    regs.pc = 0x0000
    fetch_opcode_opcode = proc.fetch_opcode()
    assert fetch_opcode_opcode == opcode
    decoded = proc.decode(opcode, regs.pc)
    proc.addr_op.operand_fetch_op(decoded)
    proc.cpu_sbc(decoded)
    assert regs.a == 0x10
    assert regs.p.C == 1
    assert regs.p.Z == 0
    assert regs.p.N == 0

def test_and_zero_flag():
    proc, regs, bus = make_processor()
    regs.a = 0x0F
    opcode = 0x29  # AND immediate
    bus.memory[0x0000] = opcode
    bus.memory[0x0001] = 0xF0
    regs.pc = 0x0000
    fetch_opcode_opcode = proc.fetch_opcode()
    assert fetch_opcode_opcode == opcode
    decoded = proc.decode(opcode, regs.pc)
    proc.addr_op.operand_fetch_op(decoded)
    proc.cpu_and(decoded)
    assert regs.a == 0x00
    assert regs.p.Z == 1
    assert regs.p.N == 0

def test_eor_negative_flag():
    proc, regs, bus = make_processor()
    regs.a = 0xF0
    opcode = 0x49  # EOR immediate
    bus.memory[0x0000] = opcode
    bus.memory[0x0001] = 0x0F
    regs.pc = 0x0000
    fetch_opcode_opcode = proc.fetch_opcode()
    assert fetch_opcode_opcode == opcode
    decoded = proc.decode(opcode, regs.pc)
    proc.addr_op.operand_fetch_op(decoded)
    proc.cpu_eor(decoded)
    assert regs.a == 0xFF
    assert regs.p.N == 1

def test_ora():
    proc, regs, bus = make_processor()
    regs.a = 0x10
    opcode = 0x09  # ORA immediate
    bus.memory[0x0000] = opcode
    bus.memory[0x0001] = 0x01
    regs.pc = 0x0000
    fetch_opcode_opcode = proc.fetch_opcode()
    assert fetch_opcode_opcode == opcode
    decoded = proc.decode(opcode, regs.pc)
    proc.addr_op.operand_fetch_op(decoded)
    proc.cpu_ora(decoded)
    assert regs.a == 0x11
    assert regs.p.Z == 0
    assert regs.p.N == 0
    
def test_inc():
    proc, regs, bus = make_processor()
    bus.memory[0x0010] = 0xFF
    opcode = 0xE6  # INC zero page
    bus.memory[0x0000] = opcode
    bus.memory[0x0001] = 0x10
    regs.pc = 0x0000
    fetch_opcode_opcode = proc.fetch_opcode()
    assert fetch_opcode_opcode == opcode
    decoded = proc.decode(opcode, regs.pc)
    proc.addr_op.operand_fetch_op(decoded)
    proc.cpu_inc(decoded)
    assert bus.memory[0x0010] == 0x00
    assert regs.p.Z == 1
    assert regs.p.N == 0

def test_dec():
    proc, regs, bus = make_processor()
    bus.memory[0x0020] = 0x01
    opcode = 0xC6  # DEC zero page
    bus.memory[0x0000] = opcode
    bus.memory[0x0001] = 0x20
    regs.pc = 0x0000
    fetch_opcode_opcode = proc.fetch_opcode()
    assert fetch_opcode_opcode == opcode
    decoded = proc.decode(opcode, regs.pc)
    proc.addr_op.operand_fetch_op(decoded)
    proc.cpu_dec(decoded)
    assert bus.memory[0x0020] == 0x00
    assert regs.p.Z == 1
    assert regs.p.N == 0

def test_inx():
    proc, regs, bus = make_processor()
    regs.x = 0xFF
    opcode = 0xE8  # INX
    bus.memory[0x0000] = opcode
    regs.pc = 0x0000
    fetch_opcode_opcode = proc.fetch_opcode()
    assert fetch_opcode_opcode == opcode
    decoded = proc.decode(opcode, regs.pc)
    proc.cpu_inx(decoded)
    assert regs.x == 0x00
    assert regs.p.Z == 1
    assert regs.p.N == 0

def test_dex():
    proc, regs, bus = make_processor()
    regs.x = 0x01
    opcode = 0xCA  # DEX
    bus.memory[0x0000] = opcode
    regs.pc = 0x0000
    fetch_opcode_opcode = proc.fetch_opcode()
    assert fetch_opcode_opcode == opcode
    decoded = proc.decode(opcode, regs.pc)
    proc.cpu_dex(decoded)
    assert regs.x == 0x00
    assert regs.p.Z == 1
    assert regs.p.N == 0

def test_iny():
    proc, regs, bus = make_processor()
    regs.y = 0xFF
    opcode = 0xC8  # INY
    bus.memory[0x0000] = opcode
    regs.pc = 0x0000
    fetch_opcode_opcode = proc.fetch_opcode()
    assert fetch_opcode_opcode == opcode
    decoded = proc.decode(opcode, regs.pc)
    proc.cpu_iny(decoded)
    assert regs.y == 0x00
    assert regs.p.Z == 1
    assert regs.p.N == 0

def test_dey():
    proc, regs, bus = make_processor()
    regs.y = 0x01
    opcode = 0x88  # DEY
    bus.memory[0x0000] = opcode
    regs.pc = 0x0000
    fetch_opcode_opcode = proc.fetch_opcode()
    assert fetch_opcode_opcode == opcode
    decoded = proc.decode(opcode, regs.pc)
    proc.cpu_dey(decoded)
    assert regs.y == 0x00
    assert regs.p.Z == 1
    assert regs.p.N == 0