from setting import *
import math
from tetramino import Tetromino


class Tetris:
    def __init__(self, app):
        self.app = app
        self.sprite_group = pg.sprite.Group()
        self.field_array = self.get_field_array()
        self.tetramino = Tetromino(self)

    def put_tetramino_blocks_in_array(self):
        for block in self.tetramino.blocks:
            x, y = int(block.pos.x), int(block.pos.y)
            self.field_array[y][x] = block

    def get_field_array(self):
        return [[0 for x in range(FIELD_W)] for y in range(FIELD_H)]

    def check_tetromino_landing(self):
        if self.tetramino.landing:
            self.put_tetramino_blocks_in_array()
            self.tetramino = Tetromino(self)

    def control(self, pressed_key):
        if pressed_key == pg.K_LEFT:
            self.tetramino.move(direction='left')
        elif pressed_key == pg.K_RIGHT:
            self.tetramino.move(direction='right')
        elif pressed_key == pg.K_UP:
            self.tetramino.rotate()

    def draw_grid(self):
        for x in range(FIELD_W):
            for y in range(FIELD_H):
                pg.draw.rect(self.app.screen, 'black',
                             (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE), 1)

    def update(self):
        if self.app.anim_trigger:
            self.tetramino.update()
            self.check_tetromino_landing()
        self.sprite_group.update()

    def draw(self):
        self.draw_grid()
        self.sprite_group.draw(self.app.screen)
