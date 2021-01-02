import pygame, random, math
from pygame import mixer

# Initialize pygame
pygame.init()

# Define Constants
SCREEN_WIDTH = int(800)
SCREEN_HEIGHT = int(600)
PLAY_DURATION = 30000

# Load graphics
socc_closed_L = pygame.image.load('graphics/socky_closed.png')
socc_closed_R = pygame.transform.flip(socc_closed_L, True, False)
socc_open_L = pygame.image.load('graphics/socky_open.png')
socc_open_R = pygame.transform.flip(socc_open_L, True, False)
background = pygame.image.load('graphics/dirty_bedroom.png')
start_screen = pygame.image.load('graphics/socky_start.png')
instructions = pygame.image.load('graphics/socky_instructions.png')
game_over_screen = pygame.image.load('graphics/socky_game_over.png')

# Load item graphics
apple = pygame.image.load('graphics/apple.png')
can = pygame.image.load('graphics/can.png')
chips = pygame.image.load('graphics/chips.png')
undies = pygame.image.load('graphics/undies.png')
dollar = pygame.image.load('graphics/dollar.png')
pill = pygame.image.load('graphics/pill.png')
pill_bottle = pygame.image.load('graphics/pill_bottle.png')

# Load sounds
eat_sounds = [
    mixer.Sound('sounds/apple_1.wav'),
    mixer.Sound('sounds/apple_2.wav'),
    mixer.Sound('sounds/apple_3.wav'),
    mixer.Sound('sounds/apple_4.wav')
]

# Load music
pygame.mixer.music.load('sounds/bensound-jazzyfrenchy.mp3')
pygame.mixer.music.set_volume(0.4)
music = 'ready'

# create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Set title and icon
pygame.display.set_caption("Socky")
icon = pygame.image.load('graphics/sock_icon.png')
pygame.display.set_icon(icon)

# TODO implement more items
# items
items = {
    "apple": 1,
    "dollar": 1,
    "can": 1,
    "chips": 2,
    "undies": 3,
    "pill": 3,
    "pill_bottle": 5,
}
item_id = []
item_img = []
item_x = []
item_y = []
item_dx = []
item_dy = []
item_count = 10

ITEM_PADDING = 75

for i in range(item_count):
    tmp = random.randint(0, 100)
    if 0 <= tmp < 25:
        item_img.append(apple)
        item_id.append('apple')
    elif 25 <= tmp < 50:
        item_img.append(dollar)
        item_id.append('dollar')
    elif 50 <= tmp < 75:
        item_img.append(can)
        item_id.append('can')
    elif 75 <= tmp < 85:
        item_img.append(chips)
        item_id.append('chips')
    elif 85 <= tmp < 92:
        item_img.append(undies)
        item_id.append('undies')
    elif 92 <= tmp < 98:
        item_img.append(pill)
        item_id.append('pill')
    else:
        item_img.append(pill_bottle)
        item_id.append('pill_bottle')

    item_x.append(random.randint(ITEM_PADDING, SCREEN_WIDTH - ITEM_PADDING))
    item_y.append(random.randint(ITEM_PADDING, SCREEN_HEIGHT - ITEM_PADDING))
    item_dx.append(0)
    item_dy.append(0)


def draw_item(x, y, i):
    screen.blit(item_img[i], (int(x), int(y)))


# Player
player_img = socc_closed_L
player_img_width = player_img.get_rect().size[0]
player_img_height = player_img.get_rect().size[1]
player_x = int(SCREEN_WIDTH / 2) - (player_img_width / 2)
player_y = int(SCREEN_HEIGHT / 3)
player_dx = 0
player_dy = 0
move_speed = 15
direction = 'left'
mouth_open = False


def player(x, y, direction, mouth_open):
    # screen.blit(player_img, (int(x), int(y)))
    if direction == 'left':
        if mouth_open:
            screen.blit(socc_open_L, (int(x), int(y)))
        else:
            screen.blit(socc_closed_L, (int(x), int(y)))
    else:
        if mouth_open:
            screen.blit(socc_open_R, (int(x), int(y)))
        else:
            screen.blit(socc_closed_R, (int(x), int(y)))


# function for detecting mouth collision
def mouth_collision(mouth_x, mouth_y, item_x, item_y):
    dist = math.hypot(mouth_x - item_x, mouth_y - item_y)
    if dist <= 100:
        return True
    return False
    # middle of mouth = (195, 80)


# Score
score_value = 0
score_x = 30
score_y = 10
score_font = pygame.font.Font('graphics/Rockies.otf', 32)


def show_score(x, y):
    score = score_font.render("Score: " + str(score_value), True, (0, 0, 0,))
    screen.blit(score, (x, y))




# Game Over
game_over_font = pygame.font.Font('graphics/Rockies.otf', 64)
def game_over():
    game_over_text = game_over_font.render("Final Score: " + str(score_value), True, (0, 0, 0,))
    screen.blit(game_over_screen, (0, 0))
    screen.blit(game_over_text, (60, 215))
    pygame.mixer.music.fadeout(1500)

# Set timer
timer_x = SCREEN_WIDTH - 200
timer_y = 10


class Timer:
    """ Timer initialized with a duration in milliseconds to be called"""

    def __init__(self, start, duration):  # start timer
        self.now = pygame.time.get_ticks()
        self.start = start
        self.duration = duration
        self.seconds = round((duration - (self.now - self.start)) / 1000)
        self.time_left = score_font.render("Time left: " + str(self.seconds), True, (0, 0, 0,))

    def running(self):  # check if timer has reached duration
        if self.duration <= (self.now - self.start):
            return False
        return True

    def display(self, x, y):
        screen.blit(self.time_left, (int(x), int(y)))


