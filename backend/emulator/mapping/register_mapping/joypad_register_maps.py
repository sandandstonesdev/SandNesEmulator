from emulator.mapping.register_mapping.io_register_type import IORegisterType

# NES Mapper 0 (NROM) memory map
JOYPAD_REGISTER_READ_MAP = {
    (0x4016): IORegisterType.JOYPAD1,  # Joypad 1 (read)
    (0x4017): IORegisterType.JOYPAD2,  # Joypad 2 (read)
}

JOYPAD_REGISTER_WRITE_MAP = {
    (0x4016): IORegisterType.JOYPAD1,  # Joypad 1 (read)
    (0x4017): IORegisterType.JOYPAD2,  # Joypad 2 (read)
}
