from emulator.cartridge.cartridge_map_router import CartridgeMapRouter
from emulator.cpu import CPU
from emulator.apu import APU
from emulator.bus import Bus
from emulator.cartridge.cartridge import Cartridge
from emulator.joypad import Joypad
from emulator.mapping.memory_map_router import MemoryMapRouter
from emulator.ppu import PPU
from emulator.ram import RAM


class Board:
    def __init__(self):
        self.master_clock = 0

        self.ram = RAM()
        self.apu = APU()
        self.ppu = PPU()
        self.joypad = Joypad()
        self.memory_mam_router = MemoryMapRouter()

        self.cartridge_map_router = CartridgeMapRouter()
        self.cartridge = Cartridge(self.cartridge_map_router)
        

        self.bus = Bus(self.ppu, self.apu, self.cartridge, self.ram, self.memory_mam_router)
        
        self.cpu = CPU(self.bus)
        
        pass

    def tick(self):
        # Note: CPU/PPU => 1/3
        self.cpu.tick()
        self.ppu.tick()
        self.apu.tick()

    # Open NES ROM In GUI
    def insert_cartridge(self, cartridge):
        cartridge.insert_rom_file(rom_path="")
        pass

    # On Power On Button in GUI
    def power_on(self):
        self.cpu.power_on()

    # On Reset in GUI
    def reset(self):
        self.cpu.reset()

    # Off Button in GUI
    def power_off(self):
        pass

    # Get Frame (batching in future)
    def get_frame(self):
        return self.ppu.get_frame()

    # Input controller state from GUI
    def input_controller_state(self, controller_state):
        self.joypad.update_state(controller_state)