import pygame as pg
import sys
import game_objects
import time

pg.init()

screen = pg.display.set_mode(flags=pg.FULLSCREEN)

image = pg.image.load("viking.png").convert_alpha()
image = pg.transform.scale(image, (116, 121))

bush = pg.image.load("bush.png").convert_alpha()

wordimg = pg.image.load("cigarette.png").convert_alpha()
wordimg = pg.transform.scale(wordimg, (50, 50))

background = pg.Surface(screen.get_size())
background.fill((250, 250, 250))

sprites = pg.sprite.Group()
player = game_objects.Player(screen)
sprites.add(player)


def main():

    while True:

        # Exit Window if Closed of ESC is pressed
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    sys.exit()

        # screen loading
        sprites.update()
        screen.blit(background, (0, 0))
        sprites.draw(screen)
        pg.display.update()
        print(player.rect.x, player.rect.y, image.get_size())


main()
