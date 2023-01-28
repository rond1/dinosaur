import pygame
import random


class BarrierSprite(pygame.sprite.Sprite):
    def __init__(self, all_sprites, sheet, speed, x, y):
        super().__init__(all_sprites)
        self.random_size = [[[230, 3, 15, 33], [246, 3, 32, 33], [280, 3, 49, 33]],
                            [[333, 3, 23, 46], [356, 3, 50, 46], [408, 3, 73, 46]], [[182, 4, 41, 25]],
                            [[230, 3, 15, 33], [246, 3, 32, 33], [280, 3, 49, 33]],
                            [[333, 3, 23, 46], [356, 3, 50, 46], [408, 3, 73, 46]],
                            [[230, 3, 15, 33], [246, 3, 32, 33], [280, 3, 49, 33]],
                            [[333, 3, 23, 46], [356, 3, 50, 46], [408, 3, 73, 46]]]
        self.part_of_sheet = [333, 3, 23, 46]
        self.image = sheet.subsurface(pygame.Rect([333, 3, 23, 46]))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.sheet = sheet
        self.speed = speed
        self.count = 0
        self.position = -1
        self.mask = pygame.mask.from_surface(self.image)
        self.action = True

    def update(self):
        if self.action:
            self.rect.x -= self.speed
            if self.rect.x < -150:
                self.part_of_sheet = random.choice(random.choice(self.random_size))
                self.image = self.sheet.subsurface(pygame.Rect(self.part_of_sheet))
                self.rect = self.image.get_rect()
                self.rect.x = 750
                if self.part_of_sheet in self.random_size[1]:
                    self.rect.y = 97
                    self.position = -1
                elif self.part_of_sheet in self.random_size[0]:
                    self.rect.y = 108
                    self.position = -1
                else:
                    self.rect.y = random.choice([60, 75, 90])
                    self.count = 0
                    self.position = 1
            elif self.position >= 0:
                if self.count % 7 == 0:
                    if self.position:
                        self.image = self.sheet.subsurface(pygame.Rect(136, 4, 41, 37))
                        self.position = 0
                    else:
                        self.image = self.sheet.subsurface(pygame.Rect(182, 4, 41, 25))
                        self.position = 1
                self.count += 1