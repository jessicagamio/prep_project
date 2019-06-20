import turtle
import time 
import random

##########WINDOW SETUP############

win=turtle.Screen()
win.setup(width=800,height=800,startx=None,starty=None)
win.bgcolor("light blue")
win.title("Snoopy to the Rescue!")

#########GAME FUNCTIONS############

def hide_all_turtle():
	"""Hides all turtles and clears stamps"""
	snoopy.hideturtle()
	trivia_question.hideturtle()
	clouds.hideturtle()
	clouds.clearstamps(None)
	trivia_question.clearstamps(None)
	woodstock.hideturtle()
	start_text.hideturtle()

def greet():
	"""Greet user and set premise for game"""
	hide_all_turtle()
	start_text.write("The Flying Ace to the Rescue!!\n\nWoodstock's in trouble!\n\nGuide Snoopy through the maze of clouds to reach his friend\n\nHit the Space Bar to continue or the Q key to quit.", align="center",font=("Arial",12,"normal"))
	controller()
	
def instruct():
	"""gives instruction for gameplay"""
	hide_all_turtle()
	start_text.clear()
	start_text.write("Navigate Snoopy through the maze using the Arrow Keys in your keyboard\n\nAnswer Trivia Questions along the way, 2 wrong answers in a row and you lose the game\n\nHit the Q key any time to quit the game\n\n Hit the S key to Start/Restart the game.", align="center",font=("Arial",12,"normal"))
	controller()
	
def start():
	"""start the game"""
	start_text.clear()
	maze_generator()
	snoopy.showturtle()
	woodstock.showturtle()
	controller()

def quit():
	"""quit game"""
	win.clearscreen()
	start_text.write("Goodbye!", align="center",font=("Arial",12,"normal"))
	time.sleep(2)
	win.bye()	

def win_game():
	"""user wins"""
	win.clearscreen()
	start_text.write("You Finished!!",align="center",font=("Arial",18,"bold"))
	time.sleep(5)
	win.bye()
	
def loser():
	"""lose game"""
	hide_all_turtle()
	start_text.write("Sorry try again!\n\nHit S key to start a new game or Q to quit", align="center",font=("Arial",12,"normal"))
	controller()
		
def trivia():
	"""trivia questions. question[0]=Question and question[1]=Answer"""
	question_pool={"question_1":("What year did Peanuts debut as a comic strip?\n A: 1949\n B: 1950\n C: 1961",'b'),
	"question_2":("Snoopy is a..\n A: Schnauzer\n B: Retriever\n C: Beagle","c"),
	"question_3":("The creater of Peanuts is\n A: Charles E. Brown\n B: Charles B. Schulz\n C: Charles M. Schulz", "c"),
	"question_4":("Joe Cool is a ..\n A: Fighter Pilot\n B: Singer\n C: College Student","c"),
	"question_5":("The name of Snoopy's best friend is ..\n A: Woodstock\n B: Yellow Bird\n C: Charly Brown","a"),
	"question_6":("Snoopy hates ..\n A: Leashes\n B: Pats on the head\n C: Whistles","b"),
	"question_7":("What is Lucy's last name? \n A: Van Helsing\n B: Van Husten\n C: Van Pelt","c"),
	"question_8":("What's the name of Snoopy's brother? \n A: Spike\n B: Spot\n C: Sparky","a"),
	"question_9":("Charlie Brown's best friend was ..\n A: Lucy\n B: Linus\n C: Charlie Brown","b")}

	keys=[]
	selected=""
	for questions in question_pool:
		keys.append(questions)
		
	selected=random.choice(keys)
	question=question_pool[selected]
	
	count=0
	
	while True:
		answer= win.textinput("Trivia Question",question[0])	
		controller()
		if answer.lower()==question[1]:
			break
		if answer==None:
			count+=1
			break
		if answer.lower()!=question[1]:
			count+=1
		if count>1:
			loser()
			break
	
	return "pass"

	
def controller():
	"""set controller function for game"""
	win.listen()
	win.onkey(snoopy.up,'Up')
	win.onkey(snoopy.down,'Down')
	win.onkey(snoopy.left,'Left')
	win.onkey(snoopy.right,'Right')
	win.onkey(quit,'q')
	win.onkey(start,'s')
	win.onkey(instruct,'space')

	
##########PLAYER CLASS SETUP##############

turtle.register_shape("snoopy.gif")
turtle.register_shape("woodstock_2.gif")

