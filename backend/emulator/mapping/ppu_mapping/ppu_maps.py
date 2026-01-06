from emulator.mapping.ppu_mapping.ppu_space_mapping import PPUSpaceMapping


PPU_READ_MAP = {
    (0x0000, 0x0fff): PPUSpaceMapping.PPU_PATTERN_TABLE_0,  # Pattern Table 0
    (0x1000, 0x1fff): PPUSpaceMapping.PPU_PATTERN_TABLE_1,  # Pattern Table 1
    (0x2000, 0x23ff): PPUSpaceMapping.PPU_NAME_TABLE_0,     # Name Table 0
    (0x2400, 0x27ff): PPUSpaceMapping.PPU_NAME_TABLE_1,     # Name Table 1
    (0x2800, 0x2bff): PPUSpaceMapping.PPU_NAME_TABLE_2,     # Name Table 2
    (0x2c00, 0x2fff): PPUSpaceMapping.PPU_NAME_TABLE_3,     # Name Table 3
    (0x3000, 0x3eff): PPUSpaceMapping.PPU_NAME_TABLE_MIRRORS, # Name Table Mirrors
    (0x3f00, 0x3f1f): PPUSpaceMapping.PPU_PALETTE_RAM,      # Palette RAM
    (0x3f20, 0x3fff): PPUSpaceMapping.PPU_PALETTE_RAM_MIRRORS, # Palette RAM Mirrors
}

PPU_WRITE_MAP = {
    (0x0000, 0x0fff): PPUSpaceMapping.PPU_PATTERN_TABLE_0,  # Pattern Table 0
    (0x1000, 0x1fff): PPUSpaceMapping.PPU_PATTERN_TABLE_1,  # Pattern Table 1
    (0x2000, 0x23ff): PPUSpaceMapping.PPU_NAME_TABLE_0,     # Name Table 0
    (0x2400, 0x27ff): PPUSpaceMapping.PPU_NAME_TABLE_1,     # Name Table 1
    (0x2800, 0x2bff): PPUSpaceMapping.PPU_NAME_TABLE_2,     # Name Table 2
    (0x2c00, 0x2fff): PPUSpaceMapping.PPU_NAME_TABLE_3,     # Name Table 3
    (0x3000, 0x3eff): PPUSpaceMapping.PPU_NAME_TABLE_MIRRORS, # Name Table Mirrors
    (0x3f00, 0x3f1f): PPUSpaceMapping.PPU_PALETTE_RAM,      # Palette RAM
    (0x3f20, 0x3fff): PPUSpaceMapping.PPU_PALETTE_RAM_MIRRORS, # Palette RAM Mirrors
}