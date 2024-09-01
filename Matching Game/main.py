import pygame
pygame.init()

WIDTH = 600
HEIGHT = 600
BLACK = 0,0,0

screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill("white")
pygame.display.set_caption("Matching Games")
pygame.display.update()

candy_crush = pygame.image.load("./images/candycrush.jpeg")
ludo = pygame.image.load("./images/ludo.png")
subway_surfers = pygame.image.load("./images/subwaysurfers.png")
temple_run = pygame.image.load("./images/templerun.png")

screen.blit(candy_crush, (150,100))
screen.blit(ludo, (150,200))
screen.blit(subway_surfers, (150,300))
screen.blit(temple_run, (150,400))

font = pygame.font.SysFont("futura", 45)

text1 = font.render("Subway Surfers", False, BLACK)
text2 = font.render("Candy Crush", False, BLACK)
text1 = font.render("Temple Run", True, BLACK)
text2 = font.render("Ludo", True, BLACK)

pygame.display.update()

while 1:
    pass