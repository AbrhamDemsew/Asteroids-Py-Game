import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from player import Player

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH} \nScreen height: {SCREEN_HEIGHT}")
    pygame.init()  #initializing the pygame
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    drawable = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    Player.containers = (drawable, updatable)
    player = Player(x,y)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0.0

    while True:
        log_state()
        for event in pygame.event.get():
            pass
        screen.fill("black")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        dt = clock.tick(60) / 1000

        updatable.update(dt)
        for draw in drawable:
            draw.draw(screen)


        pygame.display.flip()

if __name__ == "__main__":
    main()
