import pygame
from Colours import *
import os
from Menu import *
from Objects import *

path = os.path.dirname(os.path.abspath(__file__))
os.chdir(path)

pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((1200, 700))
pygame.display.set_caption("Pong Online")
size = screen.get_size()

clock = pygame.time.Clock()

font = "./Fonts/atlantis-international-font/AtlantisInternational-jen0.ttf"
regularfont = pygame.font.Font("./Fonts/atlantis-international-font/AtlantisInternational-jen0.ttf", 30)
titlefont = pygame.font.Font("./Fonts/atlantis-international-font/AtlantisInternational-jen0.ttf", 50)

def test(a="", b=""):
    print("a: " + a)
    print("b: " + b)

key1 = "a"
value1 = "a"

key2 = "b"
value2 = "b"

test(**{key1:value1, key2:value2})

if "t" in "test":
    print("t is in test")

text = "test"

print(text[:len(text) - 1])

#Local Host Game
class Local:
    def __init__(self, screen):
        self.screen = screen

#Online Game
class Online:
    def __init__(self, screen):
        self.screen = screen

page = "Title"

title = Title(font, screen)
hostmenu = HostMenu(font, screen)
joinmenu = JoinMenu(font, screen)

while page != "Quit":
    if page == "Title":
        
        eventList = pygame.event.get()
        page = title.event(eventList, page)
        title.draw()
    
    elif page == "Start Local":

        eventList = pygame.event.get()
        page = hostmenu.event(eventList, page)
        hostmenu.draw()

    elif page == "Host LAN":

        eventList = pygame.event.get()
        page = hostmenu.event(eventList, page)
        hostmenu.draw()

    elif page == "Join LAN":

        eventList = pygame.event.get()
        page = joinmenu.event(eventList, page)
        joinmenu.draw()

        
