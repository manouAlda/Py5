import py5

pos_x=27
pos_y=60
marqueur_y=1
marqueur_x=1

def setup():
    py5.size(480,400)

def draw():
    global pos_x
    global pos_y
    global marqueur_y
    global marqueur_x

    py5.background(120)
    py5.fill(250,200,200)
    py5.no_stroke()
    py5.ellipse(pos_x,pos_y,50,50)

    if pos_y+25>=py5.height or pos_y-25<=0:
        marqueur_y = -marqueur_y

    if pos_x+25>=py5.width or pos_x-25<=0:
        marqueur_x = -marqueur_x

    pos_y = pos_y + marqueur_y
    pos_x = pos_x + marqueur_x

py5.run_sketch()