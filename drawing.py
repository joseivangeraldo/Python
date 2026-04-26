#If you need a Virtual Display
#If you must run code that requires a display (e.g., for automated testing), you can simulate one using Xvfb (X Virtual Framebuffer): 
#Install Xvfb: sudo apt-get install xvfb
#Run your script with it: xvfb-run python drawing.py
import turtle

# Create the screen object
window = turtle.Screen()
window.setup(width=600, height=400)
window.bgcolor("white")
window.title("My Drawing")

# Create a turtle to draw on the screen
my_turtle = turtle.Turtle()
my_turtle.forward(100)

# Close the window when clicked
window.exitonclick()


