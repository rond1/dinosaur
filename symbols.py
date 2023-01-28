import pygame


class ScoreSprite(pygame.sprite.Sprite):
    def __init__(self, all_sprites, sheet, x, y, score, index):
        super().__init__(all_sprites)
        self.sheet = sheet
        self.action = True
        self.index = index
        self.dict_of_numbers = {'0': [655, 2, 9, 10], '1': [665, 2, 9, 10], '2': [675, 2, 9, 10],
                                '3': [685, 2, 9, 10], '4': [695, 2, 9, 10], '5': [705, 2, 9, 10],
                                '6': [715, 2, 9, 10], '7': [725, 2, 9, 10], '8': [735, 2, 9, 10],
                                '9': [745, 2, 9, 10]}
        self.score = '0' * (5 - len(str(score))) + str(score)
        self.image = self.sheet.subsurface(pygame.Rect(self.dict_of_numbers[self.score[self.index]]))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        if self.action:
            self.image = self.sheet.subsurface(pygame.Rect(self.dict_of_numbers[self.score[self.index]]))

    def reinit(self, all_sprites, sheet, x, y, score, index):
        self.__init__(all_sprites, sheet, x, y, score, index)


class LettersSprite(pygame.sprite.Sprite):
    def __init__(self, all_sprites, sheet, x, y):
        super().__init__(all_sprites)
        self.image = sheet.subsurface(pygame.Rect(755, 2, 18, 10))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y