from emulator.cartridge.prg_rom_bank import PrgRomBank
from emulator.apu.apu import APU
from emulator.board.bus import Bus
from emulator.board.interrupt_info import InterruptInfo
from emulator.cartridge.cartridge import Cartridge
from emulator.cpu.cpu import CPU
from emulator.joypad import Joypad
from emulator.mapping.base_mapping.default_map_router import DefaultMapRouter
from emulator.mapping.cartridge_mapping.mapper_0 import Mapper0
from emulator.mapping.cpu_mapping.cpu_maps import CPU_READ_MAP, CPU_WRITE_MAP
from emulator.ppu.ppu import PPU
from emulator.ram import RAM


def test_cpu_tick_opcodes(mocker):
    interrupt_info = InterruptInfo()
    io_register_router = mocker.MagicMock()
    joypad = Joypad(io_register_router)
    ppu_bus = mocker.MagicMock()
    ppu = PPU(ppu_bus, interrupt_info)
    apu = APU(io_register_router, interrupt_info)
    ram = RAM()
    cpu_map_router = DefaultMapRouter(read_space_map=CPU_READ_MAP, write_space_map=CPU_WRITE_MAP)

    cartridge = Cartridge()

    # Create a mock PRG ROM of 32KB (0x8000 bytes), filled with NOP (0xEA)
    mock_prg = [0xEA] * 0x8000
    # Set reset vector at $FFFC/$FFFD (0x7FFC/0x7FFD in this array) to 0x8000
    mock_prg[0x7FFC] = 0x00  # low byte
    mock_prg[0x7FFD] = 0x80  # high byte

    prg_rom_bank = mocker.MagicMock(spec=PrgRomBank)
    prg_rom_bank.base_address = 0x8000
    prg_rom_bank.data = mock_prg
    prg_rom_bank.read = mocker.MagicMock(side_effect=lambda addr: mock_prg[addr - 0x8000])

    cartridge.prg_rom_banks = [prg_rom_bank]
    cartridge.mapper = Mapper0()

    bus = Bus(ppu, apu, cartridge, ram, joypad, cpu_map_router)
    cpu = CPU(bus, interrupt_info)

    # Simulate reset: fetch PC from reset vector
    cpu.registers.pc = (mock_prg[0x7FFD] << 8) | mock_prg[0x7FFC]

    for _ in range(3):
        cpu.tick()

    assert cpu.registers.pc == 0x8003