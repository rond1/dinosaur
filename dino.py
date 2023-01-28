import pygame


class DinoSprite(pygame.sprite.Sprite):
    def __init__(self, all_sprites, sheet, x, y, g, height):
        super().__init__(all_sprites)
        self.height = height
        self.sheet = sheet
        self.image = sheet.subsurface(pygame.Rect(938, 4, 40, 42))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.position = 1
        self.count = 0
        self.jumping = False
        self.mask = pygame.mask.from_surface(self.image)
        self.action = True
        self.time = 0
        self.g = g
        self.v0 = (2 * self.g * self.height) ** 0.5

    def update(self):
        if self.action:
            if self.jumping:
                self.time += 1
                self.image = self.sheet.subsurface(pygame.Rect(850, 4, 40, 42))
                self.rect.y = 97 - (self.v0 * self.time - (self.g * self.time ** 2) // 2)
                if self.rect.y >= 97:
                    self.rect.y = 97
                    self.jumping = False
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
        else:
            self.image = self.sheet.subsurface(pygame.Rect(1026, 4, 40, 42))

    def reinit(self, all_sprites, sheet, x, y, g, height):
        self.__init__(all_sprites, sheet, x, y, g, height)
