from emulator.mapping.register_mapping.io_register_type import IORegisterType

# NES Mapper 0 (NROM) memory map
PPU_REGISTER_READ_MAP = {
    (0x2000): IORegisterType.PPUCTRL,  # PPU Control Register
    (0x2001): IORegisterType.PPUMASK,   # PPU Mask Register
    (0x2002): IORegisterType.PPUSTATUS, # PPU Status Register
    (0x2003): IORegisterType.OAMADDR,   # OAM Address Register
    (0x2004): IORegisterType.OAMDATA,   # OAM Data Register
    (0x2005): IORegisterType.PPUSCROLL, # PPU Scroll Register
    (0x2006): IORegisterType.PPUADDR,   # PPU Address Register
    (0x2007): IORegisterType.PPUDATA,   # PPU Data Register
    (0x4014): IORegisterType.OAMDMA,    # OAM DMA Register
}

PPU_REGISTER_WRITE_MAP = {
    (0x2000): IORegisterType.PPUCTRL,  # PPU Control Register
    (0x2001): IORegisterType.PPUMASK,   # PPU Mask Register
    (0x2002): IORegisterType.PPUSTATUS, # PPU Status Register
    (0x2003): IORegisterType.OAMADDR,   # OAM Address Register
    (0x2004): IORegisterType.OAMDATA,   # OAM Data Register
    (0x2005): IORegisterType.PPUSCROLL, # PPU Scroll Register
    (0x2006): IORegisterType.PPUADDR,   # PPU Address Register
    (0x2007): IORegisterType.PPUDATA,   # PPU Data Register
    (0x4014): IORegisterType.OAMDMA,    # OAM DMA Register
}
