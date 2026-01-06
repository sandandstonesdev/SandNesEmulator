from emulator.mapping.register_mapping.io_register_router import IORegisterRouter
from emulator.mapping.register_mapping.io_register_type import IORegisterType
from emulator.apu.apu_instructions import APUInstructions
from emulator.apu.apu_registers import APURegisters
from emulator.board.interrupt_info import InterruptInfo

class APU:
    def __init__(self, io_register_router: IORegisterRouter, interrupt_info: InterruptInfo):
        self.io_register_router = io_register_router
        self.interrupt_info = interrupt_info
        self.registers = APURegisters()
        self.apu_instructions = APUInstructions(self.registers, interrupt_info)

    def reset(self):
        pass

    def read_register(self, address: int) -> int:
        value = self.apu_instructions.read_register(address)
        return value
    
    def write_register(self, address: int, value: int):
        self.apu_instructions.write_register(address, value)

    def tick(self):
        # APUInstructions
        pass


    def clock_frame_counter(self):
        pass
    
    def render_mixed_sample(self) -> int:
        self.render_square_sample(0)
        self.render_square_sample(1)
        self.render_triangle_sample()
        self.render_noise_sample()
        self.render_dmc_sample()
        
        self.mix_squares()
        self.mix_triangle_noise_dmc()


        return 0x00
    
    def mix_squares(self) -> int:
        return 0x00
    
    def mix_triangle_noise_dmc(self) -> int:
        return 0x00

    def render_square_sample(self, channel: int) -> int:
        return 0x00
    
    def render_triangle_sample(self) -> int:
        return 0x00
    
    def render_noise_sample(self) -> int:
        return 0x00
    
    def render_dmc_sample(self) -> int:
        return 0x00