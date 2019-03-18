# Water World

from ple import PLE
from ple.games.waterworld import WaterWorld
import pygame
import time, sys
from pygame.locals import *
import random

game = WaterWorld(800,800,4)

p = PLE(game, display_screen=True)
p.init()

print(p.getActionSet())
action_set = p.getActionSet()

nb_frames = 1000000

for f in range(nb_frames):
    if p.game_over():
        sys.exit()
    p.act(random.choice(action_set))
    time.sleep(.05)

