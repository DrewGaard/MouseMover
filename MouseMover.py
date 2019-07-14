import pynput
import time
from Tkinter import *
import keyboard

master = Tk()

if keyboard.is_pressed('q'):
    print("Hello!")

notpressed = True


def callback():
    while notpressed == True:
            print "click!"
            if keyboard.is_pressed('space'):
                notpressed == False

def mouseMover():
    mouse = pynput.mouse.Controller()

    mouse.position = (10, 20)


    while True:
        try:
            mouse.move(500, 1000)
            mouse.press(pynput.mouse.Button.right)
            mouse.release(pynput.mouse.Button.right)
            time.sleep(5)
            if keyboard.is_pressed('q'):  # if key 'q' is pressed 
                print('You Pressed A Key!')
                break  # finishing the loop
            mouse.move(500, 0)
            mouse.press(pynput.mouse.Button.right)
            mouse.release(pynput.mouse.Button.right)
            if keyboard.is_pressed('q'):  # if key 'q' is pressed 
                print('You Pressed A Key!')
                break  # finishing the loop
            time.sleep(5)
            mouse.position = (0,0)
        except keyboard.is_pressed('q'):
            print('You Pressed A Key Two!')
            break


    mouse.press(pynput.mouse.Button.right)
    mouse.release(pynput.mouse.Button.right)

    

b = Button(master, text="OK", command=mouseMover)
b.pack()

mainloop()


