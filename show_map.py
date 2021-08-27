#! /usr/bin/env python3
''' Show off mazes and their algorithms. '''
import pygame
import pygame.gfxdraw
from pygame.locals import *
import automaton


def main():
    pygame.init()
    screen = pygame.display.set_mode([1034, 778])
    running = True
    grid_width = 20
    row = int(778 / grid_width)
    col = int(1034 / grid_width)
    automata = automaton.Automata(col, row)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == K_q:  # Quit
                    running = False
                elif event.key == K_n:  # New
                    automata = automaton.Automata(col, row)
                elif event.key == K_f:  # Save to FILE
                    pygame.image.save(screen, 'automaton.png')
                elif event.key == K_a:  # Automaton
                    automata.life_stage(1)
                elif event.key == K_i:  # Automaton
                    automata.island_simulation(1, 4, 3)
        display_map(automata, screen, grid_width)
        pygame.display.flip()


def display_map(automata, screen, grid_width):
    island = pygame.Color('#478de9')
    ocean = pygame.Color('#3c4245')
    screen.fill(ocean)
    for x in range(automata.row):
        for y in range(automata.col):
            c = automata.map[x][y]
            cell_x = x * grid_width + 5
            cell_y = y * grid_width + 5
            if c == 1:
                cell = pygame.Rect(cell_x, cell_y, grid_width, grid_width)
                pygame.draw.rect(screen, island, cell)


if __name__ == "__main__":
    main()
