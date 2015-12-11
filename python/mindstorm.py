import turtle

def draw_square(aTurtle):
	for i in range(1, 5):
		aTurtle.forward(150)
		aTurtle.right(90)	

def draw_art():
	window = turtle.Screen()
	window.bgcolor("red")
	

	brad = turtle.Turtle()
	brad.color("yellow")
	brad.shape("turtle")
	brad.speed("fast")

	for i in range(1, 10):
		draw_square(brad)
		brad.right(36)

	window.exitonclick()

draw_art()