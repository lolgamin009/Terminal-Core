import main

#This is the variable ROM
def defaultvalues():
    global state, temp, status, plaser1, plaser2, plaser3, plaser4, claser1, claser2, TPS
    temp = 300
    status = 0
    plaser1 = 0
    plaser2 = 0
    plaser3 = 0
    plaser4 = 0
    claser1 = 0
    claser2 = 0
    state = 0
    TPS = 30

def init():
    defaultvalues()
    main.pygame.init()

#This is the ASCII Art ROM
def mainmenu():
    pass

def rec0image():
    pass