from pygame import*
from Character import*
from Bullet import*

bullets = []

class Player(Character):
    def __init__(self, x, y, img_link=False):
        self.size = (50,50)
        self.hp = 3000
        self.speed = 3
        self.angle = 0
        self.offset = 30
        self.amount_ammo = 100
        super().__init__(self.speed, self.hp, x, y, self.size, img_link)
        self.x = self.rect.x
        self.y = self.rect.y
        self.bullfire = True
        self.firedelay = 0
    def update(self):
        if self.firedelay > 0:
            self.firedelay -= 1
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x > self.offset:
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
        if keys[K_d] and self.rect.x < width - self.size[0] - self.offset:
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
            self.rect.x += self.speed
        if keys[K_w] and self.rect.y > self.offset:
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
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < height - self.size[1] - self.offset:
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
            self.rect.y += self.speed
        if keys[K_LSHIFT]:
            self.speed = 5
        else:
            self.speed = self.normalspeed
        if keys[K_LCTRL] and self.firedelay == 0 and self.bullfire:
            self.firedelay = 10
            self.fire()
            self.amount_ammo -= 1
            if self.amount_ammo == 0:
                self.bullfire = False
            else:
                self.bullfire = True
        if keys[K_0]:
            self.amount_ammo = 100
            self.bullfire = True
        print(self.rect.x)
    def picture(self, angle):
        self.angle = (self.angle - angle) % 360
        self.image = transform.rotate(self.image, self.angle)
    def fire(self):
        bullet = Bullet(self.rect.centerx, self.rect.top, self.angle)  
        bullets.append(bullet)
         
        