import pygame
import time
pygame.mixer.init()
band = pygame.mixer.Sound("beat11.wav")
while True:
    band.play()
    time.sleep(2.0)
