import pygame as pg
from newSprite import newSprite

class Textbox(newSprite):
    def __init__(self, text = "sample", offset = 20):
        # set up background
        self.offset = offset
        pg.sprite.Sprite.__init__(self)
        self.next = True
        self.end = False
        # make background
        self.image = pg.Surface((1920, 240))
        self.image.fill((255,0,0))
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0

        # index of word blits
        self.originalX = self.rect.x + self.offset
        self.originalY = self.rect.y + self.offset
        self.textX = self.originalX
        self.textY = self.originalY
        self.font = pg.font.SysFont('Arial', 64)

        # text splitting and iters
        self.text = text
        self.words = iter([word.split(' ') for word in self.text.splitlines()])  # 2D array where each row is a list of words.
        self.space = self.font.size(' ')[0]  # The width of a space.
        self.line = iter(next(self.words)) # get first line as iter
        self.nextWord()

    def update(self):
        if self.next:
            self.blitWord()
        else:
            pass

    def nextWord(self):
        try:
            self.word = next(self.line)
            self.wordLength = len(self.word)
            self.letterIndex = 0
            self.wordSurface = self.font.render(self.word, 0, pg.Color('black'))
            self.word_width, self.word_height = self.wordSurface.get_size()
            if self.textX + self.word_width >= self.rect.width:
                self.lineBreak()

        except StopIteration:
            # if no more words then get next line
            self.nextLine()

    def nextLine(self):
        try:
            # get next line
            self.line = iter(next(self.words))
            # go to next line
            self.lineBreak()
            self.nextWord()
            if self.textY + self.word_height >= self.rect.height:
                self.next = False
        except StopIteration:
            self.end = True


    def blitWord(self):
        word_surface = self.font.render(self.word[:self.letterIndex], 0, pg.Color('black'))
        self.image.blit(word_surface, (self.textX, self.textY))
        if self.letterIndex < self.wordLength:
            self.letterIndex += 1
        else:
            self.textX += self.word_width + self.space
            self.nextWord()

    def lineBreak(self):
        self.textX = self.originalX
        self.textY += self.word_height

    def clearScreen(self):
        self.next = True
        self.textX = self.originalX
        self.textY = self.originalY
        self.image.fill((255,0,0))

    def nextScreen(self):
        if not self.next:
            self.clearScreen()
        if self.end:
            self.kill()
