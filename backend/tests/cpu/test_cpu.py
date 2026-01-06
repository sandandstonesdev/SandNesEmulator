from emulator.mapping.cpu_mapping.cpu_maps import CPU_READ_MAP, CPU_WRITE_MAP
from emulator.mapping.base_mapping.default_map_router import DefaultMapRouter
from emulator.board.interrupt_info import InterruptInfo
from emulator.mapping.cartridge_mapping.mapper_0 import Mapper0
from emulator.board.bus import Bus
from emulator.cpu.cpu import CPU
from emulator.ppu.ppu import PPU
from emulator.apu.apu import APU
from emulator.cartridge.cartridge import Cartridge
from emulator.ram import RAM
from emulator.joypad import Joypad

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

    # Mock the PRG ROM read method to return NOP (0xEA) for the first 3 bytes
    mock_prg = [0xEA, 0xEA, 0xEA]
    cartridge.prg_rom = mocker.MagicMock()
    cartridge.prg_rom.read = mocker.MagicMock(side_effect=lambda addr: mock_prg[addr - 0x8000])
    cartridge.mapper = Mapper0()


    bus = Bus(ppu, apu, cartridge, ram, joypad, cpu_map_router)
    cpu = CPU(bus, interrupt_info)
    cpu.registers.pc = 0x8000

    # Act
    for _ in range(3):
        cpu.tick()

    # Assert
    assert cpu.registers.pc == 0x8003