import turtle

# Configurações iniciais
t = turtle.Turtle()
t.speed(2)  # Velocidade do desenho

# Desenhar a base da casa
t.penup()
t.goto(-100, -100)
t.pendown()
t.begin_fill()
t.color("yellow")
for _ in range(4):
    t.forward(200)
    t.left(90)
t.end_fill()

# Desenhar o telhado
t.penup()
t.goto(-100, 100)
t.pendown()
t.begin_fill()
t.color("red")
t.goto(0, 200)
t.goto(100, 100)
t.goto(-100, 100)
t.end_fill()

# Desenhar a porta
t.penup()
t.goto(-30, -100)
t.pendown()
t.begin_fill()
t.color("blue")
for _ in range(2):
    t.forward(60)
    t.left(90)
    t.forward(100)
    t.left(90)
t.end_fill()

# Desenhar a janela
t.penup()
t.goto(-70, 0)
t.pendown()
t.begin_fill()
t.color("blue")
for _ in range(4):
    t.forward(40)
    t.left(90)
t.end_fill()

# Finalizar
t.hideturtle()
turtle.done()
