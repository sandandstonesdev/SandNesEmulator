from emulator.cpu.registers import Registers
from emulator.cpu.cpu import CPU
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
        self.memory_map_router = MemoryMapRouter()
        self.cartridge = Cartridge()
        
        self.cpu = CPU(self.bus)
        self.bus = Bus(self.ppu, self.apu, self.cartridge, self.ram, self.joypad, self.memory_map_router)
        self.bus.attach_cpu(self.cpu)

    def tick(self):
        # Note: CPU/PPU => 1/3
        self.bus.tick()
        self.master_clock += 1

    # Open NES ROM In GUI
    def insert_rom(self, cartridge):
        self.bus.insert_rom(cartridge)
        pass

    # On Power On Button in GUI
    def power_on(self):
        self.bus.power_on()

    # On Reset in GUI
    def reset(self):
        self.bus.reset()
    # Off Button in GUI
    def power_off(self):
        pass

    # Get Frame (batching in future)
    def get_frame(self):
        return self.bus.get_frame()

    # Input controller state from GUI
    def input_controller_state(self, controller_state):
        self.bus.input_controller_state(controller_state)