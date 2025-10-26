from pygame import *
from random import *
font.init()


mod = 3


spis = list()
spis.append('sand.png')
spis.append('diamond.png')
spis.append('emerald.png')
spis.append('heaven.png')

class GameSprite(sprite.Sprite):
    def __init__(self,f_name = 'rocket.png',speed = 5,x = 350,y = 400,x_size =50,y_size = 80):
        super().__init__()
        self.image  = transform.scale(image.load(f_name),(x_size,y_size))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):

        window.blit(self.image,(self.rect.x,self.rect.y))
    def restart(self,x,y):
        self.rect.x = x
        self.rect.y = y
    def killing(self):
        self.kill()
class Platform(GameSprite):
    def update_1(self):
        key_p = key.get_pressed()
        if key_p[K_UP] and self.rect.y >= 0:
            self.rect.y-=self.speed
        if key_p[K_DOWN] and self.rect.y <= 500:
            self.rect.y+=self.speed
    def update_2(self):
        key_p = key.get_pressed()
        if key_p[K_w] and self.rect.y >= 0:
            self.rect.y-=self.speed
        if key_p[K_s] and self.rect.y <= 500:
            self.rect.y+=self.speed
    def change(self,spis,counter,ab):
            f_name = spis[ab]
            self.image = transform.scale(image.load(f_name),(self.rect.width,self.rect.height))


class Ball(GameSprite):
    def __init__(self,f_name = 'ball.png',speed = 8,x = 250, y = 250, x_size = 50,y_size = 50):
        super().__init__(f_name,speed,x,y,x_size,y_size)
        self.speedx = speed
        self.speedy = speed
    
    def update(self,platforma_1,platforma_2):
        self.rect.x +=self.speedx
        self.rect.y +=self.speedy
        if sprite.collide_rect(self,platforma_1) == True:
            self.speedx*=-1
            a_s = abs(self.speedx)
            self.speedx = randint(2,7)*self.speedx//a_s
            self.rect.x += self.speed
        elif sprite.collide_rect(self,platforma_2) == True:
            self.speedx*=-1
            self.rect.x -= self.speed
        if self.rect.y >= 490 or self.rect.y <= 10:
            self.speedy *=-1
            b_s = abs(self.speedy)
            self.rect.y +=self.speedy
            self.speedy = randint(2,9)*self.speedy//b_s


        


platforma_1 = Platform(f_name = 'rectsd.png',speed = 7, x = 50, y = 250, x_size = 40, y_size = 150)
platforma_2 = Platform(f_name = 'rectsd.png',speed = 7, x = 600, y = 250, x_size = 40, y_size = 150)
ball = Ball()


schet_1 = 0
schet_2 = 0 

window = display.set_mode((700,500))
display.set_caption('Пин понг')
game = True 
finish = False
fps = 60
clock = time.Clock()

count = 0
counter_91 = 0
counter_92 = 0


font_1 = font.SysFont('Times New Roman',70)
text = 'Player 1 won'
text_2 = 'Player 2 won'
won_1 = font_1.render(text,True,(0,0,0))
won_2 = font_1.render(text_2,True,(0,0,0))
back = transform.scale(image.load('пляж.jpg'),(700,500))
scorer_1 = font_1.render(str(schet_1),True,(0,0,0))
scorer_2 = font_1.render(str(schet_2),True,(0,0,0))
underscorer_1 = font_1.render(str(counter_91),True,(0,255,255))
underscorer_2 = font_1.render(str(counter_92),True,(0,255,255))

window.blit(scorer_1,(50,50))
window.blit(scorer_2,(600,50))
window.blit(underscorer_1,(50,400))
window.blit(underscorer_2,(600,400))

window.blit(back,(0,0))
while game:
    window.blit(back,(0,0))
    window.blit(scorer_1,(50,50))
    window.blit(scorer_2,(600,50))
    window.blit(underscorer_1,(50,400))
    window.blit(underscorer_2,(600,400))
    clock.tick(fps)
    events = event.get()
    for e in events:
        if e.type == QUIT:
            game = False
    if finish == False:
        platforma_1.update_2()
        platforma_2.update_1()
        platforma_1.reset()
        platforma_2.reset()
        ball.update(platforma_1,platforma_2)
        ball.reset()
        if ball.rect.x >=690:
            ball.restart(250,250)
            ball.speedx*=-1
            schet_1+=1
            scorer_1 = font_1.render(str(schet_1),True,(0,0,0))
            if schet_1 == 3:
                counter_91 +=1
                a_s = min(counter_91//mod,len(spis) - 1)                
                platforma_1.change(spis,counter_91,a_s) 



                underscorer_1 = font_1.render(str(counter_91),True,(0,255,255))
                finish = True


        elif ball.rect.x<=10:
            ball.restart(250,250)
            ball.speedx*=-1
            schet_2+=1
            scorer_2 = font_1.render(str(schet_2),True,(0,0,0))
            if schet_2 == 3:
                counter_92 +=1
                v_s = min(counter_92//mod,len(spis) - 1)   
                platforma_2.change(spis,counter_92,v_s)  




                underscorer_2 = font_1.render(str(counter_92),True,(0,255,255))
                finish = True
            
    if finish == True:
        count += 1
        if schet_1 == 3:
            window.blit(won_1,(200,250))
        if schet_2 == 3:
            window.blit(won_2,(200,250))
            
        if count == 300:
            finish = False
            count = 0 
            schet_1 = 0
            schet_2 = 0
            scorer_1 = font_1.render(str(schet_1),True,(0,0,0))
            scorer_2 = font_1.render(str(schet_2),True,(0,0,0))
            underscorer_1 = font_1.render(str(counter_91),True,(0,255,255))
            underscorer_2 = font_1.render(str(counter_92),True,(0,255,255))


        
        




    
    display.update()

display.update()