# Game Loop
game_state = 'start'
running = True
while running:

    # Set background
    screen.fill((255, 255, 255))
    # Background image
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        # Click X to close window
        if event.type == pygame.QUIT:
            running = False

        # KEY PRESSES
        if event.type == pygame.KEYDOWN:
            # Press escape to close window
            if event.key == pygame.K_ESCAPE:
                running = False
            # Left to move left
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:  # and event.key != pygame.K_d and event.key == pygame.K_RIGHT:
                player_dx += -move_speed
                direction = 'left'
            # Right to move right
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:  # and event.key != pygame.K_a and event.key == pygame.K_LEFT:
                player_dx += move_speed
                direction = 'right'
            # Up movement
            if event.key == pygame.K_w or event.key == pygame.K_UP:
                player_dy += -move_speed
            # Down movement
            if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                player_dy += move_speed
            # Space to open mouth
            if event.key == pygame.K_SPACE:
                mouth_open = True
            if event.key == pygame.K_RETURN:
                game_state = 'play'
                pygame.mixer.music.play(-1)
                game_start_time = pygame.time.get_ticks()
                score_value = 0
            if event.key == pygame.K_TAB:
                game_state = 'instructions'
                pygame.mixer.music.fadeout(1500)
            if event.key == pygame.K_m:
                if music == 'ready':
                    pygame.mixer.music.stop()
                    music = 'muted'
                elif music == 'muted':
                    pygame.mixer.music.play(-1)
                    music = 'ready'
        # KEY RELEASES
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                player_dx += move_speed
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                player_dx += -move_speed
            if event.key == pygame.K_w or event.key == pygame.K_UP:
                player_dy += move_speed
            if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                player_dy += -move_speed
            if event.key == pygame.K_SPACE and game_state == 'play':
                mouth_open = False
                for i in range(item_count):
                    if mouth_collision(player_x + 195, player_y + 80, item_x[i], item_y[i]):
                        score_value += items[item_id[i]]
                        tmp = random.randint(0, 3)
                        eat_sounds[tmp].play()
                        item_x[i] = random.randint(ITEM_PADDING, SCREEN_WIDTH - ITEM_PADDING)
                        item_y[i] = random.randint(ITEM_PADDING, SCREEN_HEIGHT - ITEM_PADDING)
                        tmp = random.randint(0, 100)
                        # set new random item to replace eaten item
                        if 0 <= tmp < 25:
                            item_img[i] = apple
                            item_id[i] = 'apple'
                        elif 25 <= tmp < 50:
                            item_img[i] = dollar
                            item_id[i] = 'dollar'
                        elif 50 <= tmp < 75:
                            item_img[i] = can
                            item_id[i] = 'can'
                        elif 75 <= tmp < 85:
                            item_img[i] = chips
                            item_id[i] = 'chips'
                        elif 85 <= tmp < 92:
                            item_img[i] = undies
                            item_id[i] = 'undies'
                        elif 92 <= tmp < 98:
                            item_img[i] = pill
                            item_id[i] = 'pill'
                        else:
                            item_img[i] = pill_bottle
                            item_id[i] = 'pill_bottle'

    if game_state == 'start':
        screen.blit(start_screen, (0, 0))
    elif game_state == 'instructions':
        screen.blit(instructions, (0, 0))
    elif game_state == 'play':

        # Set player direction
        if player_dx > 0:
            direction = 'right'
        elif player_dx <= 0:
            direction = 'left'

        # Add player velocity
        player_x += player_dx
        player_y += player_dy

        # Add player boundaries
        if player_x < -(player_img_width / 2):
            player_x = -(player_img_width / 2)
        elif player_x >= SCREEN_WIDTH - player_img_width / 2:
            player_x = SCREEN_WIDTH - player_img_width / 2
        if player_y < (player_img_height / 8):
            player_y = (player_img_height / 8)
        elif player_y >= SCREEN_HEIGHT - player_img_height / 3:
            player_y = SCREEN_HEIGHT - player_img_height / 3

        player(player_x, player_y, direction, mouth_open)

        # Add items
        for i in range(item_count):

            # change movement if socc is open
            if player_img == socc_open_L:
                item_dx[i] = 0.2 * player_dx + random.randint(-30, 30)
                item_dy[i] = 0.2 * player_dy + random.randint(-30, 30)
            else:
                item_dx[i] = 0
                item_dy[i] = 0

            item_x[i] += item_dx[i]
            item_y[i] += item_dy[i]

            # Add item boundaries
            if item_x[i] < 0:
                item_x[i] = 0
            elif item_x[i] > SCREEN_WIDTH - ITEM_PADDING:
                item_x[i] = SCREEN_WIDTH - ITEM_PADDING
            if item_y[i] < ITEM_PADDING:
                item_y[i] = ITEM_PADDING
            elif item_y[i] > SCREEN_HEIGHT - ITEM_PADDING:
                item_y[i] = SCREEN_HEIGHT - ITEM_PADDING

            # Draw items
            draw_item(item_x[i], item_y[i], i)

        # Draw score
        show_score(score_x, score_y)

        # Draw timer
        Game_Timer = Timer(game_start_time, PLAY_DURATION)
        if Game_Timer.running():
            Game_Timer.display(timer_x, timer_y)
        else:
            game_state = 'game_over'
    else:  # game_state == 'game_over'
        game_over()
        pass

    # Update
    pygame.display.update()

# Credits:
# https://www.youtube.com/watch?v=FfWpgLFMI7w
# Music:
# Royalty Free Music from Bensound.com
