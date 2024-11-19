import pygame
import math
import random

def main():
    try:

        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        #print(random.randrange(0, 16))
        #print(random.randrange(0, 20))
        x2 = 1
        y2 = 1
        running = True
        r = 0
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x = event.pos[0]
                    y = event.pos[1]

                    x1 = math.ceil(x / 32)
                    y1 = math.ceil(y / 32)

                    if x1 == 1 and y1 == 1:
                        x2 = random.randrange(1, 21)
                        y2 = random.randrange(1, 17)
                        while True:
                            if x1 == x2 or y1 == y2:
                                x2 = random.randrange(1, 21)
                                y2 = random.randrange(1, 17)
                            else:
                                break

                    elif x1 == x2 and y1 == y2:
                        x2 = random.randrange(1, 21)
                        y2 = random.randrange(1, 17)
                    else:
                        break

            screen.fill((84, 67, 29))
            for row in range(1, 17, 1):
                pygame.draw.line(screen, (0, 0, 0), (0, row * 32), (640, row * 32))
            for col in range(1, 21, 1):
                pygame.draw.line(screen, (0, 0, 0), (col * 32, 0), (col * 32, 512))
            screen.blit(mole_image, mole_image.get_rect(topleft=((x2-1)*32, (y2-1)*32)))
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
