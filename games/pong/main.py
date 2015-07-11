__author__ = "PtGaming"
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
        import time #Import time module
        print("time imported") #Tell user that time was imported
        break #Break the loop

    except ImportError: #If it failed to import
        error = "module: time could not be imported" #Declare the error
        raise PtGamingError(error) #Raise the error

while True:
    try:
        import random #Import random module
        print("random imported") #Tell user that the module was imported
        break #Break the loop

    except ImportError: #If it failed
        error = "module: random could not be imported" #Declare the error
        raise PtGamingError(error) #Raise the error
    
###########
# CLASSES #
###########

class PtGamingError(Exception): #My custom error
    pass #Do nothing, Exception calls itself

##############
# PROCEDURES #
##############

def MLG_Procedure():
    global MLG
    if MLG:
        hitmarker = random.randint(0,3)
        if hitmarker == 1:
            pygame.mixer.Sound("sound\\triangle.wav").play()

        else:
            pygame.mixer.Sound("sound\\triangle.wav").play()

def Scored(): #When the ball hits an edge behind a player
    global ball_x, ball_y, ballspeed_x, ballspeed_y, player1_score, player2_score, score_limit #Retrieve gloabal values
    if player1_score != score_limit and player2_score != score_limit: #If the game is still active
        if not MLG:
            pygame.mixer.Sound("sound\\end.wav").play() #Play a little effect

        else:
            hitmarker = random.randint(0,2)
            if hitmarker != 1:
                pygame.mixer.Sound("sound\\camera.wav").play()

            else:
                pygame.mixer.Sound("sound\\noscope.wav").play()
        
                
    ball_x = int(display_size[0] * 0.5) #Put ball back in center of screen
    ball_y = int(display_size[1] * 0.5)
    ballspeed_x = 0 #Stop the ball moving
    ballspeed_y = 0
    return True #start = True

###############
# PRE-LOADING #
###############

print("Initialising pygame engine")
pygame.init() #Initialise the engine
print("pygame engine initialised")

fontsize = 30
font = pygame.font.SysFont("sans", fontsize, bold=True) #Declare the font

display_size = (1024, 576) #Display Size (Feel free to edit size, everything changes accordingly)
print("Display size set at: X:{0} Y:{1}".format(display_size[0], display_size[1])) #Print the display config

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY_DARK = (73, 73, 73)
GREY_LIGHT = (191, 191, 191)
RED = (255, 0, 0)
MLG_colour = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]
#Declare the colours (RRR, GGG, BBB)

player1_xaxis = int(0 + (display_size[0] * 0.05)) #Align player 1 accordingly to the display size
player1_yaxis = int(display_size[1] * 0.5)
player1_score = 0
player2_xaxis = int(display_size[0] - (display_size[0] * 0.05)) #Align player 2 accordingly to the display size
player2_yaxis = int(display_size[1] * 0.5)
player2_score = 0
#Player data variables

ball_x = int(display_size[0] * 0.5) #Ball start location
ball_y = int(display_size[1] * 0.5)
ballspeed_x = 0
ballspeed_y = 0
#Ball variables

delay = 0
MLGdelay = 0
stopdelay = 0
scored = 0
bg = 0
score_limit = 8 #The score limit, feel free to change
#Declare integer variables

close = False
start = True
MLG = False
antispam = False
#Declare boolean variables

screen = pygame.display.set_mode(display_size) #Start the display
pygame.display.set_caption("PONG (2 Player)") #Set the title
clock = pygame.time.Clock() #Declare the clock
#time.sleep(2)

