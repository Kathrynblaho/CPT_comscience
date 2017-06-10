"""
"""
#import pygame library
import pygame

#import randpom library
import random

# Define some colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (38, 206, 8)
PURPLE = (222, 94, 255)
LIGHT_PURPLE= (235, 155, 255)

# Call this function so the Pygame library can initialize itself
pygame.init()

# Create an 800x600 sized screen
screen = pygame.display.set_mode([800, 600])

# This sets the name of the window
pygame.display.set_caption('Bye Bye Bloop!')


# Used to manage how fast the screen updates
clock = pygame.time.Clock()


# Set position of Background
background_position = [0, 0]

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Starting position of the rectangle
rect_x = 50
rect_y = 50

# Speed and direction of rectangle
rect_change_x = 5
rect_change_y = 5

#Timer variables
frame_count = 0
frame_rate = 60

#Health
health = 5

#initialize font
font = pygame.font.Font(None, 50)

# Load and set up graphics.
background_image = pygame.image.load("blue.jpg").convert()

bloop_image = pygame.image.load("bloop_square.png").convert()
bloop_image.set_colorkey(WHITE)

bloop_image_LARGE = pygame.image.load("Bloop LARGER.png").convert()
bloop_image_LARGE.set_colorkey(WHITE)

main_menu = pygame.image.load("MenuBloop.png").convert()

bloop_dead = pygame.image.load("dead_bloop.png").convert()
bloop_dead.set_colorkey(WHITE)

icon_image = pygame.image.load("iconbloop.png").convert()

rock_image = pygame.image.load("rock_spiky.png").convert()
rock_image.set_colorkey(WHITE)

#Set game icon on window
pygame.display.set_icon(icon_image)

#Create list to store location or random clouds
cloud_list = []
for i in range(4):
    x = random.randrange(-170,800)
    y = random.randrange(-170,410)
    cloud_list.append( [x,y] )

rock_list = []
for i in range(4):
    x_rock = random.randrange(-170,800)
    y_rock = random.randrange(-170,400)
    rock_list.append( [x_rock,y_rock] )

#define cloud function
def cloudDraw(screen,x,y):
    for item in cloud_list:
        item[0] -= 2
        pygame.draw.ellipse(screen, WHITE, [item[0],item[1],90,50], )
        pygame.draw.ellipse(screen, WHITE, [item[0] + 30,item[1] + 30,90,50], )
        pygame.draw.ellipse(screen, WHITE, [item[0] + 30,item[1] + 30,90,50], )
        pygame.draw.ellipse(screen, WHITE, [item[0] + 30,item[1] - 30,90,50], )
        pygame.draw.ellipse(screen, WHITE, [item[0] + 75,item[1] - 10,90,50], )
        pygame.draw.ellipse(screen, WHITE, [item[0] + 75,item[1] + 30,90,50], )
        pygame.draw.ellipse(screen, WHITE, [item[0] + 98,item[1] + 10,90,50], )

        if item[0] < -180:
            item [0] = 800
            item [1] = random.randrange(400)

def timer():
    global frame_count
    global frame_rate
    # --- Timer going up ---
    # Calculate total seconds
    total_seconds = frame_count // frame_rate

    # Divide by 60 to get total minutes
    minutes = total_seconds // 60

    # Use modulus (remainder) to get seconds
    seconds = total_seconds % 60

    # Use python string formatting to format in leading zeros
    output_string = "Time: {0:02}:{1:02}".format(minutes, seconds)

    # Blit to the screen
    text = font.render(output_string, True, BLACK)
    screen.blit(text, [0, 0])

    # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
    frame_count += 1

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()


#define grass function
def grassDraw(screen,x,y):
    pygame.draw.rect(screen, GREEN, [x,y,800,200] )

def rockDraw(x_rock_1,y_rock_1):
        screen.blit(rock_image, (x_rock_1,y_rock_1))



#define button function
def button(message, x, y, w,h, colour_1, colour_2, action = None):
        #Position of mouse
        mouse = pygame.mouse.get_pos()

        #If mouse is clicked
        click = pygame.mouse.get_pressed()

        #Button colour change
        if x + w > mouse[0] > x and y+h > mouse[1] > y:
            pygame.draw.rect(screen, colour_2,(x,y,w,h))

            if click[0] == 1 and action != None:
                action()
        else: pygame.draw.rect(screen, colour_1,(x,y,w,h))



        #button message
        text = font.render(message, True, BLACK)
        screen.blit(text, [x + 10, y + 20])

def message_display(text,colour,size,x,y):
    font = pygame.font.Font(None, size)
    text = font.render(text, True, colour)
    screen.blit(text, [x,y])

    pygame.display.update()

def game_over():
    screen.fill (BLACK)
    screen.blit(bloop_dead, [260, 200])
    message_display('Oh No! Bloop Is Dead',WHITE,90,80,100)
    pygame.time.delay(3000)
    game_intro()


def game_intro():
    intro = True

    while intro:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        game_loop()
            elif event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.blit(main_menu, [0,0])
        screen.blit(bloop_image_LARGE, [260, 200])

        button("START", 110,470,230,70, PURPLE, LIGHT_PURPLE, game_loop)
        button("HIGHSCORES", 420,470,250,70, PURPLE, LIGHT_PURPLE)

        pygame.display.update()
        clock.tick(15)

def game_loop():

    # -------- Main Game Loop -----------

    #Set Variables

    # Speed of Bloop
    x_speed = 0
    y_speed = 0

    # Current position of Bloop
    x_coord = 10
    y_coord = 200

    #Set health counter
    health = 10
    if health == 0:
        game_over()