class Player(turtle.Turtle):
	def __init__(self):
		turtle.Turtle.__init__(self)
		self.penup()
		self.speed(0)
		
	def up(self):
		"""moves player up maze by 24 pixels"""
		if (self.xcor(),self.ycor()+24) not in barriers and (self.xcor(),self.ycor()+24)not in winner:
			self.goto(self.xcor(),self.ycor()+24)
		if (self.xcor(),self.ycor()) in trivia_list:
			if trivia()=="pass":
				if (self.xcor(),self.ycor()+24) not in barriers and (self.xcor(),self.ycor()+24)not in winner:
					self.goto(self.xcor(),self.ycor()+24)				
		if (self.xcor(),self.ycor()+24) in winner:
			self.goto(self.xcor(),self.ycor()+24)
			win_game()
			
	def down(self):
		"""moves player down maze by 24 pixels"""
		if (self.xcor(),self.ycor()-24) not in barriers and (self.xcor(),self.ycor()-24) not in winner:
			self.goto(self.xcor(),self.ycor()-24)
		if (self.xcor(),self.ycor()) in trivia_list:
			if trivia()=="pass":
				if (self.xcor(),self.ycor()-24) not in barriers and (self.xcor(),self.ycor()-24) not in winner:
					self.goto(self.xcor(),self.ycor()-24)
		if (self.xcor(),self.ycor()-24) in winner:
			self.goto(self.xcor(),self.ycor()-24)
			win_game()
			
	def left(self):
		"""moves play left by 24 pixels"""
		if (self.xcor()-24,self.ycor()) not in barriers and (self.xcor()-24,self.ycor()) not in winner:
			self.goto(self.xcor()-24,self.ycor())
		if (self.xcor(),self.ycor())in trivia_list:
			if trivia()=="pass":
				if (self.xcor()-24,self.ycor()) not in barriers and (self.xcor()-24,self.ycor()) not in winner:
					self.goto(self.xcor()-24,self.ycor())				
		if (self.xcor()-24,self.ycor())in winner:
			self.goto(self.xcor()-24,self.ycor())
			win_game()
			
	def right(self):
		"""moves player right by 24 pixels"""
		if (self.xcor()+24,self.ycor()) not in barriers and (self.xcor()+24,self.ycor()) not in winner:
			self.goto(self.xcor()+24,self.ycor())
		if (self.xcor(),self.ycor())in trivia_list:
			if trivia()=="pass":
				if (self.xcor()+24,self.ycor()) not in barriers and (self.xcor()+24,self.ycor()) not in winner:
					self.goto(self.xcor()+24,self.ycor())				
		if (self.xcor()+24,self.ycor())in winner:
			self.goto(self.xcor()+24,self.ycor())
			win_game()		


#########MAZE CLASS SETUP AND FUNCTION######

turtle.register_shape("clouds.gif")
turtle.register_shape("trivia.gif")
		
			
class Maze(turtle.Turtle):
	"""sets up Maze characterstics"""
	def __init__(self):
		turtle.Turtle.__init__(self)
		self.penup()
		self.speed(0)
	

def maze_generator():
	"""generates maze for game and calculates all,winner,trivia,barriers coordinate lists
	for player functionality in maze"""

	maze=[
			'XXXXXXXXXXXXXXXXXXXXXXXXX',
			'S                       X',
			'XXXXXXXXXXXX XXXXXXXXXX X',
			'X                       X',
			'XXXXXXTXXXXXXXXXXXXXXXXXX',
			'X                       X',
			'XXXXXXXXXXXXTXXXXXXXXXXXX',
			'X                       X',
			'XXXXXXXXXXXXXXXXXXX XXXXX',
			'X                       X',
			'XXXXXXXXX XXXXXXXXX XXXXX',
			'X                       X',
			'XXXXXXXXXTXXXXXXXXX XXXXX',
			'X                     X F',
			'XXXXXXXXXXX XXXXXXXXXXX X',
			'X                   X   X',
			'XXXXXXX XXXXXXXXXXXXX XXX',
			'X                 X     X',
			'XXXX XXXXXXXXXXXXXXTXXXXX',
			'X                 X     X',
			'XXXXTXXXXXXXXXXXXXX XXXXX',
			'X                       X',
			'XXXXXXXXXXXXXXXX XXXXXXXX',
			'X                       X',
			'XXXXXXXXXXXXXXXXXXXXXXXXX',
	     ]
		 
		 
		 
	x_col=-288
	y_row=288
	
	for row in maze:#collects coord. for snoopy, woodstock, walls(clouds), winner, all, barrier,and trivia_questions.
		for col in row:
			all.append((x_col,y_row))
			if col == 'X':
				clouds.goto((x_col,y_row))
				clouds.stamp()
				barriers.append((x_col,y_row))
			elif col == 'S':
				snoopy.goto(x_col,y_row)
				starter.append((x_col,y_row))
			elif col == 'T':
				trivia_question.goto(x_col,y_row)
				trivia_question.stamp()
				trivia_list.append((x_col,y_row))
			elif col == 'F':
				winner.append((x_col,y_row))
				woodstock.goto(x_col+48,y_row)
			x_col=x_col+24
		y_row=y_row-24
		x_col=-288
	
	for unit in all:#appends outer extents of maze to keep player inside maze.		
		if -288 in unit or 288 in unit:
			x,y=unit 
			if x==288:
				barriers.append((x+24,y))
			elif x==-288:
				barriers.append((x-24,y))
			elif y==288:
				barriers.append((x,y+24))
			elif y==-288:
				barriers.append((x,y-24))
					

#############add lists############		
starter=[] #contains starting coordinates
barriers=[] #contains barriers coordinates
trivia_list=[]	#contains trivia coordinates		
winner=[] #contains winning coordinate
all=[] #contains all coordinates in grid				
	

########Set up Turtles #######


start_text=turtle.Turtle()#window text
start_text.hideturtle()

snoopy=Player()#snoopy player
snoopy.hideturtle()
snoopy.shape("snoopy.gif")

woodstock=Player()#woodstock player
woodstock.hideturtle()
woodstock.shape("woodstock_2.gif")

clouds=Maze() # walls
clouds.hideturtle()
clouds.shape("clouds.gif")

trivia_question=Maze()#trivia questions
trivia_question.hideturtle()
trivia_question.shape("trivia.gif")

###### PLAY #########

greet()	
		
win.mainloop()
