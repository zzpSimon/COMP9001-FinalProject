import random
import pygame
import sys
from settings import *
from Diver import Diver
from Platform import Platform
from Splash import Splash


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("High Diving Game")
    clock = pygame.time.Clock()
    score = random.randint(90, 100)  # Keep scores high (90-100) to encourage the player to keep playing
    score_font = pygame.font.Font(None,50)
    score_surface = score_font.render(f'Awesome! You earned {score} points!', False, (255, 255, 255))

    # load and transform the image to the display size
    bg1_img = pygame.image.load(BG_IMAGE1_PATH).convert()
    bg1_img = pygame.transform.scale(bg1_img, (WIDTH, HEIGHT))
    bg2_img = pygame.image.load(BG_IMAGE2_PATH).convert()
    bg2_img = pygame.transform.scale(bg2_img, (WIDTH, HEIGHT))
    bg3_img = pygame.image.load(BG_IMAGE3_PATH).convert()
    bg3_img = pygame.transform.scale(bg3_img, (WIDTH, HEIGHT))

    bg_images = [bg1_img, bg2_img, bg3_img]

    bg_index = 0
    bg_timer = 0
    bg_ticks_per_frame = 15

    # Hardcoded coordinates that perfectly align the diver onto the platform surface
    platform = Platform(200, 550)
    diver = Diver(380, 180)

    # Put platform and diver into sprite group to process more efficiently
    all_sprites = pygame.sprite.Group(platform, diver)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if diver.status == "standing":
                        diver.prepare()  # First Press for ready to jump
                    elif diver.status == "ready":
                        diver.jump()  # Second Press for formal jump
                        platform.trigger_bend()  # trigger the platform to bend
                elif event.key == pygame.K_r:
                    main()
                    return

        # Check if the player is holding SPACE to perform rotation
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            diver.rotate()

        all_sprites.update()

        if diver.spawn_splash:
            # get the splash coordinate by diver and display the splash
            new_splash = Splash(diver.rect.centerx, WATER_LINE)
            all_sprites.add(new_splash)
            diver.spawn_splash = False

        # display the background first
        # constant live background
        bg_timer += 1
        if bg_timer >= bg_ticks_per_frame:
            bg_timer = 0
            bg_index = (bg_index + 1) % len(bg_images)

        screen.blit(bg_images[bg_index], (0, 0))

        # Render all sprite elements onto the screen
        all_sprites.draw(screen)

        # Check diver status and update the window caption with instructions
        if diver.status == "standing":
            pygame.display.set_caption("Press SPACE to be ready")
        elif diver.status == "ready":
            pygame.display.set_caption("Press SPACE again to Jump!")
        elif diver.in_water:
            pygame.display.set_caption("Press [R] to restart")
            screen.blit(score_surface, (120, 40))
        else:
            pygame.display.set_caption("Keep pressing SPACE to rotate in the air!")

        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
