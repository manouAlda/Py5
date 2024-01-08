#notre premier code
import py5

pos_x=0
marqueur=0

def setup():
    py5.size(480,120)

def draw():
    global pos_x
    global marqueur
    py5.background(120)
    py5.fill(250,200,200)
    py5.no_stroke()
    py5.ellipse(pos_x,60,50,50)

    if pos_x>py5.width :
        marqueur = -1
    elif  pos_x<0 :
        marqueur = 0

    if marqueur==0 :
        pos_x = pos_x +1
    elif marqueur==-1 :
        pos_x = pos_x -1


py5.run_sketch()