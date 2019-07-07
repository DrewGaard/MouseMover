import pynput
import time

mouse = pynput.mouse.Controller()

mouse.position = (10, 20)


while True:
    try:
        mouse.move(500, 1000)
        mouse.press(pynput.mouse.Button.right)
        mouse.release(pynput.mouse.Button.right)
        time.sleep(5)
        mouse.move(500, 0)
        mouse.press(pynput.mouse.Button.right)
        mouse.release(pynput.mouse.Button.right)
        time.sleep(5)
        mouse.position = (0,0)
    except KeyboardInterrupt:
        break


mouse.press(pynput.mouse.Button.right)
mouse.release(pynput.mouse.Button.right)

