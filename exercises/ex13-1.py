# 13-1. Stars: Find an image of a star. Make a grid of stars appear on the screen.

import pygame
import sys

from star import Star

class Stars:
    def __init__(self) -> None:
        """Initialize the game, and create game resources"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption('Alien Invasion')