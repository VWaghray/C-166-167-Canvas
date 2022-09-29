from tkinter import *
from PIL import Image, ImageTk
from PIL import *

root = Tk()

root.geometry("600x600")
root.title("Canvas")

cl = Label(root, text="Enter a Colour :")
cl.place(relx = 0.6, rely = 0.9, anchor = CENTER)

i_box = Entry(root)
i_box.insert(0, "black")
i_box.place(relx = 0.8, rely = 0.9, anchor = CENTER)

canvas = Canvas(root, width = 590, height = 510 , bg = "beige", highlightbackground= "gold2")
canvas.pack()

img = ImageTk.PhotoImage(Image.open ("start_point1.png"))
my_image =canvas.create_image(550,50, image = img)

direction = ""

oldx = 550
oldy = 50
newx = 550
newy = 50

def right_dir(event):
    global oldx
    global oldy
    global newx
    global newy
    oldx = newx
    oldy = newy
    newx = newx +5
    direction = "right"
    draw(direction, oldx,oldy,newx,newy)
    
def left_dir(event):
    global oldx
    global oldy
    global newx
    global newy
    oldx = newx
    oldy = newy
    newx = newx -5
    direction = "left"
    draw(direction, oldx,oldy,newx,newy)
    
def up_dir(event):
    global oldx
    global oldy
    global newx
    global newy
    oldx = newx
    oldy = newy
    newy = newy - 5
    direction = "up"
    draw(direction, oldx,oldy,newx,newy)
    
def down_dir(event):
    global oldx
    global oldy
    global newx
    global newy
    oldx = newx
    oldy = newy
    newy = newy +5
    direction = "down"
    draw(direction, oldx,oldy,newx,newy)

def draw( direction,oldx,oldy, newx, newy):
    fill_colour = i_box.get()
    if(direction == "right"):
        right_line = canvas.create_line(oldx, oldy, newx, newy, width = 5, fill = fill_colour)
    if(direction == "left"):
        left_line = canvas.create_line(oldx, oldy, newx, newy, width = 5, fill = fill_colour)
    if(direction == "up"):
        up_line = canvas.create_line(oldx, oldy, newx, newy, width = 5, fill = fill_colour)
    if(direction == "down"):
        down_line = canvas.create_line(oldx, oldy, newx, newy, width = 5, fill = fill_colour)
        

    


root.bind("<Right>", right_dir)
root.bind("<Left>", left_dir)
root.bind("<Up>", up_dir)
root.bind("<Down>", down_dir)



root.mainloop()