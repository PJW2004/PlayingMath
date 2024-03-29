import pygame
import time
import numpy as np
from multiprocessing import Pool
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

width, height = 400, 400
zoom = 0.3
# don't change zoom_factor, quite buggy, too lazy to fix
zoom_factor = 2
xAxis = 1 / zoom
yAxis = height / (width * zoom)
camX = -0.5
camY = 0
iterations = 100
iterations_factor = 1.4

# zoom in: left click
# zoom out: right click
# increase iteration: scroll up
# decrease iteration: scroll down

xOffset = (-xAxis / 2) + camX
yOffset = (-yAxis / 2) - camY
ratio = xAxis / width


def frac(x, y, rat, xOff, yOff, iter):
    a = (x * rat) + xOff
    b = (y * rat) + yOff
    ca = a
    cb = b
    n = 0
    # change lim condition to a * a + b * b < 4 for normal effect
    while a + b < 40 and n < iter:
        ai = a * a - b * b
        bi = 2 * a * b

        a = ai + ca
        b = bi + cb
        n += 1

    m = n / iter
    
    # m = np.sqrt(m)
    lin = int(255 * m) % 255
    sin = int(255 * (-np.cos(np.pi * m) + 1) / 2) % 255
    sqrt = int(255 * np.sqrt(m)) % 255
    sqr = int(255 * (m * m)) % 255
    r = sqr
    g = lin
    b = sin
    return r, g, b


def control(mouse, button):
    global xOffset, yOffset, ratio, iterations
    if button == 1:
        ratio /= zoom_factor
        dx = (mouse[0]) * ratio
        dy = (mouse[1]) * ratio
        xOffset += dx
        yOffset += dy
    elif button == 3:
        dx = (mouse[0]) * ratio
        dy = (mouse[1]) * ratio
        ratio *= zoom_factor
        xOffset -= dx
        yOffset -= dy
    elif button == 4:
        iterations = int(iterations * iterations_factor)
    elif button == 5:
        iterations = int(iterations / iterations_factor)
    main()


def process():
    t1 = time.perf_counter()
    win = (width, height)
    screen = pygame.display.set_mode(win)
    pix = []
    for x in range(width):
        for y in range(height):
            pix.append((x, y, ratio, xOffset, yOffset, iterations))

    p = Pool()
    pixels = p.starmap(frac, pix)
    p.close()
    p.join()

    # array = np.asarray(pixels)
    # reshaped_array = array.reshape(width, height, 3)
    # pygame.surfarray.blit_array(screen, reshaped_array)

    for x in range(height):
        for y in range(width):
            screen.set_at((y, x), pixels[y * height + x])

    t2 = time.perf_counter()
    print(t2 - t1)


def main():
    process()
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                control(pygame.mouse.get_pos(), event.button)
            pygame.display.update()


if __name__ == '__main__':
    main()