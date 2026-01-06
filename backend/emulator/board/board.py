from emulator.mapping.cpu_mapping.cpu_maps import CPU_READ_MAP, CPU_WRITE_MAP
from emulator.ppu.ppu_frame import PPUFrame
from emulator.mapping.base_mapping.default_map_router import DefaultMapRouter
from emulator.ppu.ppu_bus import PPUBus
from emulator.mapping.register_mapping.io_register_router import IORegisterRouter
from emulator.board.interrupt_info import InterruptInfo
from emulator.cpu.cpu import CPU
from emulator.apu.apu import APU
from emulator.board.bus import Bus
from emulator.cartridge.cartridge import Cartridge
from emulator.joypad import Joypad
from emulator.ppu.ppu import PPU
from emulator.ram import RAM


class Board:
    def __init__(self):
        self.master_clock = 0

        self.interrupt_info = InterruptInfo()
        self.io_register_router = IORegisterRouter()
        
        self.cartridge = Cartridge()

        self.ppu_bus = PPUBus(self.cartridge)
        self.ppu = PPU(self.ppu_bus, self.interrupt_info)

        self.cpu_map_router = DefaultMapRouter(read_space_map=CPU_READ_MAP, write_space_map=CPU_WRITE_MAP)
        
        self.ram = RAM()

        self.apu = APU(self.io_register_router, self.interrupt_info)
        self.joypad = Joypad(self.io_register_router)

        self.bus = Bus(self.ppu, self.apu, self.cartridge, self.ram, self.joypad, self.cpu_map_router)
        self.cpu = CPU(self.bus, self.interrupt_info)

    def tick(self):
        self.joypad.tick()
        # Note: CPU/PPU => 1/3
        self.cpu.tick()
        for _ in range(3):
            self.ppu.tick()
        
        self.apu.tick()
        
        self.master_clock += 1

    def power_on(self):
        self.cpu.power_on()

    def reset(self):
        self.cpu.reset()

    def power_off(self):
        pass

    def insert_rom(self, rpm_path):
        self.bus.insert_rom(rpm_path)
        pass

    def get_frame(self) -> PPUFrame:
        return self.bus.get_frame()

    def update_controller(self, controller_state1): # On this layer we should have Joypad Byte
        self.bus.update_controller(controller_state1)