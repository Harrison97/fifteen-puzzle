import random
import copy

LEFT = 'LEFT'
RIGHT = 'RIGHT'
UP = 'UP'
DOWN = 'DOWN'

class Puzzle:
    def __init__(self, height, width):
        # empty_space is represented as the largest number in the puzzle: width*height-1
        self.__empty_space = []
        self.__width = width
        self.__height = height
        self.__puzzle = []
        self.__solved = []
        self.__build_puzzle()

    def __getitem__(self, loc):
        return self.__puzzle[loc[0]][loc[1]]

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return self.__stringify()

    def __stringify(self):
        s = ''
        for i in range(self.__height):
            s += str(self.__puzzle[i]) + ('\n' if i != self.__height-1 else '')
        return s

    def __build_puzzle(self):
        puzzle = [[y*self.__width+x for x in range(self.__width)] for y in range(self.__height)]
        self.__puzzle = puzzle
        self.__solved = puzzle
        self.__empty_space = [self.__width-1, self.__height-1]

    def randomize(self):
        numbers = [x for x in range(self.__width*self.__height)]
        puzzle = []
        solved = []
        for i in range(self.__height):
            row = []
            solved_row = []
            for j in range(self.__width):
                index = int(random.random()*len(numbers))
                row.append(numbers[index])
                if numbers[index] == self.__width*self.__height-1:
                    self.__empty_space = [i, j]
                solved_row.append(self.__height*self.__width-len(numbers))
                numbers.pop(index)

            puzzle.append(row)
            solved.append(solved_row)

        self.__puzzle = puzzle
        self.__solved = solved

    def clone(self):
        return copy.deepcopy(self)

    def is_solved(self):
        return self.__puzzle == self.__solved

    def get_empty_space(self):
        return self.__empty_space

    def get_height(self):
        return self.__height

    def get_width(self):
        return self.__width

    def slide(self, *args):
        if len(args) == 1:
            direction = args[0]
            if 0 in self.__empty_space and (direction is RIGHT or direction is DOWN):
                    raise IndexError('list index out of range')
            if direction == RIGHT:
                self.__slide(self.__empty_space[0], self.__empty_space[1]-1)
            if direction == LEFT:
                self.__slide(self.__empty_space[0], self.__empty_space[1]+1)
            if direction == UP:
                self.__slide(self.__empty_space[0]+1, self.__empty_space[1])
            if direction == DOWN:
                self.__slide(self.__empty_space[0]-1, self.__empty_space[1])

        elif len(args) == 2:
            row = args[0]
            col = args[1]
            if self.__puzzle[row][col] == self.__width*self.__height-1:
                return
            if [row-1, col] == self.__empty_space:
                self.__puzzle[row-1][col] = self.__puzzle[row][col]
                self.__puzzle[row][col] = self.__width*self.__height-1
            if [row+1, col] == self.__empty_space:
                self.__puzzle[row+1][col] = self.__puzzle[row][col]
                self.__puzzle[row][col] = self.__width*self.__height-1
            if [row, col-1] == self.__empty_space:
                self.__puzzle[row][col-1] = self.__puzzle[row][col]
                self.__puzzle[row][col] = self.__width*self.__height-1
            if [row, col+1] == self.__empty_space:
                self.__puzzle[row][col+1] = self.__puzzle[row][col]
                self.__puzzle[row][col] = self.__width*self.__height-1

            self.__empty_space[0] = row
            self.__empty_space[1] = col

            if self.is_solved():
                print("You have solved the puzzle!!!")

        else:
            raise TypeError('slide() takes 1 or 2 positional arguments ONLY.')

