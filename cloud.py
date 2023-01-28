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


# running = True
# screen.fill((255, 255, 255))
# sheet = load_image("all.png")
# all_sprites = pygame.sprite.Group()
# cloud1 = CloudSprite(all_sprites, sheet, cloud_speed, 0, random.randint(30, 70))
# cloud2 = CloudSprite(all_sprites, sheet, cloud_speed, 200, random.randint(30, 70))
# cloud3 = CloudSprite(all_sprites, sheet, cloud_speed, 400, random.randint(30, 70))
# road_start = RoadSprite(all_sprites, sheet, road_speed, 0, 129)
# road_end = RoadSprite(all_sprites, sheet, road_speed, road_start.width, 129)
# clock = pygame.time.Clock()
# fps = 24
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#     screen.fill((255, 255, 255))
#     all_sprites.update()
#     all_sprites.draw(screen)
#     clock.tick(fps)
#     pygame.display.flip()