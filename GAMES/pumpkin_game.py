import pygame

screen = pygame.display.set_mode((800,600))     #display settings

#title & icon
title = "Pumpkin Shooter"
icon = pygame.image.load('logo.png')
pygame.display.set_caption(title)
pygame.display.set_icon(icon)

game_on = True          
while game_on:
    #background color RGB values
    screen.fill((121, 145, 102))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_on = False
    pygame.display.update()
