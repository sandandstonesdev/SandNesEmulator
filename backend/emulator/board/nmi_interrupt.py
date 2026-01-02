class NMIInterrupt:
    def __init__(self):
        self.enabled = False
        self.requested = False

    def enable(self): # PPU flag
        self.enabled = True

    def disable(self):
        self.enabled = False

    def is_enabled(self):
        return self.enabled
    
    def request(self):
        if self.enabled:
            self.requested = True
        else:
            self.requested = False

    def is_requested(self):
        return self.requested
    
    def clear_request(self):
        self.requested = False

    def is_pending(self):
        return self.requested