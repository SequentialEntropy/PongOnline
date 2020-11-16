import pygame
from Colours import *

class TextField:
    def __init__(self, screen, validChars, size, pos, font, fontsize, align, colors):
        self.screen = screen
        self.validChars = validChars
        self.size = size
        self.pos = pos
        self.fontsize = fontsize
        self.align = align
        self.colors = colors
        self.focus = False
        self.font = font

        self.fieldText = ""

        self.fieldTextSurface = pygame.font.Font(self.font, self.fontsize).render(self.fieldText, True, self.colors[1])
        self.fieldTextRect = self.fieldTextSurface.get_rect(**{self.align[0]:self.pos[0], self.align[1]:self.pos[1]})

        self.fieldBackgroundSurface = pygame.Surface((self.size[0], self.size[1]))
        self.fieldBackgroundSurface.fill(self.colors[0])
        self.fieldBackgroundRect = self.fieldBackgroundSurface.get_rect(**{self.align[0]:self.pos[0], self.align[1]:self.pos[1]})

    def draw(self):

        self.screen.blit(self.fieldBackgroundSurface, self.fieldBackgroundRect)
        self.screen.blit(self.fieldTextSurface, self.fieldTextRect)

    def event(self, EventList):

        for event in EventList:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE and self.focus:
                    self.fieldText = self.fieldText[:len(self.fieldText) - 1]
                    self.fieldTextSurface = pygame.font.Font(self.font, self.fontsize).render(self.fieldText, True, black)
                    self.fieldTextRect = self.fieldTextSurface.get_rect(**{self.align[0]:self.pos[0]}, **{self.align[1]:self.pos[1]})
                elif chr(event.key) in self.validChars and self.focus:
                    self.fieldText = self.fieldText + chr(event.key)
                    self.fieldTextSurface = pygame.font.Font(self.font, self.fontsize).render(self.fieldText, True, black)
                    self.fieldTextRect = self.fieldTextSurface.get_rect(**{self.align[0]:self.pos[0]}, **{self.align[1]:self.pos[1]})
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mousePos = pygame.mouse.get_pos()
                if self.fieldBackgroundRect.collidepoint(mousePos):
                    self.focus = True
                    self.fieldBackgroundSurface.fill(self.colors[2])
                else:
                    self.focus = False
                    self.fieldBackgroundSurface.fill(self.colors[0])

class CheckBox:
    def __init__(self, screen, size, pos, align, colors):
        self.screen = screen
        self.size = size
        self.pos = pos
        self.align = align
        self.colors = colors
        self.bool = False

        self.checkboxSurface = pygame.Surface((self.size[0], self.size[1]))
        self.checkboxSurface.fill(self.colors[0])
        self.checkboxRect = self.checkboxSurface.get_rect(**{self.align[0]:self.pos[0], self.align[1]:self.pos[1]})

    def draw(self):
        self.screen.blit(self.checkboxSurface, self.checkboxRect)

    def event(self, EventList):
        
        for event in EventList:
            if event.key == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and self.focus:
                    if self.bool:
                        self.bool = False
                    else:
                        self.bool = True