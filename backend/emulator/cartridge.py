from emulator.mapping.mapper_0 import Mapper0


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

        self.prg_rom = None
        self.chr_rom = None
        self.mapper_id = 0
        self.mapper = None
        pass


    def insert(self, rom_path):
        self.read_rom(rom_path)

    def read_rom(self, rom_path):
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
            self.mapper = Mapper0(self)


        self.tv_system = (data[9] & 0x01)

        read_index = 16
        if self.trainer:
            read_index += 512

        # Loop if more PRG or CHR banks
        self.prg_rom = data[read_index:read_index + (self.prg_rom_chunks * 16384)]
        read_index += self.prg_rom_chunks * 16384
        self.chr_rom = data[read_index:read_index + (self.chr_rom_chunks * 8192)]
        read_index += self.chr_rom_chunks * 8192

    def read_prg(self, address):
        return self.prg_rom[address]
    
    def read_chr(self, address):
        return self.chr_rom[address]
    
    # Here we can make Mapper facade methods
    # def map_address(self, address):
    #    return self.mapper.map_address(address)