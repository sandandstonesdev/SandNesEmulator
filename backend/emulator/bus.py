from backend.emulator.apu import APU
from backend.emulator.cartridge import Cartridge
from backend.emulator.joypad import Joypad
from backend.emulator.mapper import Mapper
from backend.emulator.ppu import PPU
from backend.emulator.ram import RAM


class Bus:
    def __init__(self, 
                 ppu: PPU,
                 apu: APU,
                 cartridge: Cartridge,
                 ram: RAM,
                 joypad:Joypad):
        self.ppu = ppu
        self.apu = apu
        self.cartridge = cartridge
        self.ram = ram
        self.joypad = joypad
        
    def ram_read(self, address):
        return self.ram.read(address)

    def ram_write(self, address, value):
        self.ram.write(address, value)

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

    def joypad_read(self, address):
        pass