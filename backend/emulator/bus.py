from emulator.apu import APU
from emulator.cartridge import Cartridge
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
                 MemoryMapRouter: MemoryMapRouter):
        self.ppu = ppu
        self.apu = apu
        self.cartridge = cartridge
        self.ram = ram
        self.joypad = joypad
        self.memory_map_router = MemoryMapRouter
        
    def ram_read(self, address):
        # Read routing
        # Cart capture
        # PPU capture
        # APU capture
        # Joypad capture
        # RAM access capture

        return self.ram.read(address)

    def ram_write(self, address, value):
        # Write routing capture
        self.ram.write(address, value)

   # All below should be private - used by router and consider mapper

    def read_chr(self, address):
        # Use mapper to map address
        return self.cartridge.read_chr(address)

    def read_prg(self, address):
        # Use mapper to map address
        return self.cartridge.read_prg(address) 

    def ppu_read(self, address):
        return self.ppu.read(address)

    def ppu_write(self, address, value):
        self.ppu.write(address, value)

    def apu_read(self, address):
        return self.apu.read(address)

    def apu_write(self, address, value):
        self.apu.write(address, value)

    def prg_write(self, address, value):
        self.cartridge.write_prg(address, value)

    def prg_read(self, address):
        return self.cartridge.read_prg(address)

    def joypad_read(self, address):
        pass