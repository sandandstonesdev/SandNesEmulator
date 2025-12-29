from enum import Enum, auto

class CartridgeMemoryType(Enum):
    PRG_ROM = auto()
    PRG_RAM = auto()
    CHR_ROM = auto()
    CHR_RAM = auto()
    TRAINER = auto()
    MAPPER_REGISTERS = auto()
    # Add more types as needed for specific mappers
