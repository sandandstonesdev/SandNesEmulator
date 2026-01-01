from emulator.mapping.nes_device import NESDevice

# Address maps for NES memory devices
READ_DEVICE_MAP = {
    (0x0000, 0x00FF): NESDevice.RAM_ZERO_PAGE,  # Zero Page
    (0x0100, 0x01FF): NESDevice.STACK,  # Stack
    (0x0200, 0x1FFF): NESDevice.RAM_GENERAL_PURPOSE,  # General Purpose RAM
    (0x2000, 0x3FFF): NESDevice.PPU_REGISTERS,
    (0x4000, 0x4015): NESDevice.APU_IO_REGISTERS,
    (0x4016, 0x4016): NESDevice.JOYPAD1,  # Joypad 1 (read)
    (0x4017, 0x4017): NESDevice.JOYPAD2_NOT_SUPPORTED,  # Joypad 2 (read)
    (0x4018, 0x401F): NESDevice.EXPANSION_ROM,
    (0x4020, 0x5FFF): NESDevice.SRAM,
    (0x6000, 0x7FFF): NESDevice.SRAM,
    (0x8000, 0xFFFF): NESDevice.CARTRIDGE_SPACE,
}

WRITE_DEVICE_MAP = {
    (0x0000, 0x00FF): NESDevice.RAM_ZERO_PAGE,  # Zero Page
    (0x0100, 0x01FF): NESDevice.STACK,  # Stack
    (0x0200, 0x1FFF): NESDevice.RAM_GENERAL_PURPOSE,  # General Purpose RAM
    (0x2000, 0x3FFF): NESDevice.PPU_REGISTERS,
    (0x4000, 0x4013): NESDevice.APU_IO_REGISTERS,
    (0x4014, 0x4014): NESDevice.OAM_DMA,  # PPU OAMDMA (write)
    (0x4015, 0x4015): NESDevice.APU_IO_REGISTERS,  # APU status (write)
    (0x4016, 0x4016): NESDevice.JOYPAD1,  # Joypad strobe (write)
    (0x4017, 0x4017): NESDevice.APU_IO_REGISTERS,  # APU frame counter (write)
    (0x4018, 0x401F): NESDevice.EXPANSION_ROM,
    (0x4020, 0x5FFF): NESDevice.SRAM,
    (0x6000, 0x7FFF): NESDevice.SRAM,
    (0x8000, 0xFFFF): NESDevice.CARTRIDGE_SPACE,
}