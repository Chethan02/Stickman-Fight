from globals import *
from pygame.locals import *
from pygame import mixer
import pygame as pg
from button import Button

# GAME MUSIC

pg.init()
mixer.init()
mixer.music.load('bg_music.mp3')
mixer.music.play(-1)
mixer.music.set_volume(0.15)

window = pg.display.set_mode((1280, 720))

def get_font(size):
    return pygame.font.Font("font.ttf", size)

# PyGame initialized
pygame.init()

# Refresh Rate
clock = pygame.time.Clock()

# Font and size
font = pygame.font.Font(font_path, 32)

# For performance
pygame.event.set_allowed([QUIT, KEYDOWN, KEYUP])

# Set window name
pygame.display.set_caption("Stickman Fight")

# Background image
background = pygame.image.load(background_img)
print(background.get_width(), background.get_height())

# Window Dimensions
WINDOW_DIMENSIONS = (background.get_width(), background.get_height())
WINDOW_WIDTH, WINDOW_HEIGHT = WINDOW_DIMENSIONS

# Create screen
flags = DOUBLEBUF
screen = pygame.display.set_mode(WINDOW_DIMENSIONS, flags, 16)

# Player declaration
player = Stickman_player(WINDOW_DIMENSIONS)




def background_show():
    screen.blit(background, (0, 0))

    # MENU_TEXT = get_font(100).render("MAIN MENU", True, "#b68f40")
    # MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))


def player_show(values):
    player_img = values[0]
    width, height = values[1][0], values[1][1]
    x, y = values[2][0], values[2][1]
    screen.blit(player_img, (x-width/2, y-height))


enemyCharacter = pygame.image.load("EnemyCharacter.png")
enemyX = 900
enemyY = 530

# enemy show function


def enemy_show():
    screen.blit(enemyCharacter, (enemyX, enemyY))


# Player variables
player_img = player.frame_movement()

# Enemy variables
# enemy_img = enemy.frame_movement()

# Moving keys
keys = set([pygame.K_a, pygame.K_d])
# keys = set([pygame.K_a, pygame.K_d])

# enemy Moving keys
# keys = set([pygame.K_LEFT, pygame.RIGHT])

# Jump keys
jumpKeys = set([ pygame.K_w])

# enemy jump keys
# jumpKeys = set([pygame.K_SPACE, pygame.K_w, pygame.K_UP])

#function for health bar
def draw_health_bar(health, x, y):
  ratio = health / 100
  pygame.draw.rect(screen, "WHITE", (x - 2, y - 2, 404, 34))
  pygame.draw.rect(screen, "RED", (x, y, 400, 30))
  pygame.draw.rect(screen, "YELLOW", (x, y, 400 * ratio, 30))

#function for drawing text
def draw_text(text, font, text_col, x, y):
  img = font.render(text, True, text_col)
  screen.blit(img, (x, y))

while 1:
    clock.tick(144)

    pressed = pygame.key.get_pressed()

    color = (128,255,0)
    # Drawing Rectangle
    pygame.draw.rect(window, color, pygame.Rect(50, 60, 250, 60))
    pygame.display.flip()
    HEALTH_TEXT = get_font(50).render("WARRIOR", True, "Black")
    HEALTH_RECT = HEALTH_TEXT.get_rect(center=(100, 40))

    window.blit(HEALTH_TEXT, HEALTH_RECT)
    
    color = (128,255,0)
    # Drawing Rectangle
    pygame.draw.rect(window, color, pygame.Rect(985, 60, 250, 60))
    pygame.display.flip()
    

    events = pygame.event.get()
    for event in events:

        # Click on cross button or alt+f4
        if event.type == pygame.QUIT:
            exit()

        # Key down check
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                player.move_left()

            if event.key == pygame.K_d:
                player.move_right()

            elif event.key == pygame.K_a:
                player.move_left()

            if not player.is_jumping() and event.key in jumpKeys:
                player.jump_up()

        # Key up check
        if event.type == pygame.KEYUP:
            if event.key in keys:
                player.stop_moving()
            if event.key == pygame.K_l:
                print(player.get_pos())

    # Get player image
    player_img = player.frame_movement()

    # Final display of all images
    screen.fill((0, 0, 0))
    background_show()
    enemy_show()
    player_show(player_img)

    pygame.display.update()


def get_font(size):  # Returns Press-Start-2P in the desired size
    return pygame.font.Font("font.ttf", size)


def back():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        PLAY_BACK = Button(image=None, pos=(500, 50), text_input="BACK", font=get_font(20), base_color="White",
                           hovering_color="Green")
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    mixer.music.stop()
                    import main
        pygame.display.update()


print("over")
