import pygame
import random


class CloudSprite(pygame.sprite.Sprite):
    def __init__(self, all_sprites, sheet, speed, x, y):
        super().__init__(all_sprites)
        self.width = 46
        self.image = sheet.subsurface(pygame.Rect(86, 2, self.width, 13))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
        self.action = True

    def update(self):
        if self.action:
            self.rect.x -= self.speed
            if self.rect.x + self.width < 0:
                self.rect.x = 600 + random.randint(0, 50)
                self.rect.y = random.randint(30, 70)

    def reinit(self, all_sprites, sheet, speed, x, y):
        self.__init__(all_sprites, sheet, speed, x, y)