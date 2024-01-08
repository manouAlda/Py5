import py5
import random

img = 0
img_bird = 0
pos_x = 75
pos_y = 160
rayon = 75
vitesse_bird = 3
vitesse_tube = 1
obs_x = []
height_up = []
height_down = []
score = 0


def setup():
    global img, img_bird, obs_x, height_up, height_down, score
    py5.size(680, 400)
    img = py5.load_image("bg.jpg")
    img_bird = py5.load_image("bird.png")
    create_obstacles()

def key_pressed():
    global pos_y, vitesse_bird
    if py5.key == py5.CODED:
        if py5.key_code == py5.UP:
            vitesse_bird = -3
        else:
            vitesse_bird = 3
    elif py5.key == " ":
        vitesse_bird = -3
    elif py5.key == "p":
        py5.text_size(50)
        py5.fill(0, 102, 153)
        py5.text("Pause", 200, py5.height / 2)
        py5.no_loop()
    elif py5.key == py5.ENTER:
        py5.loop()


def key_released():
    global vitesse_bird
    if py5.key == " " or py5.key == py5.CODED:
        vitesse_bird = 3

def game_over():
    global pos_y
    #py5.background(255, 144, 0)
    py5.text_size(50)
    py5.fill(0, 102, 153)
    py5.text("GAME OVER", 200, py5.height / 2)
    py5.no_loop()

def coordonate ():
    global obs_x, height_up, height_down
    i=0
    while i < 3:
        distance = random.randint(200, 300)
        a = 680 + distance * i
        b = random.randint(50, 300)
        c = random.randint(100, 350)

        if b < c and c - b > rayon :
            obs_x.append(a)
            height_up.append(b)
            height_down.append(c)
            i += 1

def create_obstacles():
    global obs_x, height_up, height_down, score
    coordonate()

def display_score():
    py5.fill(0,255,0)
    py5.text_size(32)
    py5.text("Score: "+str(score), 10,30)

def display():
    global obs_x, height_up, height_down, score, pos_x, pos_y
    for i in range(3):

        py5.rect(obs_x[i], 0, 55, height_up[i], 0, 0, 18, 18)
        py5.rect(obs_x[i], height_down[i], 55, py5.height, 18, 18, 0, 0)
        obs_x[i] = obs_x[i] - vitesse_tube

        ## Gestion score
        if    height_up[i] <= pos_y <= height_down[i] :
            if obs_x[i] == pos_x:
                print("LEARN")
                score = score + 1
            elif vitesse_tube%2==0 and obs_x[i] == pos_x+1 :
                print("IT")
                score = score + 1
        ## Gestion collision
        if  obs_x[i]-55 == pos_x : 
            if  pos_y + 8 <= height_up[i] or pos_y + 50 >= height_down[i]: 
                print("Game over 2")
                game_over()
        if obs_x[i]-40 <= pos_x <= obs_x[i]+20 :
            if pos_y + 8 <= height_up[i] or pos_y + 53 >= height_down[i] :
                game_over()
                print("Game over 1")
        ## Gestion obstacles
        j=0
        if obs_x[i] + 55 < 0:
            obs_x[i] = 680  
            a = random.randint(50, 300)
            b = random.randint(100, 350)
            if a < b and a - b > rayon :
                height_up[i] = a
                height_down[i] = b
            else :
                height_up[i] = random.randint(50, 200)
                height_down[i] = random.randint(270, 350)
                     
def game():
    global pos_y, vitesse_tube,vitesse_bird
    if pos_y + 55 >= py5.height or pos_y + 10<= 0:
        print("Game over 3")
        game_over()
    if score  == 10 and score != 0:
        vitesse_tube = vitesse_tube + 1
    if vitesse_tube >= 5 and vitesse_bird%5==0 :
        vitesse_bird = vitesse_bird + 1

def draw():
    global pos_y, vitesse_bird, img, img_bird
    py5.image(img, 0, 0, py5.width, py5.height)
    py5.fill(255, 0, 0)
    py5.no_stroke()
    py5.image(img_bird, pos_x, pos_y, rayon, rayon)
    pos_y = pos_y + vitesse_bird
    display()
    game()
    display_score()

py5.run_sketch()
