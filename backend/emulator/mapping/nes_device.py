from enum import Enum, auto

class NESDevice(Enum):
    RAM = auto()
    PPU_REGISTERS = auto()
    APU_IO_REGISTERS = auto()
    CARTRIDGE_SPACE = auto()
    EXPANSION_ROM = auto()
    SRAM = auto()
    JOYPAD = auto()
    # Add more devices as needed
