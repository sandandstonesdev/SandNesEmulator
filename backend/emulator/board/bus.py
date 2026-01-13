from emulator.ppu.ppu_frame import PPUFrame
from emulator.mapping.base_mapping.default_map_router import DefaultMapRouter
from emulator.mapping.cpu_mapping.cpu_space_mapping import CPUSpaceMapping
from emulator.apu.apu import APU
from emulator.cartridge.cartridge import Cartridge
from emulator.joypad import Joypad
from emulator.ppu.ppu import PPU
from emulator.ram import RAM


class Bus:
    def __init__(self,
                 ppu: PPU,
                 apu: APU,
                 cartridge: Cartridge,
                 ram: RAM,
                 joypad:Joypad,
                 cpu_map_router: DefaultMapRouter):
        self.ppu = ppu
        self.apu = apu
        self.cartridge = cartridge
        self.ram = ram
        self.joypad = joypad
        self.cpu_map_router = cpu_map_router
        self.master_clock = 0
        
    def read_double_byte(self, address):
        low_byte = self.read(address)
        high_byte = self.read(address + 1)
        return (high_byte << 8) | low_byte

    def read(self, address):
        mapped_space = self.cpu_map_router.route_read(address)
        if mapped_space == CPUSpaceMapping.CARTRIDGE_SPACE:
            return self.cartridge.read(address)
        elif mapped_space == CPUSpaceMapping.PPU_REGISTERS:
            return self.ppu.read_register(address)
        elif mapped_space == CPUSpaceMapping.APU_IO_REGISTERS:
            return self.apu.read_register(address)
        elif mapped_space == CPUSpaceMapping.JOYPAD1:
            return self.joypad.read(address)
        elif mapped_space == CPUSpaceMapping.JOYPAD2_NOT_SUPPORTED:
            return 0x00  # Not supported, return default
        elif mapped_space == CPUSpaceMapping.RAM_ZERO_PAGE:
            return self.ram.read_zp(address)
        elif mapped_space == CPUSpaceMapping.STACK:
            return self.ram.read_stack(address)
        elif mapped_space == CPUSpaceMapping.RAM_GENERAL_PURPOSE:
            return self.ram.read(address)
        return 0x00  # Default return for unmapped addresses

    def write(self, address, value):
        mapped_space = self.cpu_map_router.route_write(address, value)
        if mapped_space == CPUSpaceMapping.CARTRIDGE_SPACE:
            return self.cartridge.write_prg(address, value)
        elif mapped_space == CPUSpaceMapping.PPU_REGISTERS:
             return self.ppu.write_register(address, value)
        elif mapped_space == CPUSpaceMapping.APU_IO_REGISTERS:
            return self.apu.write_register(address, value)
        elif mapped_space == CPUSpaceMapping.JOYPAD1:
            return self.joypad.write(address, value)
        elif mapped_space == CPUSpaceMapping.RAM_ZERO_PAGE:
            return self.ram.write_zp(address, value)
        elif mapped_space == CPUSpaceMapping.RAMSTACK:
            return self.ram.write_stack(address, value)
        elif mapped_space == CPUSpaceMapping.RAM_GENERAL_PURPOSE:
            return self.ram.write(address, value)
            
    def insert_rom(self, rom_path: str):
        self.cartridge.insert_rom_file(rom_path=rom_path)
        # load appropriate CHR Bank to PPU according to selected bank in mapper

    def get_frame(self) -> PPUFrame:
        return self.ppu.output_frame()

    def update_controller(self, controller_state1):
        # On this layer we should have Joypad Byte
        self.joypad.update_state(controller_state1)