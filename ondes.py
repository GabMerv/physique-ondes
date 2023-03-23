from math import *
import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.animation import FuncAnimation
from matplotlib import style
import matplotlib.animation as animation

global phase
phase = 0

def change(nouvelle_valeur):
   global phase
   phase = float(nouvelle_valeur)

def f(x):
   return sin(2*pi*x)

def g(x):
   global phase
   return sin(2*pi*x+phase)

def h(x):
   return f(x) + g(x)

def update_graph(dt):
   x = [i*0.01 for i in range(200)]
   y1 = [f(u) for u in x]
   y2 = [g(u) for u in x]
   y3 = [h(u) for u in x]
   ax1.clear()
   ax1.set_ylim(-2,2, auto=False)
   ax1.set_xlabel("temps")
   ax1.set_ylabel("signal")
   ax1.set_title("Somme de deux signaux sinusoïdaux périodiques synchrones déphasés")
   l1 = ax1.plot(x, y1, color="b", label="Signal 1")
   l2 = ax1.plot(x, y2, color="g", label="Signal 2")
   l3 = ax1.plot(x, y3, color="r", label="Signal 1 + Signal 2")
   ax1.legend()

app = tk.Tk()
style.use('ggplot')
fig = Figure(figsize=(10,10), dpi=112)
ax1 = fig.add_subplot(211)
graph = FigureCanvasTkAgg(fig, master=app)
canvas = graph.get_tk_widget()
canvas.grid(row=0, column=0)
curseur = tk.Scale(app, orient='horizontal', from_=0, to=2*pi, resolution=0.1, tickinterval=pi/4, length=350, label="Phase (radian)", command=change)
curseur.grid(row=0, column=1)
ani = animation.FuncAnimation(fig, update_graph, interval=200)
app.mainloop()