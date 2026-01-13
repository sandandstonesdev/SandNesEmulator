from emulator.board.board import Board

def read_dummy_rom():
    prg_rom = (
        bytes([0xEA, 0xEA, 0xEA]) +  # NOP instructions at start
        b'\x00' * (32768 - 3 - 4) +  # Fill PRG ROM except last 4 bytes
        bytes([0x00, 0x80, 0x00, 0x00])  # Reset vector at 0xFFFC: 0x8000 (little endian), then two unused bytes
    )
    fake_rom_data = (
        b'NES\x1A' +
        bytes([2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) +
        prg_rom +
        b'\x00' * 8192  # CHR ROM
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
