import turtle

def draw_square():
    window=turtle.Screen()
    window.bgcolor('blue')

    fei=turtle.Turtle()
    fei.speed(100)
    fei.shape('turtle')
    fei.color('white')
    for e in range(0,60):
        fei.left(6)
        for i in range(0,5):
            fei.forward(100)
            fei.left(60)

draw_square()
