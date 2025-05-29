from settings import *


class Block(pg.sprite.Sprite):
    def init (self, tetromino, pos):
        self.tetromino = tetromino
        self.pos = vec(pos) + INIT_POS_OFF

        super().__init__(tetromino.tetris.spirte_group)
        self.image = pg.Surface([TILE_SIZE, TILE_SIZE])
        self.image.fill('orange')

        self.rect = self.image.get_rect()
        self.rect.topleft = pos [0] * TILE_SIZE, pos [1] * TILE_SIZE


class Tetromino:
    def init (self, tetris):
        self.tetris = tetris
        self.shape = random.choice(list(TETROMINOES.keys()))
        self.blocks = [Block(self, pos) for pos in TETROMINOES[self.shape]]

    def move(self,direction):
        move_direction = MOVE_DIRECTIONS[direction]
        for block in self.blocks:
            blocks.pos += move_direction


    def update(self):
        self.move(direction='down')
