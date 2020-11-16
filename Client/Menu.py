import pygame
from Objects import *
from Colours import *

class Title:
    def __init__(self, font, screen):
        self.selected = -1

        self.screen = screen
        self.font = font
        size = self.screen.get_size()
        self.clock = pygame.time.Clock()

        self.titleSurface = pygame.font.Font(self.font, 200).render("Pong", True, white)
        self.titleRect = self.titleSurface.get_rect(centerx=size[0] * 0.5, centery=size[1] * 0.2)

        self.startButtonSurface = pygame.Surface((size[0] * 0.5, size[1] * 0.1))
        self.startButtonSurface.fill(red)
        self.startButtonRect = self.startButtonSurface.get_rect(centerx=size[0] * 0.5, centery=size[1] * 0.44)

        self.startTextSurface = pygame.font.Font(self.font, 50).render("Start Local", True, black)
        self.startTextRect = self.startTextSurface.get_rect(centerx=size[0] * 0.5, centery=size[1] * 0.44)

        self.hostButtonSurface = pygame.Surface((size[0] * 0.5, size[1] * 0.1))
        self.hostButtonSurface.fill(green)
        self.hostButtonRect = self.hostButtonSurface.get_rect(centerx=size[0] * 0.5, centery=size[1] * 0.56)

        self.hostTextSurface = pygame.font.Font(self.font, 50).render("Host LAN", True, black)
        self.hostTextRect = self.hostTextSurface.get_rect(centerx=size[0] * 0.5, centery=size[1] * 0.56)

        self.joinButtonSurface = pygame.Surface((size[0] * 0.5, size[1] * 0.1))
        self.joinButtonSurface.fill(blue)
        self.joinButtonRect = self.joinButtonSurface.get_rect(centerx=size[0] * 0.5, centery=size[1] * 0.68)

        self.joinTextSurface = pygame.font.Font(self.font, 50).render("Join LAN", True, black)
        self.joinTextRect = self.joinTextSurface.get_rect(centerx=size[0] * 0.5, centery=size[1] * 0.68)

        self.onlineButtonSurface = pygame.Surface((size[0] * 0.5, size[1] * 0.1))
        self.onlineButtonSurface.fill(yellow)
        self.onlineButtonRect = self.onlineButtonSurface.get_rect(centerx=size[0] * 0.5, centery=size[1] * 0.80)

        self.onlineTextSurface = pygame.font.Font(self.font, 50).render("Join Online", True, black)
        self.onlineTextRect = self.onlineTextSurface.get_rect(centerx=size[0] * 0.5, centery=size[1] * 0.80)

        self.optionsButtonSurface = pygame.Surface((size[0] * 0.5, size[1] * 0.10))
        self.optionsButtonSurface.fill(white)
        self.optionsButtonRect = self.optionsButtonSurface.get_rect(centerx=size[0] * 0.5, centery=size[1] * 0.92)

        self.optionsTextSurface = pygame.font.Font(self.font, 50).render("Options", True, black)
        self.optionsTextRect = self.optionsTextSurface.get_rect(centerx=size[0] * 0.5, centery=size[1] * 0.92)

    def update(self):
        size = self.screen.get_size()
        if self.selected == 0:
            self.startButtonSurface = pygame.Surface((size[0] * 0.52, size[1] * 0.12))
            self.startButtonSurface.fill(red)
            self.startButtonRect = self.startButtonSurface.get_rect(centerx=size[0] * 0.5, centery=size[1] * 0.44)

            self.startTextSurface = pygame.font.Font(self.font, 60).render("Start Local", True, black)
            self.startTextRect = self.startTextSurface.get_rect(centerx=size[0] * 0.5, centery=size[1] * 0.44)
        else:
            self.startButtonSurface = pygame.Surface((size[0] * 0.5, size[1] * 0.1))
            self.startButtonSurface.fill(red)
            self.startButtonRect = self.startButtonSurface.get_rect(centerx=size[0] * 0.5, centery=size[1] * 0.44)

            self.startTextSurface = pygame.font.Font(self.font, 50).render("Start Local", True, black)
            self.startTextRect = self.startTextSurface.get_rect(centerx=size[0] * 0.5, centery=size[1] * 0.44)

        if self.selected == 1:
            self.hostButtonSurface = pygame.Surface((size[0] * 0.52, size[1] * 0.12))
            self.hostButtonSurface.fill(green)
            self.hostButtonRect = self.hostButtonSurface.get_rect(centerx=size[0] * 0.5, centery=size[1] * 0.56)

            self.hostTextSurface = pygame.font.Font(self.font, 60).render("Host LAN", True, black)
            self.hostTextRect = self.hostTextSurface.get_rect(centerx=size[0] * 0.5, centery=size[1] * 0.56)
        else:
            self.hostButtonSurface = pygame.Surface((size[0] * 0.5, size[1] * 0.1))
            self.hostButtonSurface.fill(green)
            self.hostButtonRect = self.hostButtonSurface.get_rect(centerx=size[0] * 0.5, centery=size[1] * 0.56)

            self.hostTextSurface = pygame.font.Font(self.font, 50).render("Host LAN", True, black)
            self.hostTextRect = self.hostTextSurface.get_rect(centerx=size[0] * 0.5, centery=size[1] * 0.56)

        if self.selected == 2:
            self.joinButtonSurface = pygame.Surface((size[0] * 0.52, size[1] * 0.12))
            self.joinButtonSurface.fill(blue)
            self.joinButtonRect = self.joinButtonSurface.get_rect(centerx=size[0] * 0.5, centery=size[1] * 0.68)

            self.joinTextSurface = pygame.font.Font(self.font, 60).render("Join LAN", True, black)
            self.joinTextRect = self.joinTextSurface.get_rect(centerx=size[0] * 0.5, centery=size[1] * 0.68)
        else:
            self.joinButtonSurface = pygame.Surface((size[0] * 0.5, size[1] * 0.1))
            self.joinButtonSurface.fill(blue)
            self.joinButtonRect = self.joinButtonSurface.get_rect(centerx=size[0] * 0.5, centery=size[1] * 0.68)

            self.joinTextSurface = pygame.font.Font(self.font, 50).render("Join LAN", True, black)
            self.joinTextRect = self.joinTextSurface.get_rect(centerx=size[0] * 0.5, centery=size[1] * 0.68)

        if self.selected == 3:
            self.onlineButtonSurface = pygame.Surface((size[0] * 0.52, size[1] * 0.12))
            self.onlineButtonSurface.fill(yellow)
            self.onlineButtonRect = self.onlineButtonSurface.get_rect(centerx=size[0] * 0.5, centery=size[1] * 0.80)

            self.onlineTextSurface = pygame.font.Font(self.font, 60).render("Join Online", True, black)
            self.onlineTextRect = self.onlineTextSurface.get_rect(centerx=size[0] * 0.5, centery=size[1] * 0.80)
        else:
            self.onlineButtonSurface = pygame.Surface((size[0] * 0.5, size[1] * 0.1))
            self.onlineButtonSurface.fill(yellow)
            self.onlineButtonRect = self.onlineButtonSurface.get_rect(centerx=size[0] * 0.5, centery=size[1] * 0.80)

            self.onlineTextSurface = pygame.font.Font(self.font, 50).render("Join Online", True, black)
            self.onlineTextRect = self.onlineTextSurface.get_rect(centerx=size[0] * 0.5, centery=size[1] * 0.80)

        if self.selected == 4:
            self.optionsButtonSurface = pygame.Surface((size[0] * 0.52, size[1] * 0.12))
            self.optionsButtonSurface.fill(white)
            self.optionsButtonRect = self.optionsButtonSurface.get_rect(centerx=size[0] * 0.5, centery=size[1] * 0.92)

            self.optionsTextSurface = pygame.font.Font(self.font, 60).render("Options", True, black)
            self.optionsTextRect = self.optionsTextSurface.get_rect(centerx=size[0] * 0.5, centery=size[1] * 0.92)
        else:
            self.optionsButtonSurface = pygame.Surface((size[0] * 0.5, size[1] * 0.1))
            self.optionsButtonSurface.fill(white)
            self.optionsButtonRect = self.optionsButtonSurface.get_rect(centerx=size[0] * 0.5, centery=size[1] * 0.92)

            self.optionsTextSurface = pygame.font.Font(self.font, 50).render("Options", True, black)
            self.optionsTextRect = self.optionsTextSurface.get_rect(centerx=size[0] * 0.5, centery=size[1] * 0.92)

    def draw(self):
        self.screen.fill(black)

        self.screen.blit(self.titleSurface, self.titleRect)

        self.screen.blit(self.startButtonSurface, self.startButtonRect)
        self.screen.blit(self.startTextSurface, self.startTextRect)

        self.screen.blit(self.hostButtonSurface, self.hostButtonRect)
        self.screen.blit(self.hostTextSurface, self.hostTextRect)

        self.screen.blit(self.joinButtonSurface, self.joinButtonRect)
        self.screen.blit(self.joinTextSurface, self.joinTextRect)

        self.screen.blit(self.onlineButtonSurface, self.onlineButtonRect)
        self.screen.blit(self.onlineTextSurface, self.onlineTextRect)

        self.screen.blit(self.optionsButtonSurface, self.optionsButtonRect)
        self.screen.blit(self.optionsTextSurface, self.optionsTextRect)
        
        pygame.display.update()

        self.clock.tick(60)

    def event(self, eventList, page):

        for event in eventList:
            if event.type == pygame.QUIT:
                page = "Quit"
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    page = "Quit"
                elif event.key == pygame.K_UP:
                    if self.selected == -1:
                        self.selected = 0
                    self.selected = (self.selected + 5 - 1) % 5
                    self.update()
                elif event.key == pygame.K_DOWN:
                    self.selected = (self.selected + 5 + 1) % 5
                    self.update()
                elif event.key == pygame.K_RETURN:
                    if self.selected == 0:
                        page = "Start Local"
                    elif self.selected == 1:
                        page = "Host LAN"
                    elif self.selected == 2:
                        page = "Join LAN"
                    elif self.selected == 3:
                        page = "Join Online"
                    elif self.selected == 4:
                        page = "Options"
        return page

