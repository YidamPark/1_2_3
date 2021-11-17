#   a123_apple_1.py
import turtle as trtl
import random as rand

#-----setup-----
apple_image = "apple.gif" # Store the file name of your shape

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.bgpic("background.gif")
wn.addshape(apple_image) # Make the screen aware of the new file

apple = trtl.Turtle()
drawer = trtl.Turtle()

#-----functions-----
# given a turtle, set that turtle to be shaped by the image file
def draw_apple(active_apple):
  active_apple.shape(apple_image)
  draw_white_A()
  wn.update()

# This function takes care of font and color.
def draw_an_A():
  drawer.color("blue")
  drawer.write("A", font=("Arial", 74, "bold")) 

def draw_white_A():
  drawer.penup()
  drawer.goto(apple.xcor(),100)
  drawer.color("white")
  drawer.write("A", font=("Arial", 74, "bold"))
  drawer.hideturtle()

def drop_apple():
  apple.penup()
  apple.goto(apple.xcor(),-150)
  drawer.hideturtle()


#-----function calls-----
draw_apple(apple)
wn.onkeypress(drop_apple(),"a")
wn.onkeypress(draw_an_A)
wn.listen()
wn.mainloop()
