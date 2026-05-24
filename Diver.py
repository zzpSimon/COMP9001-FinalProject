import pygame
from settings import *


class Diver(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        DIVER_SIZE = (100, 100)

        # make sure each diver status is at same size
        self.stand_image = pygame.transform.scale(pygame.image.load(DIVER_STAND_PATH).convert_alpha(), DIVER_SIZE)
        self.ready_image = pygame.transform.scale(pygame.image.load(DIVER_READY_PATH).convert_alpha(), DIVER_SIZE)
        self.jump_image = pygame.transform.scale(pygame.image.load(DIVER_JUMP_PATH).convert_alpha(), DIVER_SIZE)

        # original status set to stand
        self.orig_image = self.stand_image
        self.image = self.orig_image.copy()

        # Initialize original coordinates
        self.rect = self.image.get_rect()
        self.rect.midbottom = (x, y)

        # Convert integer coordinates to floats to prevent micro-stuttering caused by gravity accumulation
        self.x = float(self.rect.centerx)
        self.y = float(self.rect.centery)

        # core attribute of the diver
        self.vel_y = 0.0           # Y-axis speed
        self.angle = 0.0           # rotate angle
        self.status = "standing"   # diver status : "standing" -> "ready" -> "jumping"
        self.in_water = False
        self.spawn_splash = False  # splash status

    def prepare(self):
        if self.status == "standing":
            self.status = "ready"
            self.orig_image = self.ready_image
            self.image = self.orig_image.copy()

    def jump(self):
        if self.status == "ready":
            self.vel_y = JUMP_SPEED
            self.status = "jumping"
            self.orig_image = self.jump_image
            self.image = self.orig_image.copy()

    def rotate(self):
        if self.status == "jumping" and not self.in_water:
            self.angle = (self.angle + ROTATION_SPEED) % 360

            # use the center of the diver to perform rotate
            old_center = (self.x, self.y)
            self.image = pygame.transform.rotate(self.orig_image, self.angle)
            self.rect = self.image.get_rect()
            self.rect.center = old_center

    def update(self):
        if self.status == "jumping" and not self.in_water:
            # apply the gravity on y
            self.vel_y += GRAVITY
            self.y += self.vel_y
            self.x += 3

            self.rect.centerx = int(self.x) # give the diver an initial speed on x
            self.rect.centery = int(self.y)

            # check if touching the water surface
            if self.rect.centery >= WATER_LINE:
                self.in_water = True
                self.handle_water_entry()

    def handle_water_entry(self):
        self.spawn_splash = True  # when diver contact to the surface, set the status to true
        self.image = pygame.Surface((1, 1), pygame.SRCALPHA) # Make the diver disappear when reaching the surface
        final_angle = int(self.angle)