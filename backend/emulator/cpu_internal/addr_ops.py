from emulator.board.bus import Bus
from emulator.cpu.registers import Registers
from emulator.cpu.decoded_data_dto import DecodedDataDTO

class AddrOps:
    def __init__(self, registers: Registers, bus: Bus):
        self.registers = registers
        self.bus = bus

    def fetch_opcode_op(self):
            opcode = self.bus.read(self.registers.pc)
            self.registers.inc_pc()
            self.registers.inc_cycles(1)
            return opcode

    # Get operand location by mode
    def operand_fetch_op(self, decoded_data: DecodedDataDTO):
        if decoded_data.addr_mode == 'IMM':
            self.registers.set_addr(0, self.registers.pc)
            self.registers.data = self.bus.read(self.registers.pc)
            self.registers.inc_pc()
            self.registers.inc_cycles(1)
        elif decoded_data.addr_mode == 'ZP0':
            self.registers.set_addr(0, self.bus.read(self.registers.pc))
            addr =  self.registers.get_addr()
            self.registers.data = self.bus.read(addr)
            self.registers.inc_pc()
            self.registers.inc_cycles(1)
        elif decoded_data.addr_mode == 'ZPX':
            zp_addr = (self.bus.read(self.registers.pc) + self.registers.x) & 0xFF
            self.registers.set_addr(0, zp_addr)
            addr = self.registers.get_addr()
            self.registers.data = self.bus.read(addr)
            self.registers.inc_pc()
            self.registers.inc_cycles(1)
        elif decoded_data.addr_mode == 'ABS':
            self.registers.set_addr(self.bus.read(self.registers.pc + 1), self.bus.read(self.registers.pc))
            addr = self.registers.get_addr()
            self.registers.data = self.bus.read(addr)
            self.registers.inc_pc(2)
            self.registers.inc_cycles(1)
        elif decoded_data.addr_mode == 'ABSX':
            low = self.bus.read(self.registers.pc)
            high = self.bus.read(self.registers.pc + 1)
            addr = ((high << 8) | low) + self.registers.x
            self.registers.set_addr((addr >> 8) & 0xFF, addr & 0xFF)
            self.registers.data = self.bus.read(self.registers.get_addr())
            self.registers.inc_pc(2)
            self.registers.inc_cycles(1)
        elif decoded_data.addr_mode == 'ABSY':
            low = self.bus.read(self.registers.pc)
            high = self.bus.read(self.registers.pc + 1)
            addr = ((high << 8) | low) + self.registers.y
            self.registers.set_addr((addr >> 8) & 0xFF, addr & 0xFF)
            self.registers.data = self.bus.read(self.registers.get_addr())
            self.registers.inc_pc(2)
            self.registers.inc_cycles(1)
        elif decoded_data.addr_mode == 'IZX':
            zp_ptr = (self.bus.read(self.registers.pc) + self.registers.x) & 0xFF
            low = self.bus.read(zp_ptr)
            high = self.bus.read((zp_ptr + 1) & 0xFF)
            self.registers.set_addr(high, low)
            addr = self.registers.get_addr()
            self.registers.data = self.bus.read(addr)
            self.registers.inc_pc()
            self.registers.inc_cycles(1)
        elif decoded_data.addr_mode == 'IZY':
            zp_ptr = self.bus.read(self.registers.pc)
            low = self.bus.read(zp_ptr)
            high = self.bus.read((zp_ptr + 1) & 0xFF)
            addr = ((high << 8) | low) + self.registers.y
            self.registers.set_addr((addr >> 8) & 0xFF, addr & 0xFF)
            self.registers.data = self.bus.read(self.registers.get_addr())
            self.registers.inc_pc()
            self.registers.inc_cycles(1)

    def result_store_op(self, decoded_data: DecodedDataDTO):
        if decoded_data.addr_mode == 'ZP0':
            addr = self.registers.get_addr()
            self.bus.write(addr, self.registers.data)
            self.registers.inc_cycles(1)
        elif decoded_data.addr_mode == 'ZPX':
            addr = self.registers.get_addr()
            self.bus.write(addr, self.registers.data)
            self.registers.inc_cycles(1)
        elif decoded_data.addr_mode == 'ABS':
            addr = self.registers.get_addr()
            self.bus.write(addr, self.registers.data)
            self.registers.inc_cycles(1)
        elif decoded_data.addr_mode == 'ABSX':
            addr = self.registers.get_addr()
            self.bus.write(addr, self.registers.data)
            self.registers.inc_cycles(1)
        elif decoded_data.addr_mode == 'ABSY':
            addr = self.registers.get_addr()
            self.bus.write(addr, self.registers.data)
            self.registers.inc_cycles(1)
        elif decoded_data.addr_mode == 'IZX':
            addr = self.registers.get_addr()
            self.bus.write(addr, self.registers.data)
            self.registers.inc_cycles(1)
        elif decoded_data.addr_mode == 'IZY':
            addr = self.registers.get_addr()
            self.bus.write(addr, self.registers.data)
            self.registers.inc_cycles(1)