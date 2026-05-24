import pygame
from settings import *


class Splash(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        # load three image into a list for displaying in order which makes looks like alive
        self.images = [
            pygame.image.load(WATER_SPLASH1_PATH).convert_alpha(),
            pygame.image.load(WATER_SPLASH2_PATH).convert_alpha(),
            pygame.image.load(WATER_SPLASH3_PATH).convert_alpha()
        ]

        # adjust the splash size to fit in the display
        splash_size = (120, 100)
        self.images = [pygame.transform.scale(img, splash_size) for img in self.images]

        self.current_frame = 0
        self.image = self.images[self.current_frame]

        self.rect = self.image.get_rect()
        self.rect.midbottom = (x, y)

        # set a timer to display the frame not too fast
        self.frame_timer = 0
        self.ticks_per_frame = 6

    def update(self):
        self.frame_timer += 1
        if self.frame_timer >= self.ticks_per_frame:
            self.frame_timer = 0
            self.current_frame += 1

            if self.current_frame >= len(self.images):
                self.kill()
            else:
                self.image = self.images[self.current_frame]