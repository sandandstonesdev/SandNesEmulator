from emulator.mapping.io_register_type import IORegisterType
from emulator.mapping.io_register_router import IORegisterRouter
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
        mapped_port = self.registers.route_read(address)
        if mapped_port == IORegisterType.APUSQUARE1ENV:
            return self.apu_instructions.read_square1_env()
        elif mapped_port == IORegisterType.APUSQUARE1SWEEP:
            return self.apu_instructions.read_square1_sweep()
        elif mapped_port == IORegisterType.APUSQUARE1LO:
            return self.apu_instructions.read_square1_lo()
        elif mapped_port == IORegisterType.APUSQUARE1HI:
            return self.apu_instructions.read_square1_hi()
        elif mapped_port == IORegisterType.APUSQUARE2ENV:
            return self.apu_instructions.read_square2_env()
        elif mapped_port == IORegisterType.APUSQUARE2SWEEP:
            return self.apu_instructions.read_square2_sweep()
        elif mapped_port == IORegisterType.APUSQUARE2LO:
            return self.apu_instructions.read_square2_lo()
        elif mapped_port == IORegisterType.APUSQUARE2HI:
            return self.apu_instructions.read_square2_hi()
        elif mapped_port == IORegisterType.APUTRIANGLECTRL:
            return self.apu_instructions.read_triangle_ctrl()
        elif mapped_port == IORegisterType.APUTRIANGLUNUSED:
            return self.apu_instructions.read_triangle_unused()
        elif mapped_port == IORegisterType.APUTRIANGLELO:
            return self.apu_instructions.read_triangle_lo()
        elif mapped_port == IORegisterType.APUTRIANGLEHI:
            return self.apu_instructions.read_triangle_hi()
        elif mapped_port == IORegisterType.APUNOISEENV:
            return self.apu_instructions.read_noise_env()
        elif mapped_port == IORegisterType.APUNOISEUNUSED:
            return self.apu_instructions.read_noise_unused()
        elif mapped_port == IORegisterType.APUNOISEMODE:
            return self.apu_instructions.read_noise_mode()
        elif mapped_port == IORegisterType.APUNOISELENGTH:
            return self.apu_instructions.read_noise_length()
        elif mapped_port == IORegisterType.APUDMCFLAGS:
            return self.apu_instructions.read_dmc_flags()
        elif mapped_port == IORegisterType.APUDMCDIRECT:
            return self.apu_instructions.read_dmc_direct()
        elif mapped_port == IORegisterType.APUDMOSAMPLEADDR:
            return self.apu_instructions.read_dmc_sample_addr()
        elif mapped_port == IORegisterType.APUDMOSAMPLELEN:
            return self.apu_instructions.read_dmc_sample_len()
        elif mapped_port == IORegisterType.APUSTATUS:
            return self.apu_instructions.read_apu_status()
        elif mapped_port == IORegisterType.APUFRAMECOUNTER:
            return self.apu_instructions.read_apu_frame_counter()
        
        return 0x00
    
    def write_register(self, address: int, value: int):
        mapped_port = self.registers.route_write(address)
        if mapped_port == IORegisterType.APUSQUARE1ENV:
            self.apu_instructions.write_square1_env(value)
        elif mapped_port == IORegisterType.APUSQUARE1SWEEP:
            self.apu_instructions.write_square1_sweep(value)
        elif mapped_port == IORegisterType.APUSQUARE1LO:
            self.apu_instructions.write_square1_lo(value)
        elif mapped_port == IORegisterType.APUSQUARE1HI:
            self.apu_instructions.write_square1_hi(value)
        elif mapped_port == IORegisterType.APUSQUARE2ENV:
            self.apu_instructions.write_square2_env(value)
        elif mapped_port == IORegisterType.APUSQUARE2SWEEP:
            self.apu_instructions.write_square2_sweep(value)
        elif mapped_port == IORegisterType.APUSQUARE2LO:
            self.apu_instructions.write_square2_lo(value)
        elif mapped_port == IORegisterType.APUSQUARE2HI:
            self.apu_instructions.write_square2_hi(value)
        elif mapped_port == IORegisterType.APUTRIANGLECTRL:
            self.apu_instructions.write_triangle_ctrl(value)
        elif mapped_port == IORegisterType.APUTRIANGLUNUSED:
            self.apu_instructions.write_triangle_unused(value)
        elif mapped_port == IORegisterType.APUTRIANGLELO:
            self.apu_instructions.write_triangle_lo(value)
        elif mapped_port == IORegisterType.APUTRIANGLEHI:
            self.apu_instructions.write_triangle_hi(value)
        elif mapped_port == IORegisterType.APUNOISEENV:
            self.apu_instructions.write_noise_env(value)
        elif mapped_port == IORegisterType.APUNOISEUNUSED:
            self.apu_instructions.write_noise_unused(value)
        elif mapped_port == IORegisterType.APUNOISEMODE:
            self.apu_instructions.write_noise_mode(value)
        elif mapped_port == IORegisterType.APUNOISELENGTH:
            self.apu_instructions.write_noise_length(value)
        elif mapped_port == IORegisterType.APUDMCFLAGS:
            self.apu_instructions.write_dmc_flags(value)
        elif mapped_port == IORegisterType.APUDMCDIRECT:
            self.apu_instructions.write_dmc_direct(value)
        elif mapped_port == IORegisterType.APUDMOSAMPLEADDR:
            self.apu_instructions.write_dmc_sample_addr(value)
        elif mapped_port == IORegisterType.APUDMOSAMPLELEN:
            self.apu_instructions.write_dmc_sample_len(value)
        elif mapped_port == IORegisterType.APUSTATUS:
            self.apu_instructions.write_apu_status(value)
        elif mapped_port == IORegisterType.APUFRAMECOUNTER:
            self.apu_instructions.write_apu_frame_counter(value)

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