import pygame as pg
import sys
import pytmx
import game_objects
from pytmx.util_pygame import load_pygame
from pytmx import TiledTileLayer
import time
import test

pg.init()
clock = pg.time.Clock()

screen = pg.display.set_mode(flags=pg.FULLSCREEN)

bush = pg.image.load("bush.png").convert_alpha()

background = pg.Surface(screen.get_size())
background.fill((250, 250, 250))

sprites = pg.sprite.Group()
player = game_objects.Player(screen)
sprites.add(player)

tmxmap = load_pygame("tiled_map.tmx")
a = 0
g = 0
h = 0


def main():
    global a, g, h
    print(a)
    while True:

        # Exit Window if Closed of ESC is pressed
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    sys.exit()

        # screen loading
        g, h = player.rect.x, player.rect.y
        print(g, h, player.rect.x, player.rect.y, "here0")

        sprites.update()
        screen.blit(background, (0, 0))

        # loading the .tmx file stored in tmxmap to the screen Surface
        for layer in tmxmap.visible_layers:
            a+=1
            for x, y, gid in layer:
                tile_bitmap = tmxmap.get_tile_image_by_gid(gid)
                if (tile_bitmap):
                    screen.blit(tile_bitmap, (x * tmxmap.tilewidth,
                                              y * tmxmap.tileheight))

        sprites.draw(screen)
        pg.display.update()

        print(g, h, player.rect.x, player.rect.y, "here")
        clock.tick(1)
        if g != player.rect.x or h != player.rect.y:
            print("quit")
            quit()

        a += 1

main()
