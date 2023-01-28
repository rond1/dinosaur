import os
import sys

import pygame
import random

from road import RoadSprite
from cloud import CloudSprite
from barrier import BarrierSprite
from dino import DinoSprite
from ending import ArrowSprite, GameoverSprite
from symbols import ScoreSprite, LettersSprite


size = width, height = 600, 150
speed = 9
dino_max_height = 97
dino_g = 2
fps = 24
fpp = 4
file_score = os.path.join('data', 'high_score.txt')


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


new_game = False
score = 0
high_score = score
frames = 0
stop = False
running = True
screen.fill((255, 255, 255))
sheet = load_image("all.png")
all_sprites = pygame.sprite.Group()
cloud1 = CloudSprite(all_sprites, sheet, speed // 3, 0, random.randint(30, 70))
cloud2 = CloudSprite(all_sprites, sheet, speed // 3, 200, random.randint(30, 70))
cloud3 = CloudSprite(all_sprites, sheet, speed // 3, 400, random.randint(30, 70))
road_start = RoadSprite(all_sprites, sheet, speed, 0, 129)
road_end = RoadSprite(all_sprites, sheet, speed, road_start.width, 129)
dino = DinoSprite(all_sprites, sheet, 20, 97, dino_g, dino_max_height)
barrier1 = BarrierSprite(all_sprites, sheet, speed, 600, 97)
barrier2 = BarrierSprite(all_sprites, sheet, speed, 900, 97)
barrier3 = BarrierSprite(all_sprites, sheet, speed, 1200, 97)
letters = LettersSprite(all_sprites, sheet, 440, 5)
score_sprite1 = ScoreSprite(all_sprites, sheet, 530, 5, score, 0)
score_sprite2 = ScoreSprite(all_sprites, sheet, 540, 5, score, 1)
score_sprite3 = ScoreSprite(all_sprites, sheet, 550, 5, score, 2)
score_sprite4 = ScoreSprite(all_sprites, sheet, 560, 5, score, 3)
score_sprite5 = ScoreSprite(all_sprites, sheet, 570, 5, score, 4)
with open(file_score, 'r') as f:
    old_data = f.read()
    score_sprite6 = ScoreSprite(all_sprites, sheet, 470, 5, int(old_data), 0)
    score_sprite7 = ScoreSprite(all_sprites, sheet, 480, 5, int(old_data), 1)
    score_sprite8 = ScoreSprite(all_sprites, sheet, 490, 5, int(old_data), 2)
    score_sprite9 = ScoreSprite(all_sprites, sheet, 500, 5, int(old_data), 3)
    score_sprite10 = ScoreSprite(all_sprites, sheet, 510, 5, int(old_data), 4)
ending_sprite1 = ArrowSprite(all_sprites, sheet, 284, 70)
ending_sprite1.new_game()
ending_sprite2 = GameoverSprite(all_sprites, sheet, 205, 30)
ending_sprite2.new_game()
clock = pygame.time.Clock()
current_speed = speed

while running:
    if dino.action:
        frames += 1
        new_game = False
        score = int(frames / fpp / speed * current_speed)
        score_sprite1.score = '0' * (5 - len(str(score))) + str(score)
        score_sprite2.score = '0' * (5 - len(str(score))) + str(score)
        score_sprite3.score = '0' * (5 - len(str(score))) + str(score)
        score_sprite4.score = '0' * (5 - len(str(score))) + str(score)
        score_sprite5.score = '0' * (5 - len(str(score))) + str(score)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if new_game:
                cloud1.reinit(all_sprites, sheet, speed // 3, 0, random.randint(30, 70))
                cloud2.reinit(all_sprites, sheet, speed // 3, 200, random.randint(30, 70))
                cloud3.reinit(all_sprites, sheet, speed // 3, 400, random.randint(30, 70))
                road_start.reinit(all_sprites, sheet, speed, 0, 129)
                road_end.reinit(all_sprites, sheet, speed, road_start.width, 129)
                dino.reinit(all_sprites, sheet, 20, 97, dino_g, dino_max_height)
                barrier1.reinit(all_sprites, sheet, speed, 600, 97)
                barrier2.reinit(all_sprites, sheet, speed, 900, 97)
                barrier3.reinit(all_sprites, sheet, speed, 1200, 97)
                ending_sprite1.new_game()
                ending_sprite2.new_game()
                score_sprite1.reinit(all_sprites, sheet, 530, 5, score, 0)
                score_sprite2.reinit(all_sprites, sheet, 540, 5, score, 1)
                score_sprite3.reinit(all_sprites, sheet, 550, 5, score, 2)
                score_sprite4.reinit(all_sprites, sheet, 560, 5, score, 3)
                score_sprite5.reinit(all_sprites, sheet, 570, 5, score, 4)

                score_sprite6.reinit(all_sprites, sheet, 470, 5, high_score, 0)
                score_sprite7.reinit(all_sprites, sheet, 480, 5, high_score, 1)
                score_sprite8.reinit(all_sprites, sheet, 490, 5, high_score, 2)
                score_sprite9.reinit(all_sprites, sheet, 500, 5, high_score, 3)
                score_sprite10.reinit(all_sprites, sheet, 510, 5, high_score, 4)
                score = 0
                frames = 0
            else:
                if not dino.jumping:
                    dino.jumping = True
                    dino.time = 0
    screen.fill((255, 255, 255))
    all_sprites.update()
    all_sprites.draw(screen)
    if pygame.sprite.collide_mask(dino, barrier1) or pygame.sprite.collide_mask(dino, barrier2) or \
            pygame.sprite.collide_mask(dino, barrier3):
        cloud1.action = False
        cloud2.action = False
        cloud3.action = False
        road_end.action = False
        road_start.action = False
        barrier1.action = False
        barrier2.action = False
        barrier3.action = False
        dino.action = False
        if score > high_score:
            with open(file_score, 'w') as f:
                f.write('0' * (5 - len(str(score))) + str(score))
            high_score = score
        new_game = True
        ending_sprite1.reinit(all_sprites, sheet, 284, 70)
        ending_sprite2.reinit(all_sprites, sheet, 205, 30)
    current_speed = speed + score // 100
    road_start.speed = current_speed
    road_end.speed = current_speed
    barrier1.speed = current_speed
    barrier2.speed = current_speed
    barrier3.speed = current_speed
    cloud1.speed = current_speed // 3
    cloud2.speed = current_speed // 3
    cloud3.speed = current_speed // 3
    clock.tick(fps)
    pygame.display.flip()
