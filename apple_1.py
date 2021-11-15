#   a123_apple_1.py
import turtle as trtl

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
  wn.update()

# This function takes care of font and color.
def draw_an_A():
  drawer.color("blue")
  drawer.write("A", font=("Arial", 74, "bold")) 

def drop_apple():
  apple.penup()
  apple.goto(apple.xcor(),-200)
  



#-----function calls-----
draw_apple(apple)
draw_an_A()
# This call to the onkeypress function sets draw_an_A as the function
# that will be called when the "a" key is pressed.
wn.onkeypress(drop_apple(), "a")

wn.listen()


wn.mainloop()
