import os
import sys

import pygame
import random

from road import RoadSprite
from cloud import CloudSprite
from barrier import BarrierSprite


size = width, height = 600, 150
cloud_speed = 3
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


class DinoSprite(pygame.sprite.Sprite):
    def __init__(self, all_sprites, sheet, x, y):
        super().__init__(all_sprites)
        self.sheet = sheet
        self.image = sheet.subsurface(pygame.Rect(938, 4, 40, 42))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.position = 1
        self.count = 0
        self.jumping = False
        self.direction_up = True

    def update(self):
        if self.jumping:
            self.image = self.sheet.subsurface(pygame.Rect(850, 4, 40, 42))
            if self.direction_up:
                self.rect.y -= 7
                if self.rect.y == 27:
                    self.direction_up = False
            elif self.rect.y == 17 and self.count < 7:
                self.count += 1
            else:
                self.rect.y += 7
                if self.rect.y == 97:
                    self.position = 1
                    self.count = 0
                    self.jumping = False
                    self.direction_up = True
        elif self.count % 5 == 0:
            self.jumping = False
            self.rect.y = 97
            if self.position:
                self.image = self.sheet.subsurface(pygame.Rect(982, 4, 40, 42))
                self.position = 0
            else:
                self.image = self.sheet.subsurface(pygame.Rect(938, 4, 40, 42))
                self.position = 1
        self.count += 1


running = True
screen.fill((255, 255, 255))
sheet = load_image("all.png")
all_sprites = pygame.sprite.Group()
cloud1 = CloudSprite(all_sprites, sheet, cloud_speed, 0, random.randint(30, 70))
cloud2 = CloudSprite(all_sprites, sheet, cloud_speed, 200, random.randint(30, 70))
cloud3 = CloudSprite(all_sprites, sheet, cloud_speed, 400, random.randint(30, 70))
road_start = RoadSprite(all_sprites, sheet, road_speed, 0, 129)
road_end = RoadSprite(all_sprites, sheet, road_speed, road_start.width, 129)
dino = DinoSprite(all_sprites, sheet, 20, 97)
barrier1 = BarrierSprite(all_sprites, sheet, road_speed, 600, 97)
barrier2 = BarrierSprite(all_sprites, sheet, road_speed, 900, 97)
barrier3 = BarrierSprite(all_sprites, sheet, road_speed, 1200, 97)
clock = pygame.time.Clock()
fps = 24
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            dino.jumping = True
            dino.count = 0
    screen.fill((255, 255, 255))
    all_sprites.update()
    all_sprites.draw(screen)
    clock.tick(fps)
    pygame.display.flip()
