from emulator.apu import APU
from emulator.cartridge.cartridge import Cartridge
from emulator.joypad import Joypad
from emulator.mapping.memory_map_router import MemoryMapRouter
from emulator.ppu import PPU
from emulator.ram import RAM


class Bus:
    def __init__(self, 
                 ppu: PPU,
                 apu: APU,
                 cartridge: Cartridge,
                 ram: RAM,
                 joypad:Joypad,
                 memoryMapRouter: MemoryMapRouter):
        self.ppu = ppu
        self.apu = apu
        self.cartridge = cartridge
        self.ram = ram
        self.joypad = joypad
        self.memory_map_router = memoryMapRouter
        
    def ram_read(self, address):
        mapped_device = self.memory_map_router.route_read(address)
        if mapped_device == 'CARTRIDGE_SPACE':
            return self.cartridge.read_prg(address)
        elif mapped_device == 'PPU_REGISTERS':
            return self.ppu.read(address)
        elif mapped_device == 'APU_IO_REGISTERS':
            return self.apu.read(address)
        elif mapped_device == 'JOYPAD':
            return self.joypad.read(address)

        return self.ram.read(address)

    def ram_write(self, address, value):
        mapped_device = self.memory_map_router.route_write(address, value)
        if mapped_device == 'CARTRIDGE_SPACE':
            return self.cartridge.write_prg(address, value)
        elif mapped_device == 'PPU_REGISTERS':
             return self.ppu.write(address, value)
        elif mapped_device == 'APU_IO_REGISTERS':
            return self.apu.write(address, value)
        elif mapped_device == 'JOYPAD':
            return self.joypad.write(address, value)
        
        return self.ram.write(address, value)