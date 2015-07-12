__author__ = 'PtGaming'

###########
# CLASSES #
###########

class PtGamingError(Exception): #Custom error. (Exception) inherits all rights from the default Exception class
    pass #Do nothing

###########
# IMPORTS #
###########

while True:
    try:
        import pygame #Import pygame module
        print("pygame imported") #Tell user that pygame was imported successfully
        break #break the loop

    except ImportError: #If there was a fault
        error = "module: pygame could not be imported" #Declare the error
        raise PtGamingError(error) #Raise the error

while True:
    try:
        import solar_system #Import solar_system module
        print("solar_system imported") #Tell user that time was imported
        break #Break the loop

    except ImportError: #If it failed to import
        error = "module: solar_system could not be imported" #Declare the error
        raise PtGamingError(error) #Raise the error

while True:
    try:
        import math #Import math module
        print("math imported") #Tell user that the module was imported
        break #Break the loop

    except ImportError: #If it failed
        error = "module: math could not be imported" #Declare the error
        raise PtGamingError(error) #Raise the error

###############
# PRE-LOADING #
###############

# DECLARE COLOURS #
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PURPLE = (127, 0, 255)
CYAN = (0, 255, 255)
ORANGE = (255, 127, 0)

# INITIALISE CORE #
pygame.init()
display_size = [1000, 650] # [x, y]
screen = pygame.display.set_mode(display_size)
pygame.display.set_caption("SPACE SIMULATOR")
clock = pygame.time.Clock()

# VARIABLES #
sun = [int(display_size[0] * 0.5), int(display_size[1] * 0.5)] #Center of the screen
close = False

# OBJECTS #
# EARTH #
Earth = solar_system.Planet() #Importing my custom module, declaring the object.
Earth.colour = BLUE #Editing the traits of the object
Earth.radius = 220
# Moons
earth_moons = [[0.14, math.pi, 50, WHITE, 5],
               [0.14, 2 * math.pi, 50, WHITE, 5],
               [0.12, 3 * math.pi / 2, 60, WHITE, 5],
               [0.11, math.pi, 75, WHITE, 4]] #2 dimensional array

# MERCURY #
Mercury = solar_system.Planet()
Mercury.colour = RED
Mercury.radius = 70
Mercury.size = 4
Mercury.speed = 0.04

# VENUS #
Venus = solar_system.Planet()
Venus.colour = ORANGE
Venus.radius = 120
Venus.speed = 0.03
# Moons
venus_moons = [[0.1,        #Speed of the moon
                math.pi,    #Starting angle of moon
                25,         #Radius from planet
                WHITE,      #Colour of the moon (list)
                4]]         #Radius/size of the moon

# MARS #
Mars = solar_system.Planet()
Mars.colour = RED
Mars.radius = 280
Mars.speed = 0.008
Mars.size = 4

# PTGAMING (MY PLANET) #
PtGaming = solar_system.Planet()
PtGaming.colour = PURPLE
PtGaming.speed = 0.017
PtGaming.angle = 2 * math.pi
PtGaming.size = 25
PtGaming.radius = 350
# Moons
PtGaming_moons = [[0.145, math.pi, 35, WHITE, 5],
                 [0.125, math.pi, 45, WHITE, 5],
                 [0.115, 3 * math.pi / 2, 55, WHITE, 3],
                 [0.095, math.pi, 65, WHITE, 2],
                 [0.095, 2 * math.pi, 65, WHITE, 3]]

################
# MAIN PROGRAM #
################

while True:
    ##########
    # EVENTS #
    ##########
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #If X is clicked
            close = True #Exit the program
    
    ##############
    # USER INPUT #
    ##############
    
    action = pygame.key.get_pressed() #Get all keys (adds them to a list) and sets pressed keys to True
    if action[pygame.K_LCTRL] and action[pygame.K_c]: #CTRL + C
        close = True

    ##############
    # LOGIC CODE #
    ##############

    #No logic code. It's all handled in drawing and in the solar_system module

    ################
    # DRAWING CODE #
    ################

    screen.fill(BLACK) #Empty the screen
    
    # PLANETS #
    Earth.Orbit(screen, sun) #Calls the orbit procedure of the Planet class. Uses parameters screen (destination to draw) and sun (focus to orbit around)
    Mercury.Orbit(screen, sun)
    Venus.Orbit(screen, sun)
    Mars.Orbit(screen, sun)
    PtGaming.Orbit(screen, sun)

    # MOONS #
    venus_moons = Venus.Moon(screen, venus_moons) #Calls the moon function of the Planet class. Uses parameters screen (destination to draw) and moons:list to update the moons.
    earth_moons = Earth.Moon(screen, earth_moons)
    PtGaming_moons = PtGaming.Moon(screen, PtGaming_moons)
    pygame.draw.circle(screen, YELLOW, sun, 50) #The Sun

    # UPDATE #
    pygame.display.flip() #Update the display
    clock.tick(60) #60 ticks per second ~ 60 frames per second

    # EXTRA #
    if close:
        break

pygame.quit() #Close the pygame module
