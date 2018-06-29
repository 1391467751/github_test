import pygame ,sys
from pygame.locals import *
 
class ball:
    def __init__(self,surf,border):
        self.x = 0
        self.y = 0
        self.vx = 15
        self.vy = 15
        self.surface = surf
        self.surface.fill((0,0,0,0))
        self.border = border

    def position(self):
        return (self.x,self.y)

    def update(self):
        flag = False
        if(self.x+self.vx>self.border[1]-self.surface.get_size()[0]):
#            self.x = self.border[1]-self.surface.get_size()[0]
            self.vx=-self.vx
            flag = True
        if(self.y+self.vy>self.border[3]-self.surface.get_size()[1]):
#            self.y = self.border[3]-self.surface.get_size()[1]
            self.vy = -self.vy
            flag = True
        if(self.x+self.vx<self.border[0]):
#            self.x = self.border[0]
            self.vx=-self.vx
            flag = True            
        if(self.y+self.vy<self.border[2]):
#            self.y = self.border[2]
            self.vy = -self.vy
            flag = True
        if(flag == True):
            return
        self.x +=self.vx
        self.y +=self.vy
        return

    
        
width = 400
height = 300
pygame.init()
display = pygame.display.set_mode((width,height))
item = ball(pygame.Surface((50,50)).convert_alpha(),(0,width,0,height))
pygame.draw.circle(item.surface,(255,0,0),(25,25),25,0)

fontObj = pygame.font.Font('freesansbold.ttf',32)
txt = fontObj.render('HELLO PYTHON WORLD',True,(0,255,0),(0,0,0))
txt_rect =txt.get_rect()
txt_rect.center = (200,150)

'''
pixobj = pygame.PixelArray(display)
pixobj[300][200] = (255,255,255)
print ( display.get_locked())
pygame.draw.line(display,(255,255,255),(250,10),(10,250),4)
del pixobj
'''
fpsclock = pygame.time.Clock()

while True:
    item.update()
    for event in pygame.event.get():
        if event.type == QUIT :
            pygame.quit()
            sys.exit()
        if event.type ==MOUSEMOTION:
            print('mouse move to ',pygame.mouse.get_pos())
    display.fill((0,0,0))
    display.blit(txt,txt_rect)
    display.blit(item.surface,item.position())
    pygame.display.update()
    fpsclock.tick(60)

