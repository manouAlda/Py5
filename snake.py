import py5
import random

width_snake = 20
pos_x = 100
pos_y = 100
x = 15
y=0
position = []

number = 3

desac_up = 0
desac_down = 0
desac_left = 0
desac_right = 0

food_a = 0
food_b = 0

score = 0
game_over=0

def setup():
    py5.size(600,500)
    pos_food()
    py5.frame_rate(8)

def key_pressed():
    global pos_x, pos_y, y, x, desac_up, desac_down,desac_left, desac_right, mouth_x, mouth_y, game_over, score
    x = 0
    y = 0

    if py5.key == py5.CODED:
        if py5.key_code == py5.UP:
            desac_down = -1
            desac_left = 0
            desac_right = 0
            if desac_up == 2 :
                y = 15
            else:
                y = -15

        elif py5.key_code == py5.DOWN:
            desac_up = 2
            desac_left = 0
            desac_right = 0
            if desac_down == -1:
                y = -15
            else : 
                y = 15

        elif py5.key_code == py5.LEFT:
            desac_up=0
            desac_down = 0
            desac_right = -1
            if desac_left ==  1:
                x=15
            else:
                x = -15

        elif py5.key_code == py5.RIGHT:
            desac_up=0
            desac_down = 0
            desac_left = 1
            if desac_right == -1:
                x = -15
            else:
                x =  15
    elif py5.key == py5.ENTER and game_over==1:
        pos_x = 100
        pos_y = 100
        x = 15
        y=0
        score = 0
        game_over=0
        py5.loop()

def over():
    global game_over
    py5.text_size(50)
    py5.fill(0, 102, 153)
    py5.text("GAME OVER", 200, py5.height / 2)
    game_over=1
    py5.no_loop()

def game():
    global pos_y, pos_x, position
    if pos_y + (width_snake)>= py5.height or pos_y <= 0 or pos_x<= 0 or pos_x+(width_snake)>=py5.width :
        over()

def snake():
    global pos_x,pos_y

    py5.fill(255,255,0)
    py5.rect(pos_x,pos_y,20,20,18,18,18,18)
    py5.ellipse(pos_x+13,pos_y+16,3,3)
    py5.ellipse(pos_x+13,pos_y+13,3,3)

    position.append((pos_x, pos_y))

def tail():
    global width_snake, pos_y, pos_x, tmp
    global position

    py5.fill(255,0,0)

    last_x = 0
    last_y = 0
    if len(position) >= 2 :

        for i in range(2, number + 1):
            if len(position) >= i:
                last_p = position[-i]
                last_x = last_p[0]
                last_y = last_p[1]

                if last_x == pos_x and last_y == pos_y:
                    if i<3:
                        py5.rect(pos_x, pos_y+width_snake, 20,20,18,18,18,18)
                        py5.rect(pos_x, pos_y+(width_snake*2), 20,20,18,18,18,18)
                    else:
                        over()
                else :
                    py5.rect(last_x, last_y,20,20,18,18,18,18) 
                
def pos_food():
    global food_a, food_b
    food_a = random.randint(10,py5.width-7)
    food_b = random.randint(10,py5.height-7)

def food():
    global food_a, food_b
    py5.fill(0,255,0) 
    py5.ellipse(food_a,food_b,10,10)

def eat():
    global food_a, food_b,mouth_x, mouth_y, number, score

    py5.fill(255,0,255)
    
    if food_a-20 <= pos_x <= food_a+20 and food_b-20<= pos_y <= food_b+20:
        pos_food()
        food()
        number = number + 1
        score = score + 1

def print_score():
    global score
    py5.fill(0,255,255)
    py5.text_size(32)
    py5.text("Score: "+str(score), 10,30)

def draw():
    global pos_y,pos_x,x,y
    py5.background(125)

    pos_x = pos_x + x
    pos_y = pos_y + y

    game()

    food()
    snake()
    tail()
    eat()
    print_score()

py5.run_sketch()
