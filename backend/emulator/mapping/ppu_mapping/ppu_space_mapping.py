from enum import Enum, auto

class PPUSpaceMapping(Enum):
    PPU_PATTERN_TABLE_0 = auto()
    PPU_PATTERN_TABLE_1 = auto()
    PPU_NAME_TABLE_0 = auto()
    PPU_NAME_TABLE_1 = auto()
    PPU_NAME_TABLE_2 = auto()
    PPU_NAME_TABLE_3 = auto()
    PPU_NAME_TABLE_MIRRORS = auto()
    PPU_PALETTE_RAM = auto()
    PPU_PALETTE_RAM_MIRRORS = auto()