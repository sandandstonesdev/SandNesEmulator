from emulator.bus import Bus
from emulator.cpu.cpu import CPU
from emulator.ppu import PPU
from emulator.apu import APU
from emulator.cartridge import Cartridge
from emulator.ram import RAM
from emulator.joypad import Joypad
from emulator.mapping.memory_map_router import MemoryMapRouter

def test_cpu_tick_opcodes(mocker):
    ppu = PPU()
    apu = APU()
    ram = RAM()
    joypad = Joypad()
    memory_map_router = MemoryMapRouter()
    cartridge = Cartridge()

    # Mock the PRG ROM read method to return NOP (0xEA) for the first 3 bytes
    mock_prg = [0xEA, 0xEA, 0xEA]
    mocker.patch.object(cartridge, "read_prg", side_effect=lambda addr: mock_prg[addr] if addr < len(mock_prg) else 0)

    bus = Bus(ppu, apu, cartridge, ram, joypad, memory_map_router)
    cpu = CPU(bus)
    cpu.registers.pc = 0x8000

    # Act
    for _ in range(3):
        cpu.tick()

    # Assert
    assert cpu.registers.pc == 0x8003