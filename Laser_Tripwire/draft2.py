from gpiozero import LightSensor
import pygame
pygame.init()
ldr = LightSensor(4)
siren = pygame.mixer.Sound("/home/pi/siren.wav")
ldr.when_dark = lambda: siren.play()
