from gpiozero import LightSensor
ldr = LightSensor(4)
ldr.when_dark = lambda : print("INTRUDER")
