import pygame, sys 
import random
import time

WHITE = (255, 255, 255)
PIXELS= 130
TIME1 = 38
TIME2 = 18
POINT1 = 10
POINT2 = 20

class Crosshair(pygame.sprite.Sprite):
    def __init__(self, picture_path):
        super().__init__()
        self.image = pygame.image.load(picture_path).convert_alpha()
        self.rect = self.image.get_rect()
        self.gunshot = pygame.mixer.Sound('gunshot.wav')
        
    def update(self):
        self.rect.center = pygame.mouse.get_pos()
        
    def shoot(self):
        # self.gunshot.play()
        pygame.mixer.Channel(1).play(self.gunshot)
        return pygame.sprite.spritecollide(crosshair, target_group, True)

class Target(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.sprites = []
        self.is_animating = False
        self.missed = False
        self.sprites.append(pygame.image.load("appear_1.png").convert_alpha())
        self.sprites.append(pygame.image.load("appear_2.png").convert_alpha())
        self.sprites.append(pygame.image.load("appear_3.png").convert_alpha())
        self.sprites.append(pygame.image.load("appear_4.png").convert_alpha())
        self.sprites.append(pygame.image.load("appear_5.png").convert_alpha())
        self.sprites.append(pygame.image.load("appear_6.png").convert_alpha())
        self.sprites.append(pygame.image.load("appear_7.png").convert_alpha())
        self.sprites.append(pygame.image.load("appear_8.png").convert_alpha())
        self.sprites.append(pygame.image.load("appear_9.png").convert_alpha())
        self.sprites.append(pygame.image.load("appear_10.png").convert_alpha())
        self.sprites.append(pygame.image.load("appear_11.png").convert_alpha())
        self.sprites.append(pygame.image.load("idle_1.png").convert_alpha())
        self.sprites.append(pygame.image.load("idle_2.png").convert_alpha())
        self.sprites.append(pygame.image.load("idle_3.png").convert_alpha())
        self.sprites.append(pygame.image.load("idle_4.png").convert_alpha())
        self.sprites.append(pygame.image.load("idle_5.png").convert_alpha())
        self.sprites.append(pygame.image.load("idle_6.png").convert_alpha())
        self.sprites.append(pygame.image.load("idle_1.png").convert_alpha())
        self.sprites.append(pygame.image.load("idle_2.png").convert_alpha())
        self.sprites.append(pygame.image.load("idle_3.png").convert_alpha())
        self.sprites.append(pygame.image.load("idle_4.png").convert_alpha())
        self.sprites.append(pygame.image.load("idle_5.png").convert_alpha())
        self.sprites.append(pygame.image.load("idle_6.png").convert_alpha())
        self.sprites.append(pygame.image.load("idle_1.png").convert_alpha())
        self.sprites.append(pygame.image.load("idle_2.png").convert_alpha())
        self.sprites.append(pygame.image.load("idle_3.png").convert_alpha())
        self.sprites.append(pygame.image.load("idle_4.png").convert_alpha())
        self.sprites.append(pygame.image.load("idle_5.png").convert_alpha())
        self.sprites.append(pygame.image.load("idle_6.png").convert_alpha())
        self.sprites.append(pygame.image.load("idle_1.png").convert_alpha())
        self.sprites.append(pygame.image.load("idle_2.png").convert_alpha())
        self.sprites.append(pygame.image.load("idle_3.png").convert_alpha())
        self.sprites.append(pygame.image.load("idle_4.png").convert_alpha())
        self.sprites.append(pygame.image.load("idle_5.png").convert_alpha())
        self.sprites.append(pygame.image.load("idle_6.png").convert_alpha())
        self.sprites.append(pygame.image.load("idle_1.png").convert_alpha())
        self.sprites.append(pygame.image.load("idle_2.png").convert_alpha())
        self.sprites.append(pygame.image.load("idle_3.png").convert_alpha())
        self.sprites.append(pygame.image.load("idle_4.png").convert_alpha())
        self.sprites.append(pygame.image.load("idle_5.png").convert_alpha())
        self.sprites.append(pygame.image.load("idle_6.png").convert_alpha())
        self.sprites.append(pygame.image.load("idle_1.png").convert_alpha())
        self.sprites.append(pygame.image.load("idle_2.png").convert_alpha())
        self.sprites.append(pygame.image.load("idle_3.png").convert_alpha())
        self.sprites.append(pygame.image.load("idle_4.png").convert_alpha())
        self.sprites.append(pygame.image.load("idle_5.png").convert_alpha())
        self.sprites.append(pygame.image.load("idle_6.png").convert_alpha())
        self.sprites.append(pygame.image.load("idle_1.png").convert_alpha())
        self.sprites.append(pygame.image.load("idle_2.png").convert_alpha())
        self.sprites.append(pygame.image.load("idle_3.png").convert_alpha())
        self.sprites.append(pygame.image.load("idle_4.png").convert_alpha())
        self.sprites.append(pygame.image.load("idle_5.png").convert_alpha())
        self.sprites.append(pygame.image.load("idle_6.png").convert_alpha())
        self.sprites.append(pygame.image.load("idle_1.png").convert_alpha())
        self.sprites.append(pygame.image.load("idle_2.png").convert_alpha())
        self.sprites.append(pygame.image.load("idle_3.png").convert_alpha())
        self.sprites.append(pygame.image.load("idle_4.png").convert_alpha())
        self.sprites.append(pygame.image.load("idle_5.png").convert_alpha())
        self.sprites.append(pygame.image.load("idle_6.png").convert_alpha())
        self.sprites.append(pygame.image.load("appear_10.png").convert_alpha())
        self.sprites.append(pygame.image.load("appear_9.png").convert_alpha())
        self.sprites.append(pygame.image.load("appear_8.png").convert_alpha())
        self.sprites.append(pygame.image.load("appear_7.png").convert_alpha())
        self.sprites.append(pygame.image.load("appear_6.png").convert_alpha())
        self.sprites.append(pygame.image.load("appear_5.png").convert_alpha())
        self.sprites.append(pygame.image.load("appear_4.png").convert_alpha())
        self.sprites.append(pygame.image.load("appear_3.png").convert_alpha())
        self.sprites.append(pygame.image.load("appear_2.png").convert_alpha())
        self.sprites.append(pygame.image.load("appear_1.png").convert_alpha())
        self.sprites.append(pygame.image.load("miss.png").convert_alpha())
        self.sprites.append(pygame.image.load("miss.png").convert_alpha())
        self.sprites.append(pygame.image.load("miss.png").convert_alpha())
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]
        
    def update(self):
        if self.is_animating == True:
            self.current_sprite += 1
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
                self.is_animating = False
                self.image = pygame.image.load("miss.png").convert_alpha()
                self.missed = True
            else:
                self.image = self.sprites[self.current_sprite]
    def killed(self):
        if self.missed == True:
            self.kill()
                
    def animate(self):
        self.is_animating = True
        
