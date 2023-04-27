from Sprite import*

width = 700
height = 500


class Bullet(Sprite):
    def __init__(self, x, y, angle):
        self.angle = angle
        super().__init__(x, y, (10, 10))
        self.speed = 5
        self.rect.x = x
        self.rect.y = y
        self.size = (10, 10)
        self.offset = 30
    def update(self):
        if self.angle == 0:
            self.rect.x += self.speed      
        elif self.angle == 180:
            self.rect.x -= self.speed
        elif self.angle == 90:
            self.rect.y += self.speed
        elif self.angle == 360:
            self.rect.y -= self.speed
    def kill(self):
        if self.rect.x >= width - self.offset - self.size[0]:
            removebull = True
            return removebull
        elif self.rect.x <= self.size[0]:
            removebull = True
            return removebull
        elif self.rect.y >= height - self.offset - self.size[1]:
            removebull = True
            return removebull
        elif self.rect.y <= self.size[1]:
            removebull = True
            return removebull

    


    

        
