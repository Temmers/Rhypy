import pygame
from constants import WIDTH, HEIGHT, WHITE


class Note:
    note_list = []

    def __init__(self, color, speed, time):
        self.color = color
        self.speed = speed
        self.time = time
        self.pos = [WIDTH+20, HEIGHT/1.25-40]
        self.size = [15, 40]
        self.hitTime = self.time + self.speed*1000


class Player:
    size = [55, 35]
    pos = [WIDTH / 2 - 30, HEIGHT / 1.25 - 35]