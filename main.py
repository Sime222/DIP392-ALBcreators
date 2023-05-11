from button import  Button
import pygame
import os
import sys
from play import play
from play_AI import play_ai

WIDTH = 800
HIGHT = 700
BLACK = (0, 0, 0)
BUTTON_C=(215, 252, 212)
TITLE_C=(182, 143, 64)
pygame.init()  # initialize Pygame modules, including the font module

WIN = pygame.display.set_mode((WIDTH, HIGHT))
pygame.display.set_caption("Connect-4")
print("window created")
background = pygame.transform.scale(pygame.image.load(os.path.join('ASSET', 'download.jpg')), (WIDTH, HIGHT))
menu_font = pygame.font.SysFont('comicsans', 100)

def get_font(size):
    return pygame.font.SysFont('comicsans', size)

def main():
    while True:
        WIN.blit(background, (0, 0))

        TITLE = get_font(60).render("Welcome to Connect-4", 1, TITLE_C)
        TITLE_RECT= TITLE.get_rect(center=(400, 150))
        WIN.blit(TITLE, TITLE_RECT)
        UNA = get_font(15).render("by Simeon Flamuraj and Adela Muskollari", 1, (231, 231, 231))
        UNA_RECT = UNA.get_rect(center=(400, 200))
        WIN.blit(UNA, UNA_RECT)

        MENU_MOUSE_POS = pygame.mouse.get_pos()
        print("loop is running")

        PLAY_BUTTON = Button(image=None, pos=(400, 380),
                             text_input="PLAY", font=get_font(40), base_color=BUTTON_C, hovering_color=(200, 0, 200))
        PLAY_AI_BUTTON = Button(image=None, pos=(400, 450),
                             text_input="PLAY_AI", font=get_font(40), base_color=BUTTON_C, hovering_color=(200, 0, 200))

        for button in [PLAY_BUTTON,PLAY_AI_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(WIN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("loop finished")
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if PLAY_AI_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play_ai()



        pygame.display.update()




if __name__ == "__main__":
    main()


