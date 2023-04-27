from pygame import*
width = 700
height = 500

init()
window = display.set_mode((width, height))

class Sprite(sprite.Sprite):
    def __init__(self, x, y, size, img_link=False):
        super().__init__()
        self.size = size # (w,h)
        if img_link:
            self.image = transform.scale(image.load(img_link), self.size)
        else:
            self.image = Surface([size[0],size[1]])
            self.image.fill((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def setColor(self, color):
        self.image.fill(color)
    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    def update(self):
        pass