import turtle
circle1 = [1,1,2]
circle2 = [2,4,5]
circle3 = [-1,-3,2]
circle4 = [5,2,1]
allCircles = [circle1,circle2,circle3,circle4]
left = 0
right = 0
top = 0
bot = 0




for circle in allCircles:
	if(circle[0]+circle[2]>right):
		right = circle[0]+circle[2]
	if(circle[0]-circle[2]<left):
		left = circle[0]-circle[2]
	if(circle[1]+circle[2]>top):
		top = circle[1]+circle[2]
	if(circle[1]-circle[2]<bot):
		bot = circle[1]-circle[2]


print '(',left,',',bot,'), (',left,',',top,'), (',right,',',top,'), (',right,',',bot,')' 



myTurtle = turtle.Turtle()
myTurtle.speed('fastest')

for circle in allCircles:
	myTurtle.penup()
	myTurtle.setposition(circle[0]*50,circle[1]*50-circle[2]*50)
	myTurtle.pendown()
	myTurtle.circle(circle[2]*50)	
myTurtle.penup()
myTurtle.setposition(0,0)
myTurtle.setposition(left*50,top*50)
myTurtle.pendown()
myTurtle.forward(abs(right-left)*50)
myTurtle.right(90)
myTurtle.forward(abs(top-bot)*50)
myTurtle.right(90)
myTurtle.forward(abs(right-left)*50)
myTurtle.right(90)
myTurtle.forward(abs(top-bot)*50)

turtle.getscreen()._root.mainloop()


