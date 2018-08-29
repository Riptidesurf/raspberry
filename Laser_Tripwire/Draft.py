#Added to check versioinng
from gpiozero import LightSensor
import pygame
pygame.init()
ldr = LightSensor(4)
siren = pygame.mixer.Sound("/home/pi/tornado_siren.wav")
ldr.when_dark = lambda: siren.play()
#ldr.when_light = lambda: siren.stop()
