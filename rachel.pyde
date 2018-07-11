def setup():
    size (800, 600)
    noStroke()
    x = 0
    while x < 800:
        y = 0
        while y < 600:
            if x % 200 == 0:
                fill (random (255), random (255), random (255))
            else:
                fill (0, 0, 0)
            rect(x, y, 100, 100)
            if y % 300 == 0:
                fill (255, 255, 255)
                rect (x, y, 100, 100 )
            y = y + 100
        x = x + 100
