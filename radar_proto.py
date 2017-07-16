import Tkinter as tk
import random
from math import sin, cos,pi,radians,degrees


class Point:
    """ Point class represents and manipulates x,y coords. """

    def __init__(self, x=0, y=0):
        """ Create a new point at x, y """
        self.x = x
        self.y = y

counter = 0
radius = 100
step = 5

center = Point(200,100)
def counter_label(label, canvas):
  def count():
    global counter
    counter += step

    # get measurmenet
    distance = get_distance()
    
    label.config(text=str(counter%360)+"  " + str(counter/360))
    label.after(1000, count)
    print str(counter%360)+" " + str(distance)
    canvas.create_line(center.x, center.y, center.x+radius*sin(radians(counter%360)), center.y+radius*cos(radians(counter%360)), fill="#476042", width=3)
    canvas.create_line(center.x, center.y, center.x+distance*sin(radians(counter%360)), center.y+distance*cos(radians(counter%360)), fill="yellow",width=3)
    
  count()


def get_distance():
  distance = random.uniform(1, radius)
  return distance

 
root = tk.Tk()
root.title("Counting Seconds")
label = tk.Label(root, fg="green")
label.pack()
canvas = tk.Canvas(root)
canvas.pack(fill=tk.BOTH, expand=1)
counter_label(label, canvas)
button = tk.Button(root, text='Stop', width=25, command=root.destroy)
button.pack()

root.mainloop()
