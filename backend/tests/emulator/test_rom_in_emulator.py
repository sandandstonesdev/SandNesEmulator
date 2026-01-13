import os
from emulator.emulator import Emulator

def test_prgrom_loading_in_emulator(mocker):
    rom_path = os.path.join(os.path.dirname(__file__), "sandnes_demo.nes")
    
    emulator = Emulator()
    emulator.insert_cartridge(rom_path)
    emulator.power_on()
    
    if emulator.is_on:
        for i in range(10): # Check if 10 ticks run without issues
            emulator.tick()
            
    emulator.power_off()

    # If no exceptions
    assert True