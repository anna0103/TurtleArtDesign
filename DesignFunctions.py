def ah(t,c,s):
    for x in range(10):
        t.forward(s)

def ha(t,c,size):
    t.color(c)
    for x in range(10):
        t.circle(x)
        t.forward(size)
        t.right(50)

def polygon(t,dist,sides):
    angle=360/sides
    for times in range(sides):
        t.forward(dist)
        t.left(angle)
    
