# Catcher

from ple import PLE
from ple.games.catcher import Catcher
import pygame
import time, sys
from pygame.locals import *
import random

game = Catcher(256,256,1)

p = PLE(game, display_screen=True)
p.init()

print(p.getActionSet())
action_set = p.getActionSet()

nb_frames = 1000

for f in range(nb_frames):
    p.act(random.choice(action_set))
    time.sleep(.01)
    if p.game_over():
        sys.exit()
