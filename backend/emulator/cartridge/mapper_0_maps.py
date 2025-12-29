from emulator.cartridge.cartridge_memory_type import CartridgeMemoryType

# NES Mapper 0 (NROM) memory map
MAPPER_0_READ_MAP = {
    # PRG ROM: 0x8000-0xFFFF
    (0x8000, 0xFFFF): CartridgeMemoryType.PRG_ROM,
    # CHR ROM: 0x0000-0x1FFF (PPU address space)
    (0x0000, 0x1FFF): CartridgeMemoryType.CHR_ROM,
}

MAPPER_0_WRITE_MAP = {
    # CHR RAM (if present): 0x0000-0x1FFF (PPU address space)
    (0x0000, 0x1FFF): CartridgeMemoryType.CHR_RAM,
    # PRG RAM: Not present in standard NROM, but can be added for completeness
    # (0x6000, 0x7FFF): CartridgeMemoryType.PRG_RAM,
}