class Score:
    def __init__(self):
        self.points = 0
        self.miss_points = POINT1 + POINT2
        self.font = pygame.font.SysFont('monospace', 30, bold=False)
    
    def increase(self):
        self.points += 1
        self.miss_points -= 1
    
    def reset(self):
        self.points = 0
        self.miss_points = POINT1 + POINT2
    
    def show(self, surface):
        lbl = self.font.render('Score: ' + str(self.points) + '  Miss: ' + str(self.miss_points), 1, WHITE)    
        surface.blit(lbl, (5,5))
        
class GameState():
    def __init__(self):
        self.state = 'intro'
        self.count = 1
        self.update_target = TIME1
        self.game_audio = pygame.mixer.Sound('zombie.wav')
        self.game_ready = pygame.mixer.Sound('ready.wav')
    
    def intro(self):
        self.game_ready.play(loops = -1)
        self.game_audio.stop()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
            if event.type == pygame.MOUSEBUTTONDOWN:
                crosshair.shoot()
                self.state = 'game1'
                for i in range(1):
                    new_target = Target(random.randrange(PIXELS, screen_width-PIXELS, step= PIXELS), random.randrange(PIXELS, screen_height-PIXELS, step=PIXELS))
                    new_target.animate()
                    target_group.add(new_target)
                
        pygame.display.flip()
        screen.blit(background, (0,0))
        screen.blit(ready_text, (screen_width/2 - 225, screen_height/2 - 90))
        crosshair_group.draw(screen)
        crosshair_group.update()
        score.show(screen)
    
    def game1(self):
        self.game_ready.stop()
        self.game_audio.play(loops = -1)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
            if event.type == pygame.MOUSEBUTTONDOWN:
                shot = crosshair.shoot()
                if shot:
                    score.increase()     
        pygame.display.flip()
        screen.blit(background, (0,0))
        target_group.draw(screen)
        target_group.update()
        crosshair_group.draw(screen)
        crosshair_group.update()
        score.show(screen)
        self.update_target -= 1
        for target in target_group:
            target.killed()
        if self.count < POINT1 and self.update_target <=0:
            new_target = Target(random.randrange(PIXELS, screen_width-PIXELS, step= PIXELS), random.randrange(PIXELS, screen_height-PIXELS, step=PIXELS))
            new_target.animate()
            target_group.add(new_target) 
            self.count += 1  
            self.update_target = TIME1
        if len(target_group) == 0 and self.count == POINT1:
            self.count = 3
            self.state = 'game2'
            self.update_target = TIME2
            for i in range(3):
                new_target = Target(random.randrange(PIXELS, screen_width-PIXELS, step= PIXELS), random.randrange(PIXELS, screen_height-PIXELS, step=PIXELS))
                new_target.animate()
                target_group.add(new_target)
                
    
    def game2(self):
        self.game_ready.stop()
        self.game_audio.play(loops = -1)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
            if event.type == pygame.MOUSEBUTTONDOWN:
                shot = crosshair.shoot()
                if shot:
                    score.increase()
            
        pygame.display.flip()
        screen.blit(background, (0,0))
        target_group.draw(screen)
        target_group.update()
        crosshair_group.draw(screen)
        crosshair_group.update()
        score.show(screen)
        self.update_target -= 1
        for target in target_group:
            target.killed()
        if self.count < POINT2 and self.update_target <=0:
            new_target = Target(random.randrange(PIXELS, screen_width-PIXELS, step= PIXELS), random.randrange(PIXELS, screen_height-PIXELS, step=PIXELS))
            new_target.animate()
            target_group.add(new_target) 
            self.count += 1  
            self.update_target = TIME2
        if len(target_group) == 0 and self.count == POINT2:
            self.game_audio.stop()
            time.sleep(0.01)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
        
                if event.type == pygame.MOUSEBUTTONDOWN:
                    shot = crosshair.shoot()
                    score.reset()
                    self.state = 'intro'
                    self.count = 1
                    self.update_target = TIME1
    
    def state_manager(self):
        if self.state == 'intro':
            self.intro()
        if self.state == 'game1':
            self.game1()
        if self.state == 'game2':
            self.game2()
                
#General setup
pygame.init()
pygame.mixer.init()
clock = pygame.time.Clock()
game_state = GameState()
score = Score()

#Game Screen
screen_width = 1280
screen_height = 780
screen = pygame.display.set_mode((screen_width, screen_height))
background = pygame.image.load("BG1.png").convert_alpha()
ready_text = pygame.image.load("ready_text.png").convert_alpha()
pygame.mouse.set_visible(False)

#Crosshair
crosshair = Crosshair("crosshair.png") 
crosshair_group = pygame.sprite.Group()
crosshair_group.add(crosshair)

#Target
target_group = pygame.sprite.Group()

while True:
    game_state.state_manager()
    clock.tick(45) 