from emulator.mapping.cartridge_mapping.cartridge_memory_type import CartridgeMemoryType

# NES Mapper 0 (NROM) memory map
MAPPER_0_READ_MAP = {
    # PRG ROM: 0x8000-0xFFFF
    (0x8000, 0xBFFF): CartridgeMemoryType.PRG_ROM_BANK1,
    (0xC000, 0xFFFF): CartridgeMemoryType.PRG_ROM_BANK2,
    # CHR ROM: 0x0000-0x1FFF (PPU address space)
    (0x0000, 0x0FFF): CartridgeMemoryType.CHR_ROM_BANK1,
    (0x1000, 0x1FFF): CartridgeMemoryType.CHR_ROM_BANK2,
}

MAPPER_0_WRITE_MAP = {
    # PRG ROM: 0x8000-0xFFFF
    (0x8000, 0xBFFF): CartridgeMemoryType.PRG_ROM_BANK1,
    (0xC000, 0xFFFF): CartridgeMemoryType.PRG_ROM_BANK2,
    # CHR ROM: 0x0000-0x1FFF (PPU address space)
    (0x0000, 0x0FFF): CartridgeMemoryType.CHR_ROM_BANK1,
    (0x1000, 0x1FFF): CartridgeMemoryType.CHR_ROM_BANK2,
}
