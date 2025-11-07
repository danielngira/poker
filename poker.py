from logic import Player, Game, Card, Deck, PokerException
import pygame

pygame.init()
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("green")

    ###
    ### Game is rendered here
    ###
    pygame.draw.rect()

    pygame.display.flip()
    clock.tick(60)


pygame.quit()

