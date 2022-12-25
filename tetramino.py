from setting import *


class Block(pg.sprite.Sprite):
    def __init__(self, tetramino, pos):
        self.tetramino = tetramino
        self.pos = vec(pos) + INIT_POS_OFFSET

        super().__init__(tetramino.tetris.sprite_group)
        self.image = pg.Surface([TILE_SIZE, TILE_SIZE])
        self.image.fill('orange')

        self.rect = self.image.get_rect()
        self.rect.topleft = self.pos * TILE_SIZE

class Tetromino:
    def __init__(self, tetris):
        self.tetris = tetris
        self.shape = 'T'
        self.blocks = [Block(self, pos) for pos in TETROMINOES[self.shape]]

    def update(self):
        pass