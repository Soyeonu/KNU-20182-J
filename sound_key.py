import pygame
import time
import sys
from time import sleep

pygame.init()
pygame.mixer.init()

COLOR = (255,255,255)
screen = pygame.display.set_mode((500,400))
screen.fill(COLOR)
pygame.display.flip()

drum	 = pygame.image.load("drum_image_f.jpg")
light 	 = pygame.image.load("light.png")
light2	 = pygame.image.load("light2.png")
light3   = pygame.image.load("light3.png")
shaking	 = pygame.image.load("shaking.png")
shaking2 = pygame.image.load("shaking2.png")

snare    = pygame.mixer.Sound('snare_drum.wav')
floor    = pygame.mixer.Sound('floor_tom.wav')
tom1     = pygame.mixer.Sound('tomtom.wav')
tom2     = pygame.mixer.Sound('tomtom2.wav')
crash    = pygame.mixer.Sound('cymbal.wav')
hat      = pygame.mixer.Sound('high_hat_cymbal.wav')
ride     = pygame.mixer.Sound('cymbal2.wav')
bass     = pygame.mixer.Sound('bass_drum.wav')

screen.blit(drum,(50,50))

def sound_to_image(num):
    if num == 1:
        screen.blit(shaking,(100,200))  #snare
        pygame.display.update()
        sleep(0.5)
        screen.blit(drum,(50,50))
        pygame.display.update()
    elif num == 2:
        screen.blit(shaking2, (320,195))#floor
        pygame.display.update()
        sleep(0.5)
        screen.blit(drum,(50,50))
        pygame.display.update()
    elif num == 3:
        screen.blit(light2,(160,130))   #tom1
        pygame.display.update()
        sleep(0.5)
        screen.blit(drum,(50,50))
        pygame.display.update()
    elif num == 4:
        screen.blit(light3,(260,135))   #tom2
        pygame.display.update()
        sleep(0.5)
        screen.blit(drum,(50,50))
        pygame.display.update()
    elif num == 5:
        screen.blit(light,(100,80))     #crash
        pygame.display.update()
        sleep(0.5)
        screen.blit(drum,(50,50))
        pygame.display.update()
    elif num == 6:
        screen.blit(light3,(400,130))   #hat
        pygame.display.update()
        sleep(0.5)
        screen.blit(drum,(50,50))
        pygame.display.update()
    elif num == 7:
        screen.blit(light2,(270,90))    #ride
        pygame.display.update()
        sleep(0.5)
        screen.blit(drum,(50,50))
        pygame.display.update()
    elif num == 8:
        screen.blit(shaking,(220, 230)) #bass
        pygame.display.update()
        sleep(0.5)
        screen.blit(drum,(50,50))
        pygame.display.update()
        

def keyboard_to_sound():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    print('key: s       - Sound of snare Drum')
                    snare.play()
                    sound_to_image(1)
                elif event.key == pygame.K_l:
                    print('key: l       - Sound of Floor Drum')
                    floor.play()
                    sound_to_image(2)
                elif event.key == pygame.K_r:
                    print('key: r       - Sound of Tom tom1')
                    tom1.play()
                    sound_to_image(3)
                elif event.key == pygame.K_u:
                    print('key: u       - Sound of Tom Tom2')
                    tom2.play()
                    sound_to_image(4)
                elif event.key == pygame.K_TAB:
                    print('key: tab     - Sound of Crash Cymbal')
                    crash.play()
                    sound_to_image(5)
                elif event.key == pygame.K_CAPSLOCK:
                    print('key: Caps    - Sound of Hat Cymbal')
                    hat.play()
                    sound_to_image(6)
                elif event.key == pygame.K_p:
                    print('key: p       - Sound of Ride Cymbal')
                    ride.play()
                    sound_to_image(7)
                elif event.key == pygame.K_SPACE:
                    print('key: Space   - Sound of Bass Drum')
                    bass.play()
                    sound_to_image(8)

keyboard_to_sound()
pygame.quit()
