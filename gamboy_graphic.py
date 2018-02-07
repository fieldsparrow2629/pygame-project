
#graphics project
#Erik B.

import pygame
import math
import random

pygame.init()

SIZE = (800,600)
TITLE = "Gameboy Graphic"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)



clock = pygame.time.Clock()
refresh_rate = 60

RED =(255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
WHITE = (255,255,255)
BLACK = (0,0,0)
ORANGE = (255,125,0)
GREY = (196, 190, 186)
MAGENTA = (196, 37, 92)
SCREEN_GREEN = (125,158,82)
GREY2 = (141,135,141)
SPACE_GREEN = (0,255,0)
SATURN = (187,162,121)
NEPTUNE = (72,115,253)
MARS = (254,132,95)
BLACKISH = (40,40,40)

#list of possible planet colors
planet_colors = [GREY,NEPTUNE,SATURN,MARS]

#pics
asteroid = pygame.image.load('photos/asteroid.png')
p1 = pygame.image.load('photos/planet_1.jpg')
link = pygame.image.load('photos/link.png')
kirby = pygame.image.load('photos/kirby.png')
mario = pygame.image.load('photos/mario.png')
pikachu = pygame.image.load('photos/pikachu.png')
charmander = pygame.image.load('photos/charmander.png')
megaman = pygame.image.load('photos/megaman.png')
donkeykong = pygame.image.load('photos/donkeykong.png')
yoshi = pygame.image.load('photos/yoshi.png')

sprite_list = [link,kirby,mario,pikachu,charmander,megaman,donkeykong,yoshi]

#sounds
lazer = pygame.mixer.Sound('sounds/lazer.ogg')

#music tracks
Donkey_Kong_Theme = 'sounds/Kong_Theme.ogg'
Ken_Stage_Theme = 'sounds/Ken_Stage.ogg'
Mario_Theme = 'sounds/Mario_Theme.ogg'

#list of all songs and the current song playing
song_list = [Donkey_Kong_Theme, Ken_Stage_Theme, Mario_Theme]
song_num = 0

#fonts
BIG_FONT = pygame.font.Font(None,50)
SMALL_FONT = pygame.font.Font(None, 25)

def draw_alien(a):
    x = a[0]
    y = a[1]
    pygame.draw.rect(screen,WHITE,a)
    pygame.draw.rect(screen,BLACK,[x + 4,y+2,3,3])
    pygame.draw.rect(screen,BLACK,[x + 14,y+2,3,3])
    pygame.draw.rect(screen,BLACK,[x + 4,y+14,12,3])
    pygame.draw.rect(screen,BLACK,[x+8,y+14,4,6])
    
    
def draw_invader(x,y):
    pygame.draw.rect(screen,SPACE_GREEN,[x,y,20,10])
    pygame.draw.rect(screen,SPACE_GREEN,[x + 7.5,y-10,5,10])

def draw_planet(x,y,color):
    pygame.draw.arc(screen,GREY,[x-40,y-27,80,40],0,math.pi,5)
    pygame.draw.circle(screen,color,[x,y],25)
    pygame.draw.arc(screen,GREY,[x-40,y-35,80,50],math.pi,2*math.pi,5)

def draw_bullet(loc):
    x = loc[0]
    y = loc[1]

    pygame.draw.rect(screen, SPACE_GREEN, [x,y,5,15])

def play_music():
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(-1)


#list of sprites and 'objects'
stars = []
aliens = []
planets = []
more_stars = []
asteroids = []
sprites =[]

#list of bullets
bullets = []

#makes list of aliens
for i in range(10):
    x = random.randrange(301,520)
    y = random.randrange(80,160)
    a = [x,y,20,20]
    aliens.append(a)

#makes list of stars
for i in range(50):
    x = random.randrange(301,530)
    y = random.randrange(71,240)
    r = 1
    s = [x,y,r,r]
    stars.append(s)
    
#makes list of more stars
for i in range(500):
    x = random.randrange(0,800)
    y = random.randrange(0,600)
    r = 1
    s = [x,y,r,r]
    more_stars.append(s)
    
#make list of planets
for i in range(5):
    x = random.randrange(1,800)
    y = random.randrange(1,600)
    c = random.choice(planet_colors)
    p = [x,y,c]
    planets.append(p)

#make list of asteroids
for i in range(20):
    x = random.randrange(1,800)
    y = random.randrange(1,600)
    a = [x,y]
    asteroids.append(a)

#list of sprites
for i in range(20):
    x = random.randrange(1,800)
    y = random.randrange(1,600)
    c = random.choice(sprite_list)
    a = [x,y,c]
    sprites.append(a)

#displays gameboy on
def game_on(xpos):
        pygame.draw.rect(screen,BLACK,[300,70,240,180])
        
        #stars
        for s in stars:
            pygame.draw.ellipse(screen,WHITE,s)

        #invader
        draw_invader(xpos,235)

        #draw aliens
        for a in aliens:
            draw_alien(a)
  

done = False
powered_on = False
shoot = False
show_instruction = True
music_playing = False

#invader location and speed
xpos = 410
speedx = 0

#game loop
while not done:
    #keeps checking and loading the song
    song = song_list[song_num]
    
    for event in pygame.event.get():
        
        
        if event.type == pygame.QUIT:
            done = True
            
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                powered_on = not powered_on
            elif event.key == pygame.K_RETURN:
                show_instruction = False
            elif event.key == pygame.K_RIGHT:
                speedx = 5
            elif event.key == pygame.K_LEFT:
                speedx = -5
            elif event.key == pygame.K_UP and powered_on:
                shoot = True
                lazer.play()
            elif event.key == pygame.K_x:
                song_num += 1
                if song_num >= len(song_list):
                    song_num = 0
                song = song_list[song_num]
                play_music()
                
            elif event.key == pygame.K_z:
                if music_playing:
                    pygame.mixer.pause()
                    music_playing = False
                else:
                    play_music()
                    music_playing = True
                
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                speedx = 0

    screen.fill(BLACK)
    
    '''processing'''
    
    #move sprites
    for s in sprites:
        s[0] -= 3
        s[1] += 3

        if s[0] < -115 or s[1] > 630:
            s[0] = random.randrange(400, 1000)
            s[1] = random.randrange(-250,-100)
            s[2] = random.choice(sprite_list)
    

    #move planets
    for p in planets:
        p[0] -= 1
        p[1] += 1

        if p[0] < -75 or p[1] > 630:
            p[0] = random.randrange(400, 1000)
            p[1] = random.randrange(-150,-50)
    
    #moves the invader
    if(xpos + speedx) <= 310:
        xpos = 310
    elif(xpos + speedx) >= 510:
        xpos = 510
    else:
        xpos += speedx

    #shoots bullets
    if shoot:
        bullets.append([xpos + 8,235])
        shoot = False

    for b in bullets:
        b[1] -= 24
        if b[1] < 65:
            bullets.remove(b)
        
    '''drawings'''
    #draw lots of stars
    for s in more_stars:
        pygame.draw.ellipse(screen,WHITE,s)

    #draw planets
    for p in planets:
        draw_planet(p[0],p[1],p[2])
        
    #draw sprites
    for s in sprites:
        screen.blit(s[2], (s[0],s[1]))

    #body of gameboy
    pygame.draw.rect(screen,GREY,[280,50,280,440])

    #black screen
    pygame.draw.rect(screen,BLACK,[300,70,240,180])
    
    #displays game
    if powered_on:
        game_on(xpos)
        
        #draw bullets
        for b in bullets:
            draw_bullet(b)
         
    #a and b buttons
    pygame.draw.circle(screen,MAGENTA,[520,340],20)
    pygame.draw.circle(screen,MAGENTA,[475,365],20)

    # d-pad
    pygame.draw.rect(screen,BLACK,[340,290,20,80])
    pygame.draw.rect(screen,BLACK,[310,320,80,20])
    if speedx > 0:
        pygame.draw.rect(screen,BLACKISH,[360,320,30,20])
    if speedx < 0:
        pygame.draw.rect(screen,BLACKISH,[310,320,30,20])
        

    #screen bezel
    pygame.draw.rect(screen,GREY2,[300,70,240,180],15)

    #start and select buttons
    pygame.draw.polygon(screen,GREY2,[[380,440],[410,430]],8)
    pygame.draw.polygon(screen,GREY2,[[415,440],[445,430]],8)

    #displays the instruction screen
    if show_instruction:
        width = SIZE[0]

        pygame.draw.rect(screen,BLACK, [0,0,800,600])
        header = BIG_FONT.render('Welcome to Gameboy Similuator 2011', True, WHITE)
        inst1 = SMALL_FONT.render('Press the SPACE bar to power on the game.',True, WHITE)
        inst2 = SMALL_FONT.render('Press the left and right arrows to move, and the up arrow to shoot.',True, WHITE)
        inst3 = SMALL_FONT.render('Press "z" to start music and "x" to play next song.',True, WHITE)
        inst4 = BIG_FONT.render('Press ENTER to begin.',True, WHITE)
        
        width_head = header.get_width()
        width1 = inst1.get_width()
        width2 = inst2.get_width()
        width3 = inst3.get_width()
        width4 = inst4.get_width()
        
        screen.blit(header, [width//2 - width_head//2,150])
        screen.blit(inst1, [width//2 - width1//2,300])
        screen.blit(inst2, [width//2 - width2//2,320])
        screen.blit(inst3, [width//2 - width3//2,340])
        screen.blit(inst4, [width//2 - width4//2,380])

    #display which song is playing
    song_header = SMALL_FONT.render(song[7:-4],True, WHITE)
    screen.blit(song_header, [0,580])

    #update
    pygame.display.flip()
    clock.tick(refresh_rate)

pygame.quit()
