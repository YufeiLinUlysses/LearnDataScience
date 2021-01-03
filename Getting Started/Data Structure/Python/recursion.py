import turtle


def listSum(numList: "List[int]") -> int:
    if len(numList) == 1:
        return numList[0]
    return numList[0] + listSum(numList[1:])


def changeBase(num: int, base: int) -> str:
    baseStr = "0123456789ABCDEF"
    if num < base:
        return baseStr[num]
    return changeBase(num//base, base) + baseStr[num % base]


t = turtle.Turtle()


def drawSpiral(t, lineLen):
    if lineLen > 0:
        t.forward(lineLen)
        t.right(90)
        drawSpiral(t, lineLen - 5)


drawSpiral(t, 100)


def tree(branch_len):
    if branch_len > 5:
        t.forward(branch_len)
        t.right(20)
        tree(branch_len - 15)
        t.left(40)
        tree(branch_len - 15)
        t.right(20)
        t.backward(branch_len)


t.left(90)
t.penup()
t.backward(100)
t.pendown()
t.pencolor("green")
t.pensize(2)
tree(75)
t.hideturtle()


def drawTriangle(points, color):
    t.fillcolor(color)
    t.penup()
    t.goto(points['top'])
    t.pendown()
    t.begin_fill()
    t.goto(points['left'])
    t.goto(points['right'])
    t.goto(points['top'])
    t.end_fill()


def getMid(p1, p2):
    return ((p1[0]+p2[0])/2, (p1[1]+p2[1])/2)


def sierpinski(degree, points):
    colormap = ['blue', 'red', 'green', 'white', 'yellow', 'orange']
    drawTriangle(points, colormap[degree])
    if degree > 0:
        sierpinski(degree - 1,
                   {
                       'left': points['left'],
                       'top': getMid(points['left'], points['top']),
                       'right': getMid(points['left'], points['right'])
                   })
        sierpinski(degree - 1,
                   {
                       'left': getMid(points['left'], points['top']),
                       'top': points['top'],
                       'right': getMid(points['top'], points['right'])
                   })
        sierpinski(degree - 1,
                   {
                       'left': getMid(points['left'], points['right']),
                       'top': getMid(points['top'], points['right']),
                       'right': points['right']
                   })

points = {
    'left':(-200,-100),
    'top':(0,200),
    'right':(200,-100)
}
sierpinski(5,points)
turtle.done()