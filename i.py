from pygame import *

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
        
        


platforma_1 = Platform(f_name = 'rectsd.png',speed = 7, x = 50, y = 250, x_size = 40, y_size = 150)
platforma_2 = Platform(f_name = 'rectsd.png',speed = 7, x = 350, y = 250, x_size = 40, y_size = 150)


window = display.set_mode((500,500))
display.set_caption('Пин понг')
game = True 
finish = False
fps = 40
clock = time.Clock()
back = transform.scale(image.load('пляж.jpg'),(500,500))
window.blit(back,(0,0))
while game:
    window.blit(back,(0,0))
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
        




    
    display.update()

display.update()