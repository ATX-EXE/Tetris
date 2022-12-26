from setting import *
import math
from tetramino import Tetromino


class Tetris:
    def __init__(self, app):
        self.app = app
        self.sprite_group = pg.sprite.Group()
        self.field_array = self.get_field_array()
        self.tetramino = Tetromino(self)

    def check_full_lines(self):
        row = FIELD_H - 1
        for y in range(FIELD_H -1, -1, -1):
            for x in range(FIELD_W):
                self.field_array[row][x] = self.field_array[y][x]

                if self.field_array[y][x]:
                    self.field_array[row][x].pos = vec(x, y)

            if sum(map(bool, self.field_array[y])) < FIELD_W:
                row -= 1
            else:
                for x in range(FIELD_W):
                    self.field_array[row][x].alive = False
                    self.field_array[row][x] = 0

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
            self.check_full_lines()
            self.tetramino.update()
            self.check_tetromino_landing()
        self.sprite_group.update()

    def draw(self):
        self.draw_grid()
        self.sprite_group.draw(self.app.screen)
