from emulator.cpu.instruction_processor import InstructionProcessor
from emulator.cpu.registers import Registers
from emulator.bus import Bus

class DummyBus(Bus):
    def __init__(self):
        self.memory = [0] * 0x10000
        self.ram = self
        self.ppu = self.apu = self.cartridge = self.joypad = self.memory_map_router = None
    def ram_read(self, address):
        return self.memory[address]
    def ram_write(self, address, value):
        self.memory[address] = value
    def read(self, address):
        return self.memory[address]
    def write(self, address, value):
        self.memory[address] = value

def make_processor():
    bus = DummyBus()
    registers = Registers(bus)
    return InstructionProcessor(registers, bus), registers, bus

def test_lda():
    proc, regs, bus = make_processor()
    opcode = 0xA9  # LDA immediate
    bus.memory[0x0000] = opcode
    bus.memory[0x0001] = 0x42
    regs.pc = 0x0000
    fetch_opcode_opcode = proc.fetch_opcode()
    assert fetch_opcode_opcode == opcode
    decoded = proc.decode(opcode, regs.pc)
    proc.addr_op.operand_fetch_op(decoded)
    proc.cpu_lda(decoded)
    assert regs.a == 0x42
    assert regs.p.Z == 0
    assert regs.p.N == 0

def test_ldx():
    proc, regs, bus = make_processor()
    opcode = 0xA2  # LDX immediate
    bus.memory[0x0000] = opcode
    bus.memory[0x0001] = 0x37
    regs.pc = 0x0000
    fetch_opcode_opcode = proc.fetch_opcode()
    assert fetch_opcode_opcode == opcode
    decoded = proc.decode(opcode, regs.pc)
    proc.addr_op.operand_fetch_op(decoded)
    proc.cpu_ldx(decoded)
    assert regs.x == 0x37
    assert regs.p.Z == 0
    assert regs.p.N == 0

def test_ldy():
    proc, regs, bus = make_processor()
    opcode = 0xA0  # LDY immediate
    bus.memory[0x0000] = opcode
    bus.memory[0x0001] = 0x7F
    regs.pc = 0x0000
    fetch_opcode_opcode = proc.fetch_opcode()
    assert fetch_opcode_opcode == opcode
    decoded = proc.decode(opcode, regs.pc)
    proc.addr_op.operand_fetch_op(decoded)
    proc.cpu_ldy(decoded)
    assert regs.y == 0x7F
    assert regs.p.Z == 0
    assert regs.p.N == 0

def test_sta():
    proc, regs, bus = make_processor()
    regs.a = 0x55
    opcode = 0x8D  # STA absolute
    bus.memory[0x0000] = opcode
    bus.memory[0x0001] = 0x00  # Low byte of address
    bus.memory[0x0002] = 0x80  # High byte of address
    regs.pc = 0x0000
    fetch_opcode_opcode = proc.fetch_opcode()
    assert fetch_opcode_opcode == opcode
    decoded = proc.decode(opcode, regs.pc)
    proc.addr_op.operand_fetch_op(decoded)
    proc.cpu_sta(decoded)
    assert bus.memory[0x8000] == 0x55

def test_stx():
    proc, regs, bus = make_processor()
    regs.x = 0xAA
    opcode = 0x8E  # STX absolute
    bus.memory[0x0000] = opcode
    bus.memory[0x0001] = 0x10  # Low byte of address
    bus.memory[0x0002] = 0x80  # High byte of address
    regs.pc = 0x0000
    fetch_opcode_opcode = proc.fetch_opcode()
    assert fetch_opcode_opcode == opcode
    decoded = proc.decode(opcode, regs.pc)
    proc.addr_op.operand_fetch_op(decoded)
    proc.cpu_stx(decoded)
    assert bus.memory[0x8010] == 0xAA

def test_sty():
    proc, regs, bus = make_processor()
    regs.y = 0xFF
    opcode = 0x8C  # STY absolute
    bus.memory[0x0000] = opcode
    bus.memory[0x0001] = 0x20  # Low byte of address
    bus.memory[0x0002] = 0x80  # High byte of address
    regs.pc = 0x0000
    fetch_opcode_opcode = proc.fetch_opcode()
    assert fetch_opcode_opcode == opcode
    decoded = proc.decode(opcode, regs.pc)
    proc.addr_op.operand_fetch_op(decoded)
    proc.cpu_sty(decoded)
    assert bus.memory[0x8020] == 0xFF
    