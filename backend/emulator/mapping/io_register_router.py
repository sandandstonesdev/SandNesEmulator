from emulator.mapping.apu_registers_maps import APU_READ_MAP, APU_WRITE_MAP, APU_WRITE_MAP
from emulator.mapping.joypad_register_maps import JOYPAD_READ_MAP
from emulator.mapping.ppu_registers_maps import PPU_READ_MAP, PPU_WRITE_MAP


class IORegisterRouter:
    def __init__(self):
        self.read_joypad_map = JOYPAD_READ_MAP
        self.write_joypad_map = JOYPAD_READ_MAP

        self.read_ppu_map = PPU_READ_MAP
        self.write_ppu_map = PPU_WRITE_MAP

        self.read_apu_map = APU_READ_MAP
        self.write_apu_map = APU_WRITE_MAP

    def route_read(self, address: int) -> int:
        if address in self.read_joypad_map:
            return self.read_joypad_map[address]
        elif address in self.read_ppu_map:
            return self.read_ppu_map[address]
        elif address in self.read_apu_map:
            return self.read_apu_map[address]

    def route_write(self, address: int, value: int):
        if address in self.write_joypad_map:
            return self.write_joypad_map[address]
        elif address in self.write_ppu_map:
            return self.write_ppu_map[address]
        elif address in self.write_apu_map:
            return self.write_apu_map[address]