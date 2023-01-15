import os
import sys

import pygame
import random

from road import RoadSprite
from cloud import CloudSprite
from cactus import CactusSprite


size = width, height = 600, 150
cloud_speed = 5
road_speed = 7


pygame.init()
screen = pygame.display.set_mode(size)


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)

    if colorkey is not None:
        image = image.convert()
    if colorkey == -1:
        colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


class BirdSprite(pygame.sprite.Sprite):
    def __init__(self, all_sprites, sheet, speed, x, y):
        super().__init__(all_sprites)
        self.width = 41
        self.sheet = sheet
        self.image = sheet.subsurface(pygame.Rect(182, 4, self.width, 25))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
        self.count = 0
        self.position = 1

    def update(self):
        self.rect.x -= self.speed
        if self.count % 7 == 0:
            if self.position:
                self.image = self.sheet.subsurface(pygame.Rect(136, 10, self.width, 30))
                self.position = 0
            else:
                self.image = self.sheet.subsurface(pygame.Rect(182, 4, self.width, 25))
                self.position = 1
        if self.rect.x + self.width < 0:
            self.rect.x = 600
            self.rect.y = random.choice([10, 70, 90])
        self.count += 1


running = True
screen.fill((255, 255, 255))
sheet = load_image("all.png")
all_sprites = pygame.sprite.Group()
cloud1 = CloudSprite(all_sprites, sheet, cloud_speed, 0, random.randint(30, 70))
cloud2 = CloudSprite(all_sprites, sheet, cloud_speed, 200, random.randint(30, 70))
cloud3 = CloudSprite(all_sprites, sheet, cloud_speed, 400, random.randint(30, 70))
cactus1 = CactusSprite(all_sprites, sheet, road_speed, 600, 97)
bird = BirdSprite(all_sprites, sheet, road_speed, 600, random.choice([10, 70, 90]))
cactus2 = CactusSprite(all_sprites, sheet, road_speed, 900, 97)
road_start = RoadSprite(all_sprites, sheet, road_speed, 0, 129)
road_end = RoadSprite(all_sprites, sheet, road_speed, road_start.width, 129)
clock = pygame.time.Clock()
fps = 30
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((255, 255, 255))
    all_sprites.update()
    all_sprites.draw(screen)
    clock.tick(fps)
    pygame.display.flip()