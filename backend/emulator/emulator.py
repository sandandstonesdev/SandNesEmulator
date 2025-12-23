from backend.emulator.board import Board

class Emulator:
    def __init__(self, name):
        self.board = Board()
        pass

    # Open ROM In GUI
    def insert_cartridge(self, cartridge):
        self.board.insert_cartridge(cartridge)

    # On Button in GUI
    def power_on(self):
        self.board.power_on()

    # On Reset in GUI
    def reset(self):
        self.board.reset()

    # Off Button in GUI
    def power_off(self):
        self.board.power_off()

    # Get Frame (maybe batch get is better for frontend performance)
    def get_frame(self):
        return self.board.get_frame()

    # Input controller state from GUI
    def input_controller_state(self, controller_state):
        self.board.input_controller_state(controller_state)