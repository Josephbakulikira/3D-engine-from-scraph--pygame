import pygame
from constants import *

def HandleEvent(camera, deltaTime):
    running = True
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        if event.type == pygame.MOUSEMOTION:
            if pygame.mouse.get_pressed()[0]:
                x, y = event.rel
                x /= mouse_sensitivity
                y /= mouse_sensitivity
                camera.HandleMouseEvent(x, y, deltaTime)

    return running
