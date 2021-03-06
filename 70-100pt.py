##########################################
#                                        #
#             Draw a house!              #
#                                        #
##########################################

# Use create_line(), create_rectangle() and create_oval() to make a 
# drawing of a house using the tKinter Canvas widget.

# 70pt: House outline (roof and the house)
# 80pt: Square windows and a door
# 90pt: A door handle plus a chimney!
# 100pt: Green grass on the ground and a red house!

# Minus 5pts if your code has no comments
# Minus 10pts if you only commit once to github

from Tkinter import *
root = Tk()

# Create the canvas widget
drawpad = Canvas(root, width=800,height=600, background='white')
drawpad.grid(row=0, column=1)

# Insert your code here to draw the house!

#Chimney code
chimney = drawpad.create_rectangle(370,300,400,500, fill='grey')
#House Body Code
house = drawpad.create_rectangle(100,600,400,400, fill='red')
#Roof Code
roof = drawpad.create_rectangle(100,350,400,400, fill='brown')
#Windows Code
window1 = drawpad.create_rectangle(110,500,150,550, fill='white')
window2 = drawpad.create_rectangle(110,430,150,480, fill='white')
window3 = drawpad.create_rectangle(330,430,370,480, fill='white')
window4 = drawpad.create_rectangle(330,500,370,550, fill='white')
#Door & Door Handle code
door = drawpad.create_rectangle(200,600,270,520, fill='tan')
doorhandle = drawpad.create_oval(250,570,260,560, fill='black')
#Grass code
grass = drawpad.create_rectangle(0,585,800,600, fill='green')

root.mainloop()