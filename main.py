import pygame
import math

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)

width = 1920
height = 1080

x_start, y_start = 0, 0
x_seperator = 10
y_seperator = 20

rows = height // y_seperator
columns = width // x_seperator
screen_size = rows * columns

x_offset = columns / 2
y_offset = rows / 2

A, B = 0, 0
theta_spacing = 10
phi_spacing = 1

chars = ".,-~:;=!*#$@"

screen = pygame.display.set_mode((width, height))
display_surface = pygame.display.set_mode((width, height))
pygame.display.set_caption('Donut')
font = pygame.font.SysFont('Arial', 18, bold=True)

def text_display(letter, xstart, ystart):
    text = font.render(str(letter), True, white)
    display_surface.blit(text, (xstart, ystart))

run = True
clock = pygame.time.Clock()

while run:
    screen.fill(black)
    z = [0] * screen_size
    b = [' '] * screen_size

    # Calculate donut with current A and B angles
    for i in range(0, 628, theta_spacing):
        for j in range(0, 628, phi_spacing):
            c = math.sin(i)
            d = math.cos(j)
            e = math.sin(A)
            f = math.sin(j)
            g = math.cos(A)
            h = d + 2
            D = 1 / (c * h * e + f * g + 5)
            l = math.cos(i)
            m = math.cos(B)
            n = math.sin(B)
            t = c * h * g - f * e
            x = int(x_offset + 40 * D * (l * h * m - t * n))
            y = int(y_offset + 20 * D * (l * h * n + t * m))
            o = int(x + columns * y)
            N = int(8 * ((f * e - c * d * g) * m - c * d * e - f * g - l * d * n))
            
            if 0 < y < rows and 0 < x < columns and D > z[o]:
                z[o] = D
                b[o] = chars[N if N > 0 else 0]

    # Display the donut
    x_start, y_start = 0, 0
    for i in range(len(b)):
        if i > 0 and i % columns == 0:
            y_start += y_seperator
            x_start = 0
        text_display(b[i], x_start, y_start)
        x_start += x_seperator

    pygame.display.update()

    
    A += 0.02  # Increased from 0.000002
    B += 0.01  # Increased from 0.000001

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    # Control frame rate
    clock.tick(60)

pygame.quit()