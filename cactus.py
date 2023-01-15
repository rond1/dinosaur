import pygame
import random


class CactusSprite(pygame.sprite.Sprite):
    def __init__(self, all_sprites, sheet, speed, x, y):
        super().__init__(all_sprites)
        self.random_size = [[[230, 3, 15, 33], [246, 3, 32, 33], [280, 3, 49, 33]],
                       [[333, 3, 23, 46], [356, 3, 50, 46], [408, 3, 73, 46]]]
        self.part_of_sheet = random.choice(random.choice(self.random_size))
        self.image = sheet.subsurface(pygame.Rect([333, 3, 23, 46]))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.sheet = sheet
        self.speed = speed

    def update(self):
        self.rect.x -= self.speed
        if self.rect.x + self.part_of_sheet[2] < 0:
            self.part_of_sheet = random.choice(random.choice(self.random_size))
            self.image = self.sheet.subsurface(pygame.Rect(self.part_of_sheet))
            self.rect = self.image.get_rect()
            self.rect.x = 600
            if self.part_of_sheet not in self.random_size[0]:
                self.rect.y = 97
            else:
                self.rect.y = 108
