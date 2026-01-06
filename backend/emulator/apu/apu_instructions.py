from emulator.apu.apu_registers import APURegisters
from emulator.mapping.register_mapping.io_register_router import IORegisterRouter

class APUInstructions:
    def __init__(self, apu_registers: APURegisters, interrupt_info: IORegisterRouter):
        self.apu_registers = apu_registers
        self.interrupt_info = interrupt_info

    def read_register(self, address: int) -> int:
       register_id = self.apu_registers.get_register_id(address) # int
       if register_id == 0: # Some register
           return 0
           # Implement reading logic for this register
       else:
           pass
        # Handle invalid address or ignore
        # Implement reading from APU registers based on address
        
    def write_register(self, address: int, value: int):
       register_id = self.apu_registers.get_register_id(address) # int
       if register_id == 0: # Some register
           return 0
           # Implement reading logic for this register
       else:
           pass        
        # Implement writing to APU registers based on address and value

    def get_register_id(self, address: int) -> int:
      return self.registers.get_apu_register_id(address)