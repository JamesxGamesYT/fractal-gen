import turtle
import math

def outverge(size=40, direction="forward", angle=3, handedness="left", color="orange", bgcolor="black"):
    x = size
    for i in range(0, 1000000):
        if direction == "forward":
            turtle.forward(x)
        elif direction == "backward":
            turtle.backward(x)
        else:
            raise Exception("Incorrect Arguments")
        
        turtle.left(angle)
        x = math.log(i+2, math.e)
    




outverge(color="blue")