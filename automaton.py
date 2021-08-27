#! /usr/bin/env python3
''' Run cool maze generating algorithms. '''
import random
import time


class Automata:

    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.map = [[random.randrange(0, 2)
                     for _ in range(col)] for _ in range(row)]

    def printMap(self):
        for x in range(self.row):
            for y in range(self.col):
                print(self.map[x][y], end='  ')
            print("\n")
        print(" ")

    def life_stage(self, generations):
        ''' generations '''
        temp = [[0 for _ in range(self.col)] for _ in range(self.row)]
        for _ in range(generations):
            for x in range(self.row):
                for y in range(self.col):
                    count = self.surroundings(x, y)
                    deadORalive = self.dead_or_alive(self.map[x][y], count)
                    temp[x][y] = deadORalive
            self.map = temp
        ''' end stage '''

    def island_simulation(self, generations, birthLimit, deathLimit):
        ''' generations '''
        temp = [[0 for _ in range(self.col)] for _ in range(self.row)]
        for _ in range(generations):
            for x in range(self.row):
                for y in range(self.col):
                    count = self.surroundings(x, y)
                    isIsland = self.isIsland(
                        self.map[x][y], count, birthLimit, deathLimit)
                    temp[x][y] = isIsland
            self.map = temp
        ''' end stage '''

    def isIsland(self, isAlive, count, birthLimit, deathLimit):
        if isAlive == 1:
            if count < deathLimit:
                return 0
            else:
                return 1
        else:
            if count > birthLimit:
                return 1
            else:
                return 0

    def dead_or_alive(self, isAlive, count):
        '''
            If a living cell has less than two living neighbours, it dies.
            If a living cell has two or three living neighbours, it stays alive.
            If a living cell has more than three living neighbours, it dies.
            If a dead cell has exactly three living neighbours, it becomes alive.
        '''
        if count < 2:
            return 0
        if isAlive == 1:
            if count > 3:
                return 0
        elif isAlive == 0:
            if count == 3:
                return 1
        return isAlive

    def surroundings(self, x, y):
        count = 0

        ''' edge cases '''
        if x < 1 or x == self.row - 1:
            offset_x = 1 if x < 1 else -1
            offset_y = 1 if y < 1 else -1

            count += self.map[x+offset_x][y]
            count += self.map[x][y+offset_y]
            count += self.map[x+offset_x][y+offset_y]

            if y < 1 or y == self.col - 1:
                ''' 3 neighbors '''
                return count
            else:
                ''' 5 neighbors '''
                count += self.map[x][y-offset_y]
                count += self.map[x+offset_x][y-offset_y]
                return count

        if y < 1 or y == self.col - 1:
            ''' 5 neighbors '''
            offset_y = 1 if y < 1 else -1
            count += self.map[x-1][y]
            count += self.map[x-1][y+offset_y]
            count += self.map[x+1][y]
            count += self.map[x+1][y+offset_y]
            count += self.map[x][y+offset_y]
            return count

        ''' general '''
        count += self.map[x+1][y]
        count += self.map[x+1][y+1]
        count += self.map[x+1][y-1]
        count += self.map[x][y+1]
        count += self.map[x][y-1]
        count += self.map[x-1][y]
        count += self.map[x-1][y-1]
        count += self.map[x-1][y+1]

        return count


def main():
    pass


if __name__ == "__main__":
    main()
