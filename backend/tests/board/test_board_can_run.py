from emulator.board.board import Board

def read_dummy_rom():
    fake_rom_data = (
        b'NES\x1A' +
        bytes([2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) +
        bytes([0xEA, 0xEA, 0xEA]) + b'\x00' * (32768 - 3) + # PRG ROM
        b'\x00' * 8192 # CHR ROM
    )
    return fake_rom_data

def test_board_can_run(mocker):
    rom_path = "tests/roms/empty.nes"  # Path to a minimal ROM for
    frames = []
    board = Board()
    
    rom = read_dummy_rom()
    
    mock_file = mocker.patch("builtins.open", mocker.mock_open())
    mock_file.return_value.read.return_value = rom
    
    board.insert_rom(rom_path)  # Insert an empty cartridge for testing
    board.power_on()
    board.reset()

    # Run a few ticks to ensure no exceptions occur
    for _ in range(10):
        board.update_controller(0x00)
        board.tick()
        frame = board.get_frame()
        frames.append(frame)

    board.reset()
    board.power_off()

    assert len(frames) > 0  # Frames are collecd
