from pygame import*
from Sprite import*

class Character(Sprite):
    def __init__(self, speed, hp, x, y, size, img_link):
        super().__init__(x, y, size, img_link)
        self.hp = hp
        self.speed = speed
        self.normalspeed = self.speed # https://habr.com/ru/post/131931/
