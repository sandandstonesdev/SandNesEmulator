from emulator.cartridge.cartridge import Cartridge
from emulator.cartridge.cartridge_map_router import CartridgeMapRouter


def read_dummy_rom():
    fake_rom_data = (
        b'NES\x1A' +
        bytes([2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) +
        bytes([0xEA, 0xEA, 0xEA]) + b'\x00' * (32768 - 3) + # PRG ROM
        b'\x00' * 8192 # CHR ROM
    )
    return fake_rom_data

def test_cartridge_can_load_and_read_prg(mocker):
    cartridge_map_router = CartridgeMapRouter()
    cartridge = Cartridge(cartridge_map_router)

    rom = read_dummy_rom()
    mock_file = mocker.patch("builtins.open", mocker.mock_open())
    mock_file.return_value.read.return_value = rom
    cartridge.insert_rom_file(rom_path="dummy_path.nes")
    
    # Act & Assert
    assert cartridge.read(0x8000) == 0xEA
    assert cartridge.read(0x8001) == 0xEA
    assert cartridge.read(0x8002) == 0xEA