from tkinter import *
from random import uniform, randrange
from math import sin, cos, radians, pi


def rotate(origin, point, angle):
    ox, oy = origin
    px, py = point

    qx = ox + cos(angle) * (px - ox) - sin(angle) * (py - oy)
    qy = oy + sin(angle) * (px - ox) + cos(angle) * (py - oy)

    return qx, qy


def drawline():
    global win, width, height, t, l, canvas, total, intersect, n
    # Get the random coordinates of the lines origin and the angle its rotated
    for i in range(n):
        x = uniform(0, width)
        y = uniform(0, height)
        theta = radians(uniform(-90, 90))

        closest = 0  # X coordinate of the closest horizontal line
        for horizX in range(0, width, t):
            if abs(horizX - x) < abs(closest - x):
                closest = horizX

        # Calculate the rotated ends of the line
        x1, y1 = rotate((x, y), (x - l / 2, y), theta)
        x2, y2 = rotate((x, y), (x + l / 2, y), theta)

        # Draw the line to the canvas and colour it green if it touches a horizontal line
        if x1 <= closest <= x2:
            if show:
                canvas.create_line(x1, y1, x2, y2, fill="green", width=1)
            intersect += 1
        else:
            if show:
                canvas.create_line(x1, y1, x2, y2, fill="red", width=1)
        total += 1

    prob = intersect / total
    print("Pi ≈ ", end="")
    if intersect != 0:
        pie = 2 * l / (prob * t)

        print(str(pie))
    else:
        pie = None
        print("Need more lines")
    if show:
        win.after(100, drawline)
    else:
        return pie


def getYN(txt):
    while True:
        inp = input(txt).lower()
        if inp in ["y", "yes"]:
            return True
        elif inp in ["n", "no"]:
            return False



def main():
    global win, width, height, t, l, canvas, total, intersect, n, show
    show = getYN("Do you want a visual representation? (Y/N)")

    width, height = 600, 600
    t = 20  # Distance between horixontal lines
    l = 5  # Length of lines
    n = 1  # Number of lines dropped per frame

    if show:
        win = Tk()
        win.geometry(str(width) + "x" + str(height))
        win.title("Buffon's Needle")

        canvas = Canvas(win, width=width, height=height)
        canvas.pack()

        for i in range(0, width, t):
            canvas.create_line(i, 0, i, height, fill="black", width=1)

    total = 0
    intersect = 0
    drawline()

    if show:
        win.mainloop()
    else:
        best = 0
        while True:
            pie = drawline()
            if pie != None:
                if abs(pi - pie) < abs(pi - best):
                    best = pie
                print("Pi ≈ " + str(pie))
            else:
                print("Pi ≈ None")


if __name__ == "__main__":
    main()