##################################################################################
    #Speed of rocks
    rock_speed = -5

    #FIRST ROCK LOCATION
    rock_start_x_1 = random.randrange(600,950)
    rock_start_y_1 = random.randrange(0,400)

    #SECOND ROCK LOCATION
    rock_start_x_2 = random.randrange(600,950)
    rock_start_y_2 = random.randrange(0,400)

    #THIRD ROCK LOCATION
    rock_start_x_3 = random.randrange(600,950)
    rock_start_y_3 = random.randrange(0,400)

    #FOURTH ROCK LOCATION
    rock_start_x_4 = random.randrange(600,950)
    rock_start_y_4 = random.randrange(0,400)


#################################################################################
    #initiate game loop
    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            #If user presses a key
            elif event.type == pygame.KEYDOWN:
                # Figure out if it was an arrow key. If so
                # adjust speed.
                if event.key == pygame.K_LEFT:
                    x_speed = -6
                elif event.key == pygame.K_RIGHT:
                    x_speed = 6
                elif event.key == pygame.K_UP:
                    y_speed = -6
                elif event.key == pygame.K_DOWN:
                    y_speed = 6

            #When user lifts up arrow key change speed back to zero
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_speed = -1
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_speed = 0

#####################################################################################
        #GAME LOGIC:

        #Set up screen boundaries
        if x_coord > 730:
            x_coord = 730
        elif x_coord < -110:
            game_over()
        elif y_coord > 410:
            y_coord = 410
        elif y_coord < 0:
            y_coord = 0

        # Move the bloop according to the speed vector.
        x_coord = x_coord + x_speed
        y_coord = y_coord + y_speed

#############################################################################################
    #FIRST Rock logic
        if rock_start_x_1 < -180:
            rock_start_x_1 = random.randrange(800,990)
            rock_start_y_1 = random.randrange(0,400)

        if y_coord < rock_start_y_1 + 36 and y_coord + 88 > rock_start_y_1 and x_coord < rock_start_x_1 + 40 and x_coord + 68 > rock_start_x_1:
                health = health - 1
        # Bounce Bloop away from ememy

                y_speed = y_speed * -1
                x_speed = x_speed * -1
                if x_coord + 68 > rock_start_x_1:
                    x_speed = -8
                    if x_coord == 20:
                        x_speed = 0
##############################################################################################
    #SECOND Rock logic
        if rock_start_x_2 < -180:
            rock_start_x_2 = random.randrange(800,990)
            rock_start_y_2 = random.randrange(0,400)

        if y_coord < rock_start_y_2 + 36 and y_coord + 88 > rock_start_y_2 and x_coord < rock_start_x_2 + 40 and x_coord + 68 > rock_start_x_2:
                health = health - 1
        # Bounce Bloop away from ememy

                y_speed = y_speed * -1
                x_speed = x_speed * -1
                if x_coord + 68 > rock_start_x_2:
                    x_speed = -8
                    if x_coord == 20:
                        x_speed = 0

#############################################################################################
    #THIRD Rock logic
        if rock_start_x_3 < -180:
            rock_start_x_3 = random.randrange(800,990)
            rock_start_y_3 = random.randrange(0,400)

        if y_coord < rock_start_y_3 + 36 and y_coord + 88 > rock_start_y_3 and x_coord < rock_start_x_3 + 40 and x_coord + 68 > rock_start_x_3:
                health = health - 1
        # Bounce Bloop away from ememy

                y_speed = y_speed * -1
                x_speed = x_speed * -1
                if x_coord + 68 > rock_start_x_3:
                    x_speed = -8
                    if x_coord == 20:
                        x_speed = 0
##############################################################################################
    #FOURTH Rock logic
        if rock_start_x_4 < -180:
            rock_start_x_4 = random.randrange(800,990)
            rock_start_y_4 = random.randrange(0,400)

        if y_coord < rock_start_y_4 + 36 and y_coord + 88 > rock_start_y_4 and x_coord < rock_start_x_4 + 40 and x_coord + 68 > rock_start_x_4:
                health = health - 1
        # Bounce Bloop away from ememy

                y_speed = y_speed * -1
                x_speed = x_speed * -1
                if x_coord + 68 > rock_start_x_4:
                    x_speed = -8
                    if x_coord == 20:
                        x_speed = 0

############################################################################################
        #DRAWING CODE:


        # Copy Background image to screen:
        screen.blit(background_image, background_position)

        #Draw image of cloud
        cloudDraw(screen,0,0)

        #Image of Bloop on screen
        screen.blit(bloop_image, [x_coord, y_coord])

        #Draw immage of Grass
        grassDraw(screen, 0,500)
###########################################################################################
        #Draw rocks

        #Draw first rock
        rockDraw(rock_start_x_1, rock_start_y_1)
        rock_start_x_1 += rock_speed

        #Draw second rock
        rockDraw(rock_start_x_2, rock_start_y_2)
        rock_start_x_2 += rock_speed

        #Draw third rock
        rockDraw(rock_start_x_3, rock_start_y_3)
        rock_start_x_3 += rock_speed

        #Draw fourth rock
        rockDraw(rock_start_x_4, rock_start_y_4)
        rock_start_x_4 += rock_speed
##########################################################################################
        #Health Display
        message_display(("Health: {0}".format(health)),BLACK,50,220,0)

        #Display Timer on screen
        timer()

        #Update Screen

        pygame.display.flip()

        #Limit to 60 frames per second

        clock.tick(60)



game_intro()
game_loop()
#Close window and quit
pygame.quit()