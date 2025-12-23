from backend.emulator.apu import APU
from backend.emulator.bus import Bus
from backend.emulator.cartridge import Cartridge
from backend.emulator.cpu.cpu import CPU
from backend.emulator.joypad import Joypad
from backend.emulator.mapper import Mapper
from backend.emulator.ppu import PPU
from backend.emulator.ram import RAM


class Board:
    cpu: CPU

    def __init__(self):
        self.master_clock = 0

        self.ram = RAM()
        self.cartridge = Cartridge()
        self.apu = APU()
        self.ppu = PPU()
        self.joypad = Joypad()

        self.bus = Bus(self.ppu, self.apu, self.cartridge, self.ram)
        
        self.cpu = CPU(self.bus)
        
        pass

    def tick(self):
        # Note: CPU/PPU => 1/3
        self.cpu.tick()
        self.ppu.tick()
        self.apu.tick()

    # Open NES ROM In GUI
    def insert_cartridge(self, cartridge):
        cartridge.insert(rom_path="")
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