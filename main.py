from turtle import *
import random


##### FUNCTIONS AND CLASS DEFINITIONS ############
class Block(Turtle):
  pass
  # Constructor

  # delete() - responsible for hiding and removing the block from the list of blocks

  # strike() - handles a bullet hit, updates color and increments hit count



class Player(Turtle):
  pass
  # Constructor 
	
  # turn_right() - rotates the player right

  # turn_left() - rotates the player left
	
  # fire() - instantiates a Bullet object in the Player's bullet list if the Player has fewer than five active bullets
	


class Bullet(Turtle):
  pass
  # Constructor

  # move() - moves the bullet forward, reflects the bullet off the side of the playing area, deletes the bullet if it leaves the top of the playing area
	
  # delete() - hides the bullet object and removes itself from the Player's list of bullets

class Score(Turtle):
  pass
  # Constructor

  # clear_score() - clears the previous score before a new score is displayed

  # update_score() - updates the player's score and displays it on the screen.


# draw_border() - creates the playing area.	
def draw_border():
	p = Turtle()
	p.speed(0)
	p.ht()
	p.pu()
	p.width(10)
	p.color("white")
	p.goto(-110, 200)
	p.pendown()
	p.begin_fill()
	for i in range(2):
		p.forward(220)
		p.right(90)
		p.forward(400)
		p.right(90)
	p.end_fill()


####### PROGRAM #############
screen = Screen()
screen.title("Shooting Gallery")
screen.bgcolor("black")



screen.mainloop()