#Join IP Address Menu
class JoinMenu:

    def __init__(self, font, screen):
        self.screen = screen
        size = self.screen.get_size()
        self.font = font
        self.clock = pygame.time.Clock()

        self.titleSurface = pygame.font.Font(self.font, 100).render("Join Game", True, white)
        self.titleRect = self.titleSurface.get_rect(centerx=size[0] * 0.5, centery=size[1] * 0.1)

        self.ipField = TextField(self.screen, "1234567890.", [size[0] * 0.5, size[1] * 0.1], [size[0] * 0.5, size[1] * 0.5], font, 50, ["centerx", "centery"], [white, black, cyan])
        self.portField = TextField(self.screen, "1234567890", [size[0] * 0.5, size[1] * 0.1], [size[0] * 0.5, size[1] * 0.6], font, 50, ["centerx", "centery"], [white, black, cyan])

    def draw(self):
        screen.fill(black)

        self.screen.blit(self.titleSurface, self.titleRect)
        self.ipField.draw()
        self.portField.draw()

        pygame.display.update()

        self.clock.tick(60)

    def event(self, eventList, page):

        self.ipField.event(eventList)
        self.portField.event(eventList)

        for event in eventList:
            if event.type == pygame.QUIT:
                page = "Quit"
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    page = "Quit"

        return page

#Game Configuration Menu
class HostMenu:
    def __init__(self, font, screen):
        self.screen = screen
        size = self.screen.get_size()
        self.clock = pygame.time.Clock()

        self.font = font

        self.titleSurface = pygame.font.Font(self.font, 100).render("Configure Game", True, white)
        self.titleRect = self.titleSurface.get_rect(centerx=size[0] * 0.5, centery=size[1] * 0.1)

        self.textField = TextField(self.screen, "1234567890", [size[0] * 0.5, size[0] * 0.1], [size[0] * 0.5, size[1] * 0.5], font, 50, ["centerx", "centery"], [white, black, cyan])

    def draw(self):
        self.screen.fill(black)

        self.screen.blit(self.titleSurface, self.titleRect)
        self.textField.draw()

        pygame.display.update()

        self.clock.tick(60)

    def event(self, eventList, page):

        for event in eventList:
            if event.type == pygame.QUIT:
                page = "Quit"
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    page = "Quit"

        self.textField.event(eventList)

        return page