from emulator.board.bus import Bus
from emulator.cpu.registers import Registers
from emulator.cpu.decoded_data_dto import DecodedDataDTO

class AddrOps:
    def __init__(self, registers: Registers, bus: Bus):
        self.registers = registers
        self.bus = bus

    def fetch_opcode_op(self):
            opcode = self.bus.ram_read(self.registers.pc)
            self.registers.pc += 1
            self.registers.cycles += 1
            return opcode

    def operand_fetch_op(self, decoded_data: DecodedDataDTO):
        if decoded_data.addr_mode == 'IMM':
            self.registers.adl = self.registers.pc
            self.registers.adh = 0
            self.registers.d = self.bus.read(self.registers.adl)
            self.registers.pc += 1
            self.registers.cycles += 1
        elif decoded_data.addr_mode == 'ZP':
            self.registers.adl = self.bus.ram_read(self.registers.pc)
            self.registers.adh = 0
            addr = (self.registers.adh << 8) | self.registers.adl
            self.registers.d = self.bus.ram_read(addr)
            self.registers.pc += 1
            self.registers.cycles += 1
        elif decoded_data.addr_mode == 'ZPX':
            zp_addr = (self.bus.ram_read(self.registers.pc) + self.registers.x) & 0xFF
            self.registers.adl = zp_addr
            self.registers.adh = 0
            addr = (self.registers.adh << 8) | self.registers.adl
            self.registers.d = self.bus.ram_read(addr)
            self.registers.pc += 1
            self.registers.cycles += 1
        elif decoded_data.addr_mode == 'ABS':
            self.registers.adl = self.bus.ram_read(self.registers.pc)
            self.registers.adh = self.bus.ram_read(self.registers.pc + 1)
            addr = (self.registers.adh << 8) | self.registers.adl
            self.registers.d = self.bus.ram_read(addr)
            self.registers.pc += 2
            self.registers.cycles += 1
        elif decoded_data.addr_mode == 'ABSX':
            low = self.bus.ram_read(self.registers.pc)
            high = self.bus.ram_read(self.registers.pc + 1)
            addr = ((high << 8) | low) + self.registers.x
            self.registers.adl = addr & 0xFF
            self.registers.adh = (addr >> 8) & 0xFF
            self.registers.d = self.bus.ram_read((self.registers.adh << 8) | self.registers.adl)
            self.registers.pc += 2
            self.registers.cycles += 1
        elif decoded_data.addr_mode == 'ABSY':
            low = self.bus.ram_read(self.registers.pc)
            high = self.bus.ram_read(self.registers.pc + 1)
            addr = ((high << 8) | low) + self.registers.y
            self.registers.adl = addr & 0xFF
            self.registers.adh = (addr >> 8) & 0xFF
            self.registers.d = self.bus.ram_read((self.registers.adh << 8) | self.registers.adl)
            self.registers.pc += 2
            self.registers.cycles += 1
        elif decoded_data.addr_mode == 'IZX':
            zp_ptr = (self.bus.ram_read(self.registers.pc) + self.registers.x) & 0xFF
            low = self.bus.ram_read(zp_ptr)
            high = self.bus.ram_read((zp_ptr + 1) & 0xFF)
            self.registers.adl = low
            self.registers.adh = high
            addr = (self.registers.adh << 8) | self.registers.adl
            self.registers.d = self.bus.ram_read(addr)
            self.registers.pc += 1
            self.registers.cycles += 1
        elif decoded_data.addr_mode == 'IZY':
            zp_ptr = self.bus.ram_read(self.registers.pc)
            low = self.bus.ram_read(zp_ptr)
            high = self.bus.ram_read((zp_ptr + 1) & 0xFF)
            addr = ((high << 8) | low) + self.registers.y
            self.registers.adl = addr & 0xFF
            self.registers.adh = (addr >> 8) & 0xFF
            self.registers.d = self.bus.ram_read((self.registers.adh << 8) | self.registers.adl)
            self.registers.pc += 1
            self.registers.cycles += 1