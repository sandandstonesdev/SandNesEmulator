from emulator.cartridge.chr_rom_bank import CHRROMBank
from emulator.cartridge.prg_rom_bank import PrgRomBank
from emulator.cartridge.cartridge_map_router import CartridgeMapRouter
from emulator.mapping.mapper_0 import Mapper0


class Cartridge:
    def __init__(self, cartridgeMapRouter: CartridgeMapRouter):
        self.pattern_table = None
        self.masked_rom = None
        self.work_ram = None
        self.lockout = None
        self.prg_rom_chunks = 0 # 16KB units
        self.chr_rom_chunks = 0 # 8KB units
        self.mirroring_type = None
        self.battery_backed_ram = False
        self.alternarive_nametable_layout = False
        self.tv_system = None

        self.prg_rom = None
        self.chr_rom = None
        self.mapper_id = 0
        self.mapper = None
        self.cartridge_map_router = cartridgeMapRouter

    def insert_rom_file(self, rom_path):
        # Read iNES Header
        with open(rom_path, 'rb') as f:
            data = f.read()
        
        # Check NES header (0x4E 0x45 0x53 0x1A)
        if data[:4] == b'NES\x1A':
            print("Valid NES ROM header")
        else:
            print("Invalid header")
       
        self.prg_rom_chunks = data[4]
        self.chr_rom_chunks = data[5]

        self.mirroring_type = (data[6] & 0x01)
        self.battery_backed_ram = (data[6] & 0x02) >> 1
        self.trainer = (data[6] & 0x04) >> 2
        self.alternarive_nametable_layout = (data[6] & 0x08) >> 3
        
        lower_mapper_bits = (data[6] & 0xF0) >> 4
        upper_mapper_bits = (data[7] & 0xF0)
        
        self.mapper_id = lower_mapper_bits | upper_mapper_bits >> 4
        if self.mapper_id == 0:
            print("Using Mapper 0 (NROM)")
            self.mapper = Mapper0()


        self.tv_system = (data[9] & 0x01)

        read_index = 16
        if self.trainer:
            read_index += 512

        self.prg_rom = PrgRomBank(data[read_index:read_index + (self.prg_rom_chunks * 16384)])
        read_index += self.prg_rom_chunks * 16384
        self.chr_rom = CHRROMBank(data[read_index:read_index + (self.chr_rom_chunks * 8192)])
        read_index += self.chr_rom_chunks * 8192


    def read(self, address):
        mapped_device = self.cartridge_map_router.route_read(address)
        if mapped_device.name == 'PRG_ROM':
            return self.prg_rom.read(address)
        elif mapped_device.name == 'CHR_ROM':
            return self.chr_rom.read(address)

        return 0x00

    def write(self, address, value):
        mapped_device = self.cartridge_map_router.route_write(address)
        if mapped_device.name == 'PRG_ROM':
            self.prg_rom.write(address, value)
        elif mapped_device.name == 'CHR_ROM':
            self.chr_rom.write(address, value)

        # different read address is ignored
    
    