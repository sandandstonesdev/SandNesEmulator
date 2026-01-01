from enum import Enum, auto

class NESDevice(Enum):
    RAM_ZERO_PAGE = auto()
    RAMSTACK = auto()
    RAM_GENERAL_PURPOSE = auto()
    RAM = auto()
    STACK = auto()
    PPU_REGISTERS = auto()
    OAM_DMA = auto()
    APU_IO_REGISTERS = auto()
    CARTRIDGE_SPACE = auto()
    EXPANSION_ROM = auto()
    SRAM = auto()
    JOYPAD1 = auto()
    JOYPAD2_NOT_SUPPORTED = auto()