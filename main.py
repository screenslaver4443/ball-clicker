import pygame
pygame.init()

##### Colours #####
BLACK = (0,   0,   0)
WHITE = (255, 255, 255)
RED = (255,   0,   0)
BLUE = (0,   0, 255)

##### Screen Initialisation #####
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Title")

#### Font #####
pygame.font.init()
font = pygame.font.Font(pygame.font.get_default_font(), 20)

done = False
clock = pygame.time.Clock()

##### Classes #####
class ball:
    def __init__(self):  # Initialisation
        self.colour = WHITE  # Color of ball
        self.x = SCREEN_WIDTH/2  # spawn position of 1st ball
        self.y = SCREEN_HEIGHT/2
        self.radius = 100  # radius of ball
        self.speedx = 0  # speed of ball
        self.speedy = 0

    def movement(self):  # Movement of ball
        self.x += self.speedx  # movement
        self.y += self.speedy
        # if ball is going to leave screen: reverse direction.
        if self.x > SCREEN_WIDTH or self.x < 0:
            self.speedx *= -1
        if self.y > SCREEN_WIDTH or self.y < 0:
            self.speedy *= -1

### Class Table ###
balls = [ball() for _ in range(1)] #Creates initial ball

##### Main Program Loop #####
while not done:
    ##### Events Loop #####
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    ##### Game logic #####

    ##### Drawing code #####
    screen.fill(BLACK)
    for ball in balls:
        pygame.draw.circle(screen, ball.colour, (ball.x, ball.y), ball.radius)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
