import pygame


class RoadSprite(pygame.sprite.Sprite):
    def __init__(self, all_sprites, sheet, speed, x, y):
        super().__init__(all_sprites)
        self.width = 1199
        self.image = sheet.subsurface(pygame.Rect(2, 54, self.width, 12))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
        self.action = True
        self.count = 0

    def update(self):
        if self.action:
            self.rect.x -= self.speed
            if self.rect.x + self.width < 0:
                self.rect.x = self.width
            self.count += self.speed
