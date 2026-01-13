from emulator.mapping.cartridge_mapping.cartridge_memory_type import CartridgeMemoryType
from emulator.mapping.cartridge_mapping.mapper_0 import Mapper0
from emulator.cartridge.chr_rom_bank import CHRROMBank
from emulator.cartridge.prg_rom_bank import PrgRomBank


class Cartridge:
    def __init__(self):
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

        self.prg_rom_banks = []
        self.chr_rom_banks = []
        self.mapper_id = 0
        self.mapper = None
        self.interrupt_vectors = []

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

        prg_base_addr = 0x8000
        prg_bank_size = 0x3FFF
        for i in range(self.prg_rom_chunks):
            read_address = read_index + (i * prg_bank_size) # To 0x4010
            prg_rom_bank = PrgRomBank(data[read_address:read_address + prg_bank_size],
                                      base_address = prg_base_addr + (i * prg_bank_size))
            self.prg_rom_banks.append(prg_rom_bank)

        read_index += self.prg_rom_chunks * prg_bank_size

        for i in range(self.chr_rom_chunks):
            read_address = read_index + (i * 8192)
            chr_rom_bank = CHRROMBank(data[read_address:read_address + 8192])
            self.chr_rom_banks.append(chr_rom_bank)
            read_index += 8192

        if self.chr_rom_chunks == 1:
            # Mirror single bank to fill 8KB space
            chr_ram_bank = CHRROMBank(bytearray(8192), base_address=0x1000)
            self.chr_rom_banks.append(chr_ram_bank)

        

    def read(self, address):
        mapped_device = self.mapper.map_read(address)
        if mapped_device == CartridgeMemoryType.PRG_ROM_BANK1:
            prg_rom_bank: PrgRomBank = self.prg_rom_banks[0]
            return prg_rom_bank.read(address)
        if mapped_device == CartridgeMemoryType.PRG_ROM_BANK2:
            prg_rom_bank: PrgRomBank = self.prg_rom_banks[1]
            return prg_rom_bank.read(address)
        elif mapped_device == CartridgeMemoryType.CHR_ROM_BANK1:
            chr_rom_bank: CHRROMBank = self.chr_rom_banks[0]
            return chr_rom_bank.read(address)
        elif mapped_device == CartridgeMemoryType.CHR_ROM_BANK2:
            chr_rom_bank: CHRROMBank = self.chr_rom_banks[1]
            return chr_rom_bank.read(address)
        return 0x00

    def write(self, address, value):
        mapped_device = self.mapper.map_write(address)
        if mapped_device == CartridgeMemoryType.PRG_ROM_BANK1:
            prg_rom_bank: PrgRomBank = self.prg_rom_banks[0]
            prg_rom_bank.write(address, value)
        elif mapped_device == CartridgeMemoryType.PRG_ROM_BANK2:
            prg_rom_bank: PrgRomBank = self.prg_rom_banks[1]
            prg_rom_bank.write(address, value)
        elif mapped_device == CartridgeMemoryType.CHR_ROM_BANK1:
            chr_rom_bank: CHRROMBank = self.chr_rom_banks[0]
            chr_rom_bank.write(address, value)
        elif mapped_device == CartridgeMemoryType.CHR_ROM_BANK2:
            chr_rom_bank: CHRROMBank = self.chr_rom_banks[1]
            chr_rom_bank.write(address, value)

        # different read address is ignored
    
    