################
# MAIN PROGRAM #
################

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            close = True

        if event.type == pygame.KEYUP:
            antispam = False

    action = pygame.key.get_pressed() #The key(s) that is/are pressed.

    if (action[pygame.K_LCTRL] and action[pygame.K_c]) or action[pygame.K_ESCAPE]:
        close = True
    
    if action[pygame.K_DOWN]: #If player 2 presses down
        if player2_yaxis <= display_size[1] - 60: #Collision area
            player2_yaxis += 10 #Player 2 speed

    if action[pygame.K_UP]: #If player 2 presses up
        if player2_yaxis >= 0: #Collision area
            player2_yaxis -= 10 #Player 2 speed

    if action[pygame.K_s]: #If player 1 presses down
        if player1_yaxis <= display_size[1] - 60: #Collision area
            player1_yaxis += 10 #Player 1 speed

    if action[pygame.K_w]: #If player 1 presses up
        if player1_yaxis >= 0: #Collision area
            player1_yaxis -= 10 #Player 1 speed

    if action[pygame.K_SPACE] and not antispam:
        antispam = True
        if MLG:
            MLG = False

        else:
            MLG = True
            hitmarker = random.randint(0,3)
            if hitmarker != 0:
                pygame.mixer.Sound("sound\\triangle.wav").play()

            else:
                pygame.mixer.Sound("sound\\triangle.wav").play()

            

    screen.fill(BLACK) #Fill it with nothing-ness
    
    if MLG:
        pygame.draw.rect(screen, random.choice(MLG_colour), pygame.Rect(player1_xaxis, player1_yaxis, 10, 60))
        pygame.draw.rect(screen, random.choice(MLG_colour), pygame.Rect(player2_xaxis, player2_yaxis, 10, 60))
        pygame.draw.circle(screen, random.choice(MLG_colour), (ball_x, ball_y), 10)

    else:
        pygame.draw.rect(screen, GREY_LIGHT, pygame.Rect(player1_xaxis, player1_yaxis, 10, 60)) #Draw player 1
        pygame.draw.rect(screen, GREY_DARK, pygame.Rect(player2_xaxis, player2_yaxis, 10, 60)) #Draw player 2
        pygame.draw.circle(screen, WHITE, (ball_x, ball_y), 10) #Draw the ball
    score_screen1 = font.render(("{0}".format(player1_score)), 1, RED) #Declare player 1 score
    score_screen2 = font.render(("{0}".format(player2_score)), 1, RED) #Declare player 2 score
    screen.blit(score_screen1, ((display_size[0] * 0.25), (display_size[0] * 0.1))) #Draw player 1 score
    screen.blit(score_screen2, ((display_size[0] * 0.75), (display_size[0] * 0.1))) #Draw player 2 score

    if ball_y > (display_size[1] - 10) and ball_y < (display_size[1] + 10) and ballspeed_y > 0: #If the ball hits the collision area
        ballspeed_y *= -1 #Reverse the direction
        if not MLG:
            pygame.mixer.Sound("sound\\beep.wav").play() #And play a sound

        else:
            pygame.mixer.Sound("sound\\hit.wav").play()

    else: #If the ball isn't in a collision area
        ball_y += ballspeed_y #Move the ball

    if ball_y > -10 and ball_y < 10 and ballspeed_y < 0: #If the ball hgits the other collision area 69 lol
        ballspeed_y *= -1 #Reverse the direction
        if not MLG:
            pygame.mixer.Sound("sound\\beep.wav").play() #And play a sound

        else:
            pygame.mixer.Sound("sound\\hit.wav").play()

    else: #If the ball isn't in the collision area
        ball_y += ballspeed_y #Move the ball

    player1_data = [(player1_yaxis - 10), (player1_yaxis + 70)] #Player 1 size data
    player2_data = [(player2_yaxis - 10), (player2_yaxis + 70)] #Player 2 size data
    player1_calc1 = player1_data[1] - ball_y 
    player1_calc2 = player1_data[0] - ball_y
    player2_calc1 = player2_data[1] - ball_y
    player2_calc2 = player2_data[0] - ball_y
    #Calculations to define if the ball is in-line with the player(s)
    if ballspeed_x > 0: #If the ball is moving towards player 2
        if ball_x > (display_size[0] - 10) and ball_x < (display_size[0] + 10) and ballspeed_x > 0: #And player 2 misses
            player1_score += 1 #Player 1 scored a goal
            start = Scored() #Call the Scored function
            scored = 1 #Player 1 scored

        elif player2_calc1 > 0 and player2_calc2 < 0: #If player 2 is in the way
            if (ball_x + 10) >= player2_xaxis and (ball_x + 10) <= (player2_xaxis + 10): #And the ball collides with player 2
                ballspeed_x *= -1 #Reverse the direction
                if not MLG:
                    pygame.mixer.Sound("sound\\beep.wav").play() #And play a sound

                else:
                    pygame.mixer.Sound("sound\\hit.wav").play()
                    
                if action[pygame.K_UP]: #If player 2 was moving up (down)
                    ballspeed_y -= 1 #Decrease (increase) the y speed of the ball

                elif action[pygame.K_DOWN]: #If player 2 was moving down (up)
                    ballspeed_y += 1 #Increase (decrease) the y speed of the ball

            else:
                ball_x += ballspeed_x #Continue moving

        else:
            ball_x += ballspeed_x #Continue moving

    else: #If the ball is moving towards player 1
        if ball_x > -10 and ball_x < 10 and ballspeed_x < 0: #And player 1 misses
            player2_score += 1 #Player 2 scored a goal
            start = Scored() #Call the Scored function
            scored = 2 #Player 2 scored

        elif player1_calc1 > 0 and player1_calc2 < 0: #If player 1 is in the way
            if (ball_x - 10) <= (player1_xaxis + 10)  and (ball_x - 10) > player1_xaxis: #And the ball collides with them
                ballspeed_x *= -1 #Reverse the direction
                if not MLG:
                    pygame.mixer.Sound("sound\\beep.wav").play() #And play a sound

                else:
                    pygame.mixer.Sound("sound\\hit.wav").play()
                    
                if action[pygame.K_w]: #If they were moving up (down)
                    ballspeed_y -= 1 #Decrease (increase) the y speed of the ball

                elif action[pygame.K_s]: #If they were moving down (up)
                    ballspeed_y += 1 #Increase (decrease) the y speed of the ball

            else:
                ball_x += ballspeed_x #Continue moving

        else:
            ball_x += ballspeed_x #Continue moving

    if MLGdelay < 1200:
        MLGdelay += 1

    else:
        MLG_Procedure()
        MLGdelay = 0
        
    clock.tick(60) #60 Frames Per Second
    if start: #If the game/round has started
        if player1_score == score_limit or player2_score == score_limit: #If someone has won
            player = "PLAYER 2" #Player 2 wins!
            if player1_score == score_limit: #Unless player 1 actually won
                player = "PLAYER 1"
            #This is simpler, and shorter than using if; else
                
            pygame.mixer.Sound("sound\\win.wav").play() #Play the win sound
            if not MLG:
                win_screen = font.render(("{0} WINS!".format(player)), 1, RED) #Declare the winning player
                close = True
                time.sleep(5)

            else:
                win_screen = font.render(("DEAL WITH IT"), 1, random.choice(MLG_colour))
                if stopdelay < 180:
                    stopdelay += 1

                else:
                    close = True
                
            screen.blit(win_screen, ((display_size[0] * 0.5), (display_size[1] * 0.5))) #Display the winning player
            
        randomdelay = random.randint(180, 600) #Wait 180 - 600 ticks for the ball to move
        if delay < randomdelay: #Wait until the delay passes the random delay
            delay += 1

        else:
            if scored == 1: #If player 1 scored
                ballspeed_x = random.randint(8,9) #Throw the ball at player 2
                
            else: #If player 1 didn't score
                ballspeed_x = random.randint(8,9) * -1 #Throw the ball at player 1
                
            start = False #Reset the variables
            delay = 0
            if not MLG:
                pygame.mixer.Sound("sound\\whoosh.wav").play() #Play sound to declare ball moving

            else:
                pygame.mixer.Sound("sound\\horn.wav").play()

    pygame.display.flip() #Update the screen
    if close: #If closing
        break #BreakTheCycle

pygame.quit() #Close the program
print("P1: {0}\nP2: {1}".format(player1_score, player2_score)) #Print the player scores
