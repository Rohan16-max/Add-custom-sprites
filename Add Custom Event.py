import pygame
import random


pygame.init()


screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Sprite Color Change ")


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)


CHANGE_COLOR = pygame.USEREVENT + 1


class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, x, y):
        super().__init__()
        self.image = pygame.Surface((50, 50)) 
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.color = color

    def change_color(self):
        """Change the sprite color randomly."""
        colors = [RED, GREEN, BLUE, YELLOW]
        self.color = random.choice(colors)
        self.image.fill(self.color)


sprite1 = Sprite(RED, 100, 100)
sprite2 = Sprite(GREEN, 200, 200)


all_sprites = pygame.sprite.Group()
all_sprites.add(sprite1, sprite2)


pygame.time.set_timer(CHANGE_COLOR, 3000)


running = True
while running:
    screen.fill(WHITE)  

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
        if event.type == CHANGE_COLOR:
            sprite1.change_color()
            sprite2.change_color()

    
    all_sprites.update()
    all_sprites.draw(screen)

    
    pygame.display.flip()

    
    pygame.time.Clock().tick(60)


pygame.quit()
