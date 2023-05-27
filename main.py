from traceback import format_tb
import pygame, sys
from button import Button
from globals import *
from pygame.locals import *
from pygame import mixer


# MENU MUSIC

pygame.init()
mixer.init()
mixer.music.load('MenuMusic.mp3')
mixer.music.play(-1)
mixer.music.set_volume(0.50)

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")
TITLE = pygame.image.load("title.png")
BG = pygame.image.load("assets/Menu.png")
CR=pygame.image.load("assets/Credits.jpeg")
LOGO=pygame.image.load("assets/dbit_logo.jpg")
MIT=pygame.image.load("assets/MIT License.jpeg")
MainTitle=pygame.image.load("assets/MainTitle.png")




def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("font.ttf", size)


# TO BE USED - CREDITS FONT
def credit_font(size):
    return pygame.font.Font("times new roman bold.ttf",size)


def play():
    while True:
        import game
        
    
def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("whitesmoke")
        HELP_TEXT = get_font(100).render("HOW TO PLAY", True, "Black")
        HELP_RECT = HELP_TEXT.get_rect(center=(640, 50))

        HELP_TEXT1 = get_font(60).render("To Move the Warrior Character Forward and Backward Use W-A-S-D keys ", True, "Black")
        HELP_RECT1 = HELP_TEXT1.get_rect(center=(640, 150))
        HELP_TEXT2 = get_font(60).render("To move the Wizard Character Forward and Backward Use the Arrow Keys", True, "Black")
        HELP_RECT2 = HELP_TEXT2.get_rect(center=(640, 250))
        HELP_TEXT3 = get_font(60).render("To Jump ,use either SPACEBAR for Warrior and UP-Arrow for Wizard", True, "Black")
        HELP_RECT3 = HELP_TEXT3.get_rect(center=(640, 350))
        HELP_TEXT4 = get_font(60).render("To fight Use the E key for Warrior and NUM1 for Wizard", True, "Black")
        HELP_RECT4 = HELP_TEXT4.get_rect(center=(640, 450))
        HELP_TEXT5 = get_font(60).render("You Will have three lives.Be Cautious about the health", True, "Black")
        HELP_RECT5 = HELP_TEXT5.get_rect(center=(640, 550))
        SCREEN.blit(HELP_TEXT, HELP_RECT)
        SCREEN.blit(HELP_TEXT1, HELP_RECT1)
        SCREEN.blit(HELP_TEXT2, HELP_RECT2)
        SCREEN.blit(HELP_TEXT3, HELP_RECT3)
        SCREEN.blit(HELP_TEXT4, HELP_RECT4)
        SCREEN.blit(HELP_TEXT5, HELP_RECT5)

        OPTIONS_BACK = Button(image=None, pos=(640, 650), text_input="BACK", font=get_font(75), base_color="Black",
                              hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()


def credits():
    while True:
        
        SCREEN.blit(CR, (0, 0))
        
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
        OPTIONS_BACK = Button(image=None, pos=(1100, 650), text_input="BACK", font=get_font(60), base_color="Black",
                              hovering_color="Green")
        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()
       
        pygame.display.update()



SCREEN.blit(MainTitle,(0,0)) # render MIT license to screen 
pygame.display.flip()
pygame.event.pump()
pygame.time.delay(3000) # continue to show screen for 3 seconds 



SCREEN.blit(MIT,(0,0)) # render MIT license to screen 
pygame.display.flip()
pygame.event.pump()
pygame.time.delay(3000) # continue to show screen for 3 seconds 


def main_menu():
    while True:
        
        SCREEN.blit(BG, (0, 0))
        SCREEN.blit(TITLE, (0, 0))


        MENU_MOUSE_POS = pygame.mouse.get_pos()

        # MENU_TEXT = get_font(100).render("MAIN MENU", True, "#b68f40")
        # MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 350), 
                            text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 500), 
                            text_input="OPTIONS", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(640, 650), 
                            text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        CREDITS_BUTTON= Button(image=pygame.image.load("assets/Credits Rect.png"),pos=(1100,650),text_input="CREDITS",font=get_font(50),base_color="#d7fcd4",hovering_color="White")

        # SCREEN.blit(MENU_TEXT, MENU_RECT)
        # SCREEN.blit(MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON,CREDITS_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if CREDITS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    credits()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()