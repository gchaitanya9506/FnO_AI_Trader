from collections import deque

class TickBuffer:
    def __init__(self):
        self.ticks = deque(maxlen=5000)

    def add(self, tick):
        self.ticks.append(tick)

    def get_all(self):
        return list(self.ticks)