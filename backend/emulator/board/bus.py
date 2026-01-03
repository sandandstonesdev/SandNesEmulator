from __future__ import annotations
import weakref
from emulator.mapping.io_register_router import IORegisterRouter
from emulator.mapping.nes_device import NESDevice
from emulator.apu.apu import APU
from emulator.cartridge.cartridge import Cartridge
from emulator.joypad import Joypad
from emulator.mapping.memory_map_router import MemoryMapRouter
from emulator.ppu.ppu import PPU
from emulator.ram import RAM


class Bus:
    def __init__(self,
                 ppu: PPU,
                 apu: APU,
                 cartridge: Cartridge,
                 ram: RAM,
                 joypad:Joypad,
                 memoryMapRouter: MemoryMapRouter):
        self.ppu = ppu
        self.apu = apu
        self.cartridge = cartridge
        self.ram = ram
        self.joypad = joypad
        self.memory_map_router = memoryMapRouter
        self.master_clock = 0
        

    def ram_read(self, address):
        mapped_device = self.memory_map_router.route_read(address)
        if mapped_device == NESDevice.CARTRIDGE_SPACE:
            return self.cartridge.read(address)
        elif mapped_device == NESDevice.PPU_REGISTERS:
            return self.ppu.read(address)
        elif mapped_device == NESDevice.APU_IO_REGISTERS:
            return self.apu.read(address)
        elif mapped_device == NESDevice.JOYPAD1:
            return self.joypad.read(address)
        elif mapped_device == NESDevice.JOYPAD2_NOT_SUPPORTED:
            return 0x00  # Not supported, return default
        elif mapped_device == NESDevice.RAM_ZERO_PAGE:
            return self.ram.read_zp(address)
        elif mapped_device == NESDevice.STACK:
            return self.ram.read_stack(address)
        elif mapped_device == NESDevice.RAM_GENERAL_PURPOSE:
            return self.ram.read(address)
        return 0x00  # Default return for unmapped addresses

    def ram_write(self, address, value):
        mapped_device = self.memory_map_router.route_write(address, value)
        if mapped_device == NESDevice.CARTRIDGE_SPACE:
            return self.cartridge.write_prg(address, value)
        elif mapped_device == NESDevice.PPU_REGISTERS:
             return self.ppu.write(address, value)
        elif mapped_device == NESDevice.APU_IO_REGISTERS:
            return self.apu.write(address, value)
        elif mapped_device == NESDevice.JOYPAD1:
            return self.joypad.write(address, value)
        elif mapped_device == NESDevice.RAM_ZERO_PAGE:
            return self.ram.write_zp(address, value)
        elif mapped_device == NESDevice.RAMSTACK:
            return self.ram.write_stack(address, value)
        elif mapped_device == NESDevice.RAM_GENERAL_PURPOSE:
            return self.ram.write(address, value)
        
    def attach_cpu(self, cpu: CPU):
        self.cpu = weakref.ref(cpu)

    def tick(self):
        # Note: CPU/PPU => 1/3
        self.cpu.tick()
        for _ in range(3):
            self.ppu.tick()
        #self.apu.tick()
        self.master_clock += 1

    def power_on(self):
        self.cpu.power_on()

    def reset(self):
        self.cpu.reset()

    def insert_rom(self):
        self.cartridge.insert_rom_file(rom_path="")

    
    def power_off(self):
        pass

    def get_frame(self):
        return self.ppu.get_frame()

    def update_controller(self, controller_state):
        self.joypad.update_state(controller_state)
        pass