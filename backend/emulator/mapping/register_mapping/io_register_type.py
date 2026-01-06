from enum import Enum, auto


class IORegisterType(Enum):
    pass
    # Joypad Registers
    JOYPAD1 = auto()
    JOYPAD2 = auto()
    # PPU Registers\
    PPUCTRL = auto()
    PPUMASK = auto()
    PPUSTATUS = auto()
    OAMADDR = auto()
    OAMDATA = auto()
    PPUSCROLL = auto()
    PPUADDR = auto()
    PPUDATA = auto()
    OAMDMA = auto()
    
    # APU Registers
    APUSQUARE1ENV = auto()
    APUSQUARE1SWEEP = auto()
    APUSQUARE1LO = auto()
    APUSQUARE1HI = auto()

    APUSQUARE2ENV = auto()
    APUSQUARE2SWEEP = auto()
    APUSQUARE2LO = auto()
    APUSQUARE2HI = auto()

    APUTRIANGLECTRL = auto()
    APUTRIANGLUNUSED = auto()
    APUTRIANGLELO = auto()
    APUTRIANGLEHI = auto()

    APUNOISEENV = auto()
    APUNOISEUNUSED = auto()
    APUNOISEMODE = auto()
    APUNOISELENGTH = auto()
    
    APUDMCFLAGS = auto()
    APUDMCDIRECT = auto()
    APUDMOSAMPLEADDR = auto()
    APUDMOSAMPLELEN = auto()
    
    APUSTATUS = auto()
    APUFRAMECOUNTER = auto()
    
    # Mapper Registers
