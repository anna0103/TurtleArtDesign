def ah(t,c,s):  #def ah function
    for x in range(10): #for loop
        t.forward(s) # move forward

def ha(t,c,size): #def ha function
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
    
