import pygame
from settings import *


class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        # displaying in order to create a smooth bending animation
        self.images = [
            pygame.image.load(PLATFORM_Stage1_PATH).convert_alpha(),
            pygame.image.load(PLATFORM_Stage2_PATH).convert_alpha(),
            pygame.image.load(PLATFORM_Stage3_PATH).convert_alpha()
        ]

        # default to display the first image of the platform(not bending status)
        self.current_image_index = 0
        self.image = self.images[self.current_image_index]

        self.rect = self.image.get_rect()
        self.rect.midbottom = (x, y)

        # set a timer to display the frame not too fast
        self.is_animating = False
        self.frame_timer = 0
        self.ticks_per_frame = 8

    def trigger_bend(self):
        if not self.is_animating:
            self.is_animating = True
            self.current_image_index = 1  # go to other stages(bending)
            self.image = self.images[self.current_image_index]
            self.frame_timer = 0

    def update(self):
        if self.is_animating:
            self.frame_timer += 1

            if self.frame_timer >= self.ticks_per_frame:
                self.frame_timer = 0
                self.current_image_index += 1

                if self.current_image_index >= len(self.images):
                    self.current_image_index = 0
                    self.is_animating = False

                self.image = self.images[self.current_image_index]