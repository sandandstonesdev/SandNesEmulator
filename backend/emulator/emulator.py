from emulator.board.board import Board

class Emulator:
    def __init__(self):
        self.is_on = False
        self.board = Board()

    def insert_cartridge(self, cartridge):
        self.board.insert_rom(cartridge)

    def power_on(self):
        self.board.power_on()
        self.is_on = True

    def reset(self):
        self.board.reset()
        self.is_on = True

    def tick(self):
        if not self.is_on:
            return None
        
        self.board.tick()

    def run_frame(self):
        TICKS_PER_FRAME = 29780
        for _ in range(TICKS_PER_FRAME):
            self.tick()

        return self.board.get_frame()

    def power_off(self):
        self.board.power_off()
        self.is_on = False

    def input_controller_state(self, controller_state):
        self.board.update_controller(controller_state)