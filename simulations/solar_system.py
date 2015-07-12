__author__ = 'PtGaming'

import math
import pygame

class CoreError(Exception):
    pass

if __name__ == "__main__": #If running from shell
    error = "Running this module has been disabled. Import-only"
    raise CoreError(error) #Raise Error

class Planet(): #Class Planet. Does not inherit any characteristics from pre-defined classes
    """ object parts are x=0, y=0, speed=0.01, angle=math.pi, radius=100, colour=(0,0,0), size=10
    x is x position on screen, y is same
    speed is the velocity of rotation around the focus point (defined in orbit)
    angle is the angle of the object, works well with [x,y]
    radius is distance from focus point
    colour is the colour of the object
    size is the size of the object (radius of the circle)
    """
    def __init__(self): #Pre-determined values when initialising an object
        self.x = 0 #Planet x position. Not really needed, but useful just in-case.
        self.y = 0 #Copy + Paste ^^^
        self.speed = 0.01 #Speed of the planet
        self.angle = math.pi #Starting angle of the planet
        self.radius = 100 #Orbiting distance around the focus
        self.colour = (0, 0, 0) #Colour of the planet (This is black, so it would be invisible)
        self.size = 10 #Radius/size of the planet

    def Orbit(self, screen, center): #Procedure Orbit. Edits the x,y position of the object
        """
        Orbits the object around the focus (center)
        Does not return any values
        :param screen: The display
        :param center: The object that the Planet orbits around
        :return:
        """
        self.angle += self.speed #Change the angle
        self.x = int(self.radius * math.sin(self.angle) + int(center[0])) #This is too difficult to explain. Draw a CAST diagram and map sin and cos
        self.y = int(self.radius * math.cos(self.angle) + int(center[1])) 
        pygame.draw.circle(screen, self.colour, [self.x, self.y], self.size) #Draw the object on the screen.

    def Moon(self, screen, data=None): #Function Moon. Edits the x,y position of each moon and returns it to the main program
        """
        :param screen: The display
        :param data: The returned data for the moons
        [[speed, angle, radius, colour, size]]
        data must be a 2 dimensional array and is returned
        :return: Returns data after updated by function
        """
        if data == None: #If no moons, return None
            return None

        updated_data = [] #New list for updated moon data
        for moon in data:
            moon_speed = moon[0] #Get the values of each moon
            moon_angle = moon[1]
            moon_radius = moon[2]
            moon_colour = moon[3]
            moon_size = moon[4]
            moon_angle += moon_speed #Change the angle
            moon_x = int(moon_radius * math.sin(moon_angle) + self.x) #Again, a CAST diagram could explain much more than I could.
            moon_y = int(moon_radius * math.cos(moon_angle) + self.y) #As well as basic physics
            pygame.draw.circle(screen, moon_colour, [moon_x, moon_y], moon_size) #Draw the moon on the screen. (Buggy with a lot of moons)
            new_moon_data = moon_speed, moon_angle, moon_radius, moon_colour, moon_size #Append the new moon data to the new list
            updated_data.append(new_moon_data)

        return updated_data #Return the new list to the main program. Ready to be edited again.
        #This could all be done with self.moon_angle etc... but that would only allow for one moon unless using tuples.
        #Whereas this seemed like a much easier solution. Although it requires a 2 dimensional array, else IndexError
