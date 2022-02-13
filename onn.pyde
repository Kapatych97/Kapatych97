

a = 0
b = 0
def setup():
    size(800,800)
    noStroke()
def draw():
    global x
    y = 0
    x = 0
    while x <  height:
        fill(random(100,250), random(100,250), random(100,250))
        ellipse(x + a,y + b,30,30)
        x = x + 30
        y = y + 30
    a-= 1
    b+= 1
