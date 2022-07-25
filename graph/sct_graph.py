import pygame
import sys


pygame.init()

screenSize = (500, 500)
gameScreen = pygame.display.set_mode(screenSize)
white = (255,255,255)
clock = pygame.time.Clock()
font = pygame.font.SysFont('arial', 15, True, True)


def newScreen():
    gameScreen.fill(white)
    pygame.draw.line(gameScreen, black, [10, 250], [490,250])
    pygame.draw.line(gameScreen, black, [110, 350], [110,150])
    
    # 좌표 평면
    [exec(f'pygame.draw.line(gameScreen, black, [{i}, 10], [{i}, 490])') for i in range(210, 491, 10)] 
    [exec(f'pygame.draw.line(gameScreen, black, [210, {i}], [490, {i}])') for i in range(10, 491, 10)]


    pygame.draw.circle(gameScreen, black, seta, redius, 2) # redius : 70


def circumference_of_a_circle(coordinate=[]):
    global cnt
    if cnt < 1:
        coordinate[0] -= 1 # x
        y = (int((4900-(int(coordinate[0]-seta[0]))**2)**0.5))
        if y == 0:
            cnt += 1

        coordinate[1] = 250-y # y

    else:
        coordinate[0] += 1 # x
        y = (int((4900-(int(coordinate[0]-seta[0]))**2)**0.5))
        if y == 0:
            cnt -= 1

        coordinate[1] = 250+y # y
    return coordinate

def triangle():
    pygame.draw.line(gameScreen, red, seta, coordinate, 2)
    pygame.draw.line(gameScreen, red, [coordinate[0], 250], coordinate, 2)
    pygame.draw.line(gameScreen, red, seta, [coordinate[0], 250], 2)

# title
pygame.display.set_caption('Tangent graph')

black = (0,0,0)
blue = (0,0,255)
red = (255,0,0)

redius = 70
seta = [110, 250]

max_right = [seta[0]+70, seta[1]]
max_top = [seta[0], seta[1]-70]
max_left = [seta[0]-70, seta[1]]
max_bottom = [seta[0], seta[1]+70]

coordinate = max_right

# 좌표 평면
newScreen()

pygame.draw.circle(gameScreen, blue, max_right, 5) # dot

pygame.display.update()

cnt = 0

running =True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # circumference of a circle
    coordinate = circumference_of_a_circle(coordinate)
    newScreen()

    pygame.draw.circle(gameScreen, blue, coordinate, 3)
    text = font.render(f'({coordinate[0]}, {coordinate[1]})', True, black)
    gameScreen.blit(text, coordinate)

    # triangle
    triangle()

    pygame.display.flip()
    clock.tick(60)
        
pygame.quit()
sys.exit()