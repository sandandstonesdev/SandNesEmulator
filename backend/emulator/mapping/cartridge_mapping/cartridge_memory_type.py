from enum import Enum, auto

class CartridgeMemoryType(Enum):
    PRG_ROM_BANK1 = auto()
    PRG_ROM_BANK2 = auto()
    PRG_RAM = auto()
    CHR_ROM_BANK1 = auto()
    CHR_ROM_BANK2 = auto()
    CHR_RAM = auto()
    TRAINER = auto()
    MAPPER_REGISTERS = auto()
    # Add more types as needed for specific mappers
