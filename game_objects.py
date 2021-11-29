import pygame as pg
import sys
import time

import game_objects

pg.init()


def load_image(image:str, scale_x, scale_y, alpha=False):
    if alpha:
        output = pg.image.load(image).convert_alpha()
    else:
        output = pg.image.load(image).convert()
    return pg.transform.scale(output, (scale_x, scale_y))

#
# class Player(pg.sprite.Sprite):
#     def __init__(self, surface, image, x, y):
#         pg.sprite.Sprite.__init__(self)
#         int_image = load_image(image, 116, 121, True)
#         surface.blit(int_image, (x, y))


class Player(pg.sprite.Sprite):
    var = 0

    def __init__(self, screen, *groups):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load("viking.png").convert_alpha()
        self.image = pg.transform.scale(self.image, (116, 121))
        self.rect = self.image.get_rect()
        self.screen = screen
        self.rect.y = self.screen.get_size()[1]

    def update(self):
        # handles movement of the player,
        # dist is the pixel distance moved when the method is called
        dist = 1
        x = self.rect.x
        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            self.rect.y -= dist
        if keys[pg.K_a]:
            self.rect.x -= dist
        if keys[pg.K_s]:
            self.rect.y += dist
        if keys[pg.K_d]:
            self.rect.x += dist
        if x > self.rect.x and self.var == 0:
            self.image = pg.transform.flip(self.image, True, False)
            self.var = 1
        if x < self.rect.x and self.var == 1:
            self.image = pg.transform.flip(self.image, True, False)
            self.var = 0
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.y < 0:
            self.rect.y = 0
        if self.rect.x > self.screen.get_size()[0]-self.image.get_size()[0]:
            self.rect.x = self.screen.get_size()[0]-self.image.get_size()[0]
        if self.rect.y > self.screen.get_size()[1]-self.image.get_size()[1]:
            self.rect.y = self.screen.get_size()[1]-self.image.get_size()[1]
