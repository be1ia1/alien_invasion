import pygame
from pygame.sprite import _Group, Sprite

class Star(Sprite):
    """A class to represent a single alien in the fleet."""
    def __init__(self) -> None:
        super().__init__()
        