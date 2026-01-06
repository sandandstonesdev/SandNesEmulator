from emulator.mapping.ppu_mapping.ppu_maps import PPU_READ_MAP, PPU_WRITE_MAP
from emulator.mapping.base_mapping.default_map_router import DefaultMapRouter
from emulator.cartridge.cartridge import Cartridge
from emulator.ppu.vram import VRAM
from emulator.mapping.ppu_mapping.ppu_space_mapping import PPUSpaceMapping


class PPUBus:
    def __init__(self, cartridge: Cartridge):
        self.cartridge = cartridge
        self.vram = VRAM()
        self.ppu_mapping_router = DefaultMapRouter(read_space_map=PPU_READ_MAP, write_space_map=PPU_WRITE_MAP)
        pass

    def read(self, address):
        mapped_space = self.ppu_mapping_router.route_read(address)
        if mapped_space == PPUSpaceMapping.PPU_PATTERN_TABLE_0:
            return self.cartridge.read(address)
        elif mapped_space == PPUSpaceMapping.PPU_PATTERN_TABLE_1:
            return self.cartridge.read(address)
        elif mapped_space == PPUSpaceMapping.PPU_NAME_TABLE_0:
            return self.vram.read(address)
        elif mapped_space == PPUSpaceMapping.PPU_NAME_TABLE_1:
            return self.vram.read(address)
        elif mapped_space == PPUSpaceMapping.PPU_NAME_TABLE_2:
            return self.vram.read(address)
        elif mapped_space == PPUSpaceMapping.PPU_NAME_TABLE_3:
            return self.vram.read(address)
        elif mapped_space == PPUSpaceMapping.PPU_PALETTE_RAM:
            return self.vram.read(address)
        
        return 0x00  # Default return for unmapped addresses

    def write(self, address, value):
        mapped_space = self.ppu_mapping_router.route_write(address)