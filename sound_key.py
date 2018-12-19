import pygame
import time
import sys

pygame.init()
pygame.mixer.init()

COLOR = (255,255,255)
screen = pygame.display.set_mode((500,400))
screen.fill(COLOR)
pygame.display.flip()

snare   = pygame.mixer.Sound('snare_drum.wav')
floor   = pygame.mixer.Sound('floor_tom.wav')
tom1    = pygame.mixer.Sound('tomtom.wav')
tom2    = pygame.mixer.Sound('tomtom2.wav')
crash   = pygame.mixer.Sound('cymbal.wav')
hat     = pygame.mixer.Sound('high_hat_cymbal.wav')
ride    = pygame.mixer.Sound('cymbal2.wav')
bass    = pygame.mixer.Sound('bass_drum.wav')

def keyboard_to_sound():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    print('key: s       - Sound of snare Drum')
                    snare.play()
                elif event.key == pygame.K_l:
                    print('key: l       - Sound of Floor Drum')
                    floor.play()
                elif event.key == pygame.K_r:
                    print('key: r       - Sound of Tom tom1')
                    tom1.play()
                elif event.key == pygame.K_u:
                    print('key: u       - Sound of Tom Tom2')
                    tom2.play()
                elif event.key == pygame.K_TAB:
                    print('key: tab     - Sound of Crash Cymbal')
                    crash.play()
                elif event.key == pygame.K_CAPSLOCK:
                    print('key: Caps    - Sound of Hat Cymbal')
                    hat.play()
                elif event.key == pygame.K_p:
                    print('key: p       - Sound of Ride Cymbal')
                    ride.play()
                elif event.key == pygame.K_SPACE:
                    print('key: Space   - Sound of Bass Drum')
                    bass.play()

keyboard_to_sound()
pygame.quit()
