import random
import copy

LEFT = 'LEFT'
RIGHT = 'RIGHT'
UP = 'UP'
DOWN = 'DOWN'

class Puzzle:
    def __init__(self, height, width):
        self.width = width
        self.height = height
        self.puzzle = []
        self.solved = []
        self.__build_puzzle()

    def __getitem__(self, loc):
        return self.puzzle[loc[0]][loc[1]]

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return self.__stringify()

    def __stringify(self):
        s = ''
        for i in range(self.height):
            s += str(self.puzzle[i]) + ('\n' if i != self.height-1 else '')
        return s

    def __build_puzzle(self):
        numbers = [x for x in range(self.width*self.height)]
        puzzle = []
        solved = []
        for i in range(self.height):
            row = []
            solved_row = []
            for j in range(self.width):
                index = int(random.random()*len(numbers))
                row.append(numbers[index])
                if numbers[index] == self.width*self.height-1:
                    self.empty_space = [i, j]
                solved_row.append(self.height*self.width-len(numbers))
                numbers.pop(index)

            puzzle.append(row)
            solved.append(solved_row)

        self.puzzle = puzzle
        self.solved = solved

    def clone(self):
        return copy.deepcopy(self)

    def slide(self, *args):
        if len(args) == 1:
            direction = args[0]
            if 0 in self.empty_space and (direction is RIGHT or direction is DOWN):
                    raise IndexError('list index out of range')
            if direction == RIGHT:
                self.slide(self.empty_space[0], self.empty_space[1]-1)
            if direction == LEFT:
                self.slide(self.empty_space[0], self.empty_space[1]+1)
            if direction == UP:
                self.slide(self.empty_space[0]+1, self.empty_space[1])
            if direction == DOWN:
                self.slide(self.empty_space[0]-1, self.empty_space[1])

        elif len(args) == 2:
            row = args[0]
            col = args[1]
            if self.puzzle[row][col] == self.width*self.height-1:
                return
            if [row-1, col] == self.empty_space:
                self.puzzle[row-1][col] = self.puzzle[row][col]
                self.puzzle[row][col] = self.width*self.height-1
                self.empty_space[0] = row
                self.empty_space[1] = col
            if [row+1, col] == self.empty_space:
                self.puzzle[row+1][col] = self.puzzle[row][col]
                self.puzzle[row][col] = self.width*self.height-1
                self.empty_space[0] = row
                self.empty_space[1] = col
            if [row, col-1] == self.empty_space:
                self.puzzle[row][col-1] = self.puzzle[row][col]
                self.puzzle[row][col] = self.width*self.height-1
                self.empty_space[0] = row
                self.empty_space[1] = col
            if [row, col+1] == self.empty_space:
                self.puzzle[row][col+1] = self.puzzle[row][col]
                self.puzzle[row][col] = self.width*self.height-1
                self.empty_space[0] = row
                self.empty_space[1] = col

            if self.puzzle == self.solved:
                print("You have solved the puzzle!!!")

        else:
            raise TypeError('slide() takes 1 or 2 positional arguments ONLY.')

