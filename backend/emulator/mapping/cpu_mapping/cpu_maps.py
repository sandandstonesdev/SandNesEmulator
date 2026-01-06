from emulator.mapping.cpu_mapping.cpu_space_mapping import CPUSpaceMapping

# Address maps for NES memory devices
CPU_READ_MAP = {
    (0x0000, 0x00FF): CPUSpaceMapping.RAM_ZERO_PAGE,  # Zero Page
    (0x0100, 0x01FF): CPUSpaceMapping.STACK,  # Stack
    (0x0200, 0x02ff): CPUSpaceMapping.RAM_OAM,  # General Purpose RAM
    (0x0300, 0x07FF): CPUSpaceMapping.RAM_GENERAL_PURPOSE,  # General Purpose RAM
    (0x0800, 0x1FFF): CPUSpaceMapping.RAM_MIRRORED,  # Mirrored RAM
    (0x2000, 0x3FFF): CPUSpaceMapping.PPU_REGISTERS,
    (0x4000, 0x4015): CPUSpaceMapping.APU_IO_REGISTERS,
    (0x4016, 0x4016): CPUSpaceMapping.JOYPAD1,  # Joypad 1 (read)
    (0x4017, 0x4017): CPUSpaceMapping.JOYPAD2_NOT_SUPPORTED,  # Joypad 2 (read)
    (0x4018, 0x401F): CPUSpaceMapping.EXPANSION_ROM,
    (0x4020, 0x5FFF): CPUSpaceMapping.SRAM,
    (0x6000, 0x7FFF): CPUSpaceMapping.SRAM,
    (0x8000, 0xFFFF): CPUSpaceMapping.CARTRIDGE_SPACE,
}

CPU_WRITE_MAP = {
    (0x0000, 0x00FF): CPUSpaceMapping.RAM_ZERO_PAGE,  # Zero Page
    (0x0100, 0x01FF): CPUSpaceMapping.STACK,  # Stack
    (0x0200, 0x03FF): CPUSpaceMapping.RAM_OAM,  # OAM Memory
    (0x0300, 0x07FF): CPUSpaceMapping.RAM_GENERAL_PURPOSE,  # General Purpose RAM
    (0x0800, 0x1FFF): CPUSpaceMapping.RAM_MIRRORED,  # Mirrored RAM
    (0x2000, 0x3FFF): CPUSpaceMapping.PPU_REGISTERS,
    (0x4000, 0x4013): CPUSpaceMapping.APU_IO_REGISTERS,
    (0x4014, 0x4014): CPUSpaceMapping.OAM_DMA,  # PPU OAMDMA (write)
    (0x4015, 0x4015): CPUSpaceMapping.APU_IO_REGISTERS,  # APU status (write)
    (0x4016, 0x4016): CPUSpaceMapping.JOYPAD1,  # Joypad strobe (write)
    (0x4017, 0x4017): CPUSpaceMapping.APU_IO_REGISTERS,  # APU frame counter (write)
    (0x4018, 0x401F): CPUSpaceMapping.EXPANSION_ROM,
    (0x4020, 0x5FFF): CPUSpaceMapping.SRAM,
    (0x6000, 0x7FFF): CPUSpaceMapping.SRAM,
    (0x8000, 0xFFFF): CPUSpaceMapping.CARTRIDGE_SPACE,
}