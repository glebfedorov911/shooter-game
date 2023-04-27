from pygame import*
from Character import*
from random import*
from Player import*

hero = Player(50, 70, "hero.png")

class Enemy(Character):
    def __init__(self, speed, hp, x, y, size, img_link=False):
        super().__init__(speed, hp, x, y, size, img_link)
        self.offset = 20
        self.size = size
        self.speed = speed
        self.quantity = 0
        self.angle = 0
    def updater(self):
        if self.quantity == 0:
            self.NPSx = randint(self.offset, (width - self.size[0] - self.offset))
            self.NPSy = randint(self.offset, (height - self.size[1] - self.offset))
            self.quantity = 1    
        if self.rect.x % self.speed != 0:
            self.rect.x -= 1
        elif self.NPSx % self.speed != 0:
            self.NPSx -= 1 
        else:
            if self.rect.x < self.NPSx:
                self.rect.x += self.speed
                if self.angle == 180:
                    self.angle = 270
                    self.picture(90)
                    self.angle = 0
                elif self.angle == 360:
                    self.angle = 360
                    self.picture(90)
                    self.angle = 0
                elif self.angle == 90:
                    self.angle = 180
                    self.picture(90)
                    self.angle = 0
                else:
                    self.angle = 0
            elif self.rect.x > self.NPSx: 
                self.rect.x -= self.speed
                if self.angle == 0:
                    self.angle = 270
                    self.picture(90)
                    self.angle = 180
                elif self.angle == 90:
                    self.angle = 360
                    self.picture(90)
                    self.angle = 180
                elif self.angle == 360:
                    self.angle = 180
                    self.picture(90)
                    self.angle = 180
                else:
                    self.angle = 180
            if self.rect.x == self.NPSx:
                if self.rect.y % self.speed != 0:
                    self.rect.y -= 1
                elif self.NPSy % self.speed != 0:
                    self.NPSy -= 1
                else:
                    if self.rect.y > self.NPSy:
                        self.rect.y -= self.speed
                        if self.angle == 0:
                            self.angle = 180
                            self.picture(90)
                            self.angle = 360
                        elif self.angle == 180:
                            self.angle = 360
                            self.picture(90)
                            self.angle = 360
                        elif self.angle == 90:
                            self.angle = 270
                            self.picture(90)
                            self.angle = 360
                        else:
                            self.angle = 360
                    elif self.rect.y < self.NPSy:
                        self.rect.y += self.speed
                        if self.angle == 0:
                            self.angle = 360
                            self.picture(90)
                            self.angle = 90
                        elif self.angle == 180:
                            self.angle = 180
                            self.picture(90)
                            self.angle = 90
                        elif self.angle == 360:
                            self.angle = 270
                            self.picture(90)
                            self.angle = 90
                        else:
                            self.angle = 90
                    elif self.rect.y == self.NPSy:
                        self.quantity = 0
    def update(self):
        if hero.rect.x - self.rect.x >= 150 and hero.rect.y - self.rect.y >= 100:
            self.updater()
        elif hero.rect.x - self.rect.x >= 150 and self.rect.y - hero.rect.y >= 100:
            self.updater()
        elif self.rect.x - hero.rect.x >= 150 and hero.rect.y - self.rect.y >= 100:
            self.updater()
        elif self.rect.x - hero.rect.x >= 150 and self.rect.y - hero.rect.y >= 100:
            self.updater()
        else:
            if self.rect.x % self.speed != 0:
                self.rect.x -= 1
            elif hero.rect.x % hero.speed != 0:
                hero.rect.x -= 1 
            elif self.rect.y % self.speed != 0:
                self.rect.y -= 1
            elif hero.rect.y % hero.speed != 0:
                hero.rect.y -= 1 
            else:
                if hero.rect.x <= self.rect.x:
                    self.rect.x -= self.speed
                    if self.angle == 0:
                        self.angle = 270
                        self.picture(90)
                        self.angle = 180
                    elif self.angle == 90:
                        self.angle = 360
                        self.picture(90)
                        self.angle = 180
                    elif self.angle == 360:
                        self.angle = 180
                        self.picture(90)
                        self.angle = 180
                    else:
                        self.angle = 180
                if hero.rect.x >= self.rect.x:
                    self.rect.x += self.speed
                    if self.angle == 180:
                        self.angle = 270
                        self.picture(90)
                        self.angle = 0
                    elif self.angle == 360:
                        self.angle = 360
                        self.picture(90)
                        self.angle = 0
                    elif self.angle == 90:
                        self.angle = 180
                        self.picture(90)
                        self.angle = 0
                    else:
                        self.angle = 0
                if hero.rect.y <= self.rect.y:
                    self.rect.y -= self.speed
                    if self.angle == 0:
                        self.angle = 180
                        self.picture(90)
                        self.angle = 360
                    elif self.angle == 180:
                        self.angle = 360
                        self.picture(90)
                        self.angle = 360
                    elif self.angle == 90:
                        self.angle = 270
                        self.picture(90)
                        self.angle = 360
                    else:
                        self.angle = 360
                if hero.rect.y >= self.rect.y:
                    self.rect.y += self.speed
                    if self.angle == 0:
                        self.angle = 360
                        self.picture(90)
                        self.angle = 90
                    elif self.angle == 180:
                        self.angle = 180
                        self.picture(90)
                        self.angle = 90
                    elif self.angle == 360:
                        self.angle = 270
                        self.picture(90)
                        self.angle = 90
                    else:
                            self.angle = 90
                            
    def picture(self, angle):
        self.angle = (self.angle - angle) % 360
        self.image = transform.rotate(self.image, self.angle)
        