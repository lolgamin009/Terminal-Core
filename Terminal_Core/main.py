import ROM
import pygame
import winsound
import subprocess

ROM.init()
subprocess.run("cls", shell=True)

#This is the Mainloop
while True:
    if ROM.state == 0:
        pass
    elif ROM.state == 1:
        pass
    elif ROM.state == 2:
        pass
    elif ROM.state == 3:
        pass
    elif ROM.state == 4:
        pass
    else:
        print("GTFO YOU DIRTY HACKER")
        exit("GOODBYE")
    pygame.time.Clock.tick(ROM.TPS)