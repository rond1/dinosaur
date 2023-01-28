import pygame


class ArrowSprite(pygame.sprite.Sprite):
    def __init__(self, all_sprites, sheet, x, y):
        super().__init__(all_sprites)
        self.image = sheet.subsurface(pygame.Rect(3, 3, 33, 33))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def new_game(self):
        self.rect.y = 200

    def reinit(self, all_sprites, sheet, x, y):
        self.__init__(all_sprites, sheet, x, y)


class GameoverSprite(pygame.sprite.Sprite):
    def __init__(self, all_sprites, sheet, x, y):
        super().__init__(all_sprites)
        self.image = sheet.subsurface(pygame.Rect(655, 15, 190, 11))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def new_game(self):
        self.rect.y = 200

    def reinit(self, all_sprites, sheet, x, y):
        self.__init__(all_sprites, sheet, x, y)