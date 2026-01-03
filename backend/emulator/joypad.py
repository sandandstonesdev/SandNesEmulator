from emulator.mapping.io_register_router import IORegisterRouter


class Joypad:
    # Implement Shift Register and regular controller state mapping
    def __init__(self, io_register_router: IORegisterRouter):
        self.io_register_router = io_register_router
        self.shift_register = 0
        self.strobe = 0

    def write(self, address, value):
        mapped_port = self.io_register_router.route_write(address, value)
        if mapped_port == IORegisterRouter.JOYPAD1:
            self.strobe = value
            if self.strobe & 1:
               self.shift_register = 0  # Reset shift register on strobe high
        return

    def read(self, address):
        mapped_port = self.io_register_router.route_read(address)
        if mapped_port == IORegisterRouter.JOYPAD1:
            # Return the least significant bit of the shift register
            value = self.shift_register & 1
            # Shift the register to the right
            self.shift_register >>= 1
            return value | 0x40  # Upper bits are typically high
        return 0x00

    def update_state(self, controller_state):
        if self.strobe & 1:
            self.map_controller_state_to_bits(controller_state)
        
    def map_controller_state_to_bits(self, controller_state):
        # Process controller state (maped buttons to bits)
        self.shift_register = 0
        pass