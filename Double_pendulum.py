import numpy as np
import pygame
import matplotlib.pyplot as plt


class Pendulum:

    def __init__(self):

        self.colour1 = (0, 0, 0)
        self.colour2 = (255, 0, 0)
        self.angle1 = float(input("Angle1:"))
        self.angle2 = float(input("Angle2:"))
        self.mass1 = float(input("Mass1:"))
        self.mass2 = float(input("Mass2:"))
        self.a_velocity1 = 0
        self.a_velocity2 = 0
        self.a_acceleration1 = 0
        self.a_acceleration2 = 0
        self.length1 = float(input("Length1:"))
        self.length2 = float(input("Length2:"))
        self.x_coordinates = []
        self.y_coordinates = []

    def draw(self):

        x1 = width / 2 + self.length1 * 100 * np.sin(self.angle1)
        y1 = height / 2 + self.length1 * 100 * np.cos(self.angle1)
        x2 = self.length2 * 100 * np.sin(self.angle2)
        y2 = self.length2 * 100 * np.cos(self.angle2)

        pygame.draw.line(screen, self.colour1, (width / 2, height / 2), (x1, y1), 5)

        pygame.draw.line(screen, self.colour1, (x1, y1), (x1 + x2, y1 + y2), 5)

        pygame.draw.circle(screen, self.colour2, (x1, y1), 20)

        pygame.draw.circle(screen, self.colour2, (x1 + x2, y1 + y2), 20)

        self.x_coordinates.append(x1 + x2)
        self.y_coordinates.append(-y1 - y2)

    def move(self):

        g = 9.82
        dt = 0.0009

        term1 = -g * np.sin(self.angle1) * ((2 * self.mass1) + self.mass2)
        term2 = -self.mass2 * g * np.sin(self.angle1 - (2 * self.angle2))
        term3 = -2 * self.mass2 * np.sin(self.angle1 - self.angle2)
        term4 = (((self.a_velocity2 ** 2) * self.length2) + ((self.a_velocity1 ** 2) * self.length1 * np.cos(self.angle1 - self.angle2)))
        term5 = self.length1 * ((2 * self.mass1) + self.mass2)
        term6 = -self.mass2 * self.length1 * np.cos(2 * (self.angle1 - self.angle2))
        term7 = 2 * np.sin(self.angle1 - self.angle2)
        term8 = (self.a_velocity1 ** 2) * self.length1 * (self.mass1 + self.mass2)
        term9 = g * np.cos(self.angle1) * (self.mass1 + self.mass2)
        term10 = (self.a_velocity2 ** 2) * self.length2 * self.mass2 * np.cos(self.angle1 - self.angle2)
        term11 = self.length2 * ((2 * self.mass1) + self.mass2)
        term12 = -self.length2 * self.mass2 * np.cos(2 * (self.angle1 - self.angle2))

        self.a_acceleration1 = (term1 + term2 + (term3 * term4)) / (term5 + term6)
        self.a_acceleration2 = (term7 * (term8 + term9 + term10)) / (term11 + term12)
        self.a_velocity1 += (self.a_acceleration1 * dt)
        self.a_velocity2 += self.a_acceleration2 * dt
        self.angle1 += (self.a_velocity1 * dt)
        self.angle2 += (self.a_velocity2 * dt)


pygame.init()
pygame.font.init()

double_pendulum = Pendulum()

width, height = (1000, 1000)
background_colour = (255, 255, 255)
screen = pygame.display.set_mode((width, height))

running = True

while running:

    ev = pygame.event.get()

    screen.fill(background_colour)

    double_pendulum.move()

    double_pendulum.draw()

    pygame.display.flip()

    for event in ev:

        if event.type == pygame.QUIT:

            running = False

plt.plot(double_pendulum.x_coordinates, double_pendulum.y_coordinates)
plt.show()
pygame.quit()
