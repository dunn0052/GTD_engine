from newSprite import newSprite

class Wall(newSprite):

    def __init__(self, x, y, image, level = None):
        self.image = image
        super().__init__(self.image, 1)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y
        if level:
            level.WALL_LAYER.add(self)
            level.all_sprites.add(self)
