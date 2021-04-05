from constants import WIDTH, HEIGHT

class Note:
    note_list = []
    def __init__(self, color, speed, time):
        self.color = color
        self.speed = speed
        self.time = time
        self.pos = [WIDTH+20, HEIGHT/1.25-20]
        self.size = [40, 40]


class Metronome:
    def __init__(self):
        self.BPM = 120