from emulator.board.interrupt_info import InterruptInfo
from emulator.mapping.mapper_0 import Mapper0
from emulator.board.bus import Bus
from emulator.cpu.cpu import CPU
from emulator.ppu.ppu import PPU
from emulator.apu import APU
from emulator.cartridge.cartridge import Cartridge
from emulator.ram import RAM
from emulator.joypad import Joypad
from emulator.mapping.memory_map_router import MemoryMapRouter

def test_cpu_tick_opcodes(mocker):
    interrupt_info = InterruptInfo()
    ppu = PPU(interrupt_info)
    apu = APU(interrupt_info)
    ram = RAM()
    joypad = Joypad()
    memory_map_router = MemoryMapRouter()
    cartridge = Cartridge()

    # Mock the PRG ROM read method to return NOP (0xEA) for the first 3 bytes
    mock_prg = [0xEA, 0xEA, 0xEA]
    cartridge.prg_rom = mocker.MagicMock()
    cartridge.prg_rom.read = mocker.MagicMock(side_effect=lambda addr: mock_prg[addr - 0x8000])
    cartridge.mapper = Mapper0()


    bus = Bus(ppu, apu, cartridge, ram, joypad, memory_map_router)
    cpu = CPU(bus, interrupt_info)
    cpu.registers.pc = 0x8000

    # Act
    for _ in range(3):
        cpu.tick()

    # Assert
    assert cpu.registers.pc == 0x8003