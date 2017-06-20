"""Returns all valid combinations for N-queens problem"""
import argparse
from itertools import permutations
from termcolor import cprint

def check_valid(combination):
    """Returns true if combination is valid"""
    for queen1 in combination:
        for queen2 in combination:
            if (queen1[0] != queen2[0]
                    and abs(queen1[1]-queen2[1]) == abs(queen1[0]-queen2[0])):
                return False
    return True

def print_valid_combination(combination):
    """Prints combination if it is valid"""
    if check_valid(combination):
        draw_checkboard(combination)
        return True
    return False

def print_valid_combinations(queencombinations):
    """Prints all valid combinations"""
    map(print_valid_combination,
        [combination
         for combination in queencombinations
        ])

def count_valid_combinations(queencombinations):
    """Counts all valid combinations"""
    count = 0
    for combination in queencombinations:
        if print_valid_combination(combination):
            count += 1
    return count

def generate_combinations(queennumber):
    """Generates all combinations"""
    for ypositions in permutations(xrange(1, queennumber+1)):
        yield zip(xrange(1, queennumber+1), ypositions)

def parse_args():
    """Parses arguments"""
    parser = argparse.ArgumentParser()
    parser.add_argument('n',
                        help='number of queens')
    return int(parser.parse_args().n)

def draw_checkboard(combination):
    """Draws checkboard for each combination"""
    print_field = lambda x, y: (cprint(x, 'blue', 'on_white', end='')
                                if y else cprint(x, 'blue', 'on_red', end=''))
    string = [unichr(9813)  if combination[row][1] == column else ' '
              for row in xrange(len(combination))
              for column in xrange(1, len(combination)+1)
             ]
    for row in xrange(len(combination)):
        for column in xrange(len(combination)):
            print_field(string[row*len(combination)+column], (row+column)%2)
        print
    print

def main():
    """Main function"""
    queennumber = parse_args()
    queencombinations = generate_combinations(queennumber)
    print_valid_combinations(queencombinations)

if __name__ == "__main__":
    main()
