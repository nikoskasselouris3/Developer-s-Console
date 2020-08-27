import turtle as t
import time
from tkinter import Tk,simpledialog, messagebox,Canvas
import webbrowser


wt = t.Turtle()
t.title('BELL Multiple Windows Manager 20')
wt.ht()
wt.write("MADE BY BELL",align='center',font=('Arial', 40, 'bold'))
time.sleep(1)
wt.clear()
time.sleep(1)
wt.write("Bell MWM 20-multiple windows without bugs.",align='center',font=('Arial', 20, 'bold'))
time.sleep(2)
wt.clear()
time.sleep(1)
answer = simpledialog.askstring('Password', 'Welcome,enter sd2 to the box.')
if answer== 'sd2':
    wt.write("Enjoy MWM!!!",align='center',font=('Arial', 20, 'bold'))
    time.sleep(1)
    wt.clear()
    wt.write("Press i for Instagram",align='center',font=('Arial', 20, 'bold'))
    time.sleep(1)
    wt.clear()
    wt.write("Press y for Youtube",align='center',font=('Arial', 20, 'bold'))
    time.sleep(1)
    wt.clear()
    wt.write("Press f for Facebook",align='center',font=('Arial', 20, 'bold'))
    time.sleep(1)
    wt.clear()
    wt.write("Press s for skysports",align='center',font=('Arial', 20, 'bold'))
    time.sleep(1)
    root = Tk()
    c = Canvas(root, width=400,height=400)
    c.configure(bg='cyan',highlightthickness=0)
    c.body_color = "purple"
    body  = c.create_oval(35, 20, 365, 350,outline=c.body_color, fill=c.body_color)
    eye_left = c.create_oval(130, 110, 160, 170, outline='black', fill='white')
    pupil_left = c.create_oval(140, 145, 150, 155, outline='black', fill='black')
    eye_left = c.create_oval(230, 110, 260, 170, outline='black', fill='white')
    pupil_left = c.create_oval(240, 145, 250, 155, outline='black', fill='black')    
    c.pack()
    root.title("Loopy")
    
    



def Instagram_function():
    webbrowser.open('https://www.instagram.com/')


def Youtube_function():
    webbrowser.open('https://www.youtube.com/?hl=en')
    

def Facebook_function():
    webbrowser.open('https://www.facebook.com/')


def skysports_function():
    webbrowser.open('https://www.skysports.com/')

t.onkey(Instagram_function, 'i')
t.onkey(Youtube_function, 'y')
t.onkey(Facebook_function, 'f')
t.onkey(skysports_function, 's')
t.listen()
t.mainloop()
