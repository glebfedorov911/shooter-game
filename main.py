from pygame import*
from Player import*
from Enemy import*
from Bullet import*
from random import randint

enemy = [
Enemy(1, 100, randint(100, 650), randint(100, 450), (50, 50), "enemy1.png"),
Enemy(1, 100, randint(100, 650), randint(100, 450), (50, 50), "enemy1.png"),
Enemy(1, 100, randint(100, 650), randint(100, 450), (50, 50), "enemy1.png")
]

ulose = False

score = 0

hhp = str(hero.hp)


font.init()
font = font.Font(None, 15)
text1 = font.render("ХП:" + hhp, 1, (0, 0, 0))

objects = [hero]


lenemy = str(len(enemy))

text2 = font.render("Количество врагов:" + lenemy, 1, (0, 0, 0))
text3 = font.render("Количество патрон:" + str(hero.amount_ammo), 1, (0, 0, 0))
window.blit(text3, (10, 80)) 


# mixer.init()
# mixer.music.load("edm.mp3")
# mixer.music.play()

run = True
finish = False

while run:
    time.delay(10)
    for e in event.get():
        if e.type == QUIT:
            run = False
    
    window.fill((255, 255, 255))
    if not finish:

        text1 = font.render("ХП:" + hhp, 1, (0, 0, 0))
        text2 = font.render("Количество врагов:" + lenemy, 1, (0, 0, 0))
        text3 = font.render("Количество патрон:" + str(hero.amount_ammo), 1, (0, 0, 0))

        hhp = str(hero.hp)
        lenemy = str(len(enemy))
       
        for bull in bullets:
            bull.draw()
            bull.update()
            for e in enemy:
                if sprite.collide_rect(bull, e):
                    e.hp -= 10
                    if e.hp <= 0:
                        enemy.remove(e)
                    bullets.remove(bull)
                    break
                    
                   
        

            if bull.kill():
                bullets.remove(bull)

        for obj in objects:
            obj.draw()
            obj.update()  

        for e in enemy:
            e.draw()
            e.update()   
            if sprite.collide_rect(e, hero):
                hero.hp -= 1
                if hero.hp <= 0:
                    ulose = True

        window.blit(text1, (10, 20))
        window.blit(text2, (10, 50))
        window.blit(text3, (10, 80)) 
                    
    if ulose:    
        finish = True
        img = image.load("ulose.jpg")
        d = img.get_width() // img.get_width()
        window.fill((0, 0, 0))
        window.blit(transform.scale(img, (width * d, height)), (30, 0))

    if enemy == []:
        score += 100
        enemy = [
        Enemy(1, 100, randint(100, 650), randint(100, 450), (50, 50), "enemy1.png"),
        Enemy(1, 100, randint(100, 650), randint(100, 450), (50, 50), "enemy1.png"),
        Enemy(1, 100, randint(100, 650), randint(100, 450), (50, 50), "enemy1.png")
        ]
    
    if score == 1000:
        finish = True
        img = image.load("uwin.jpg")
        d = img.get_width() // img.get_width()
        window.fill((0, 0, 0))
        window.blit(transform.scale(img, (width * d, height)), (30, 0))



    display.update()