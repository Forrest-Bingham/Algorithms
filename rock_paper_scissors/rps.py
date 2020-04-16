#!/usr/bin/python

import sys
rps = [["rock"], ["paper"], ["scissors"]]
def rock_paper_scissors(n):
    #Base case
    if n == 0:
        return [[]]

    elif n == 1:
        return rps

    #create list of lists with correct length: 3**n
    list = []

    moves = rock_paper_scissors(n-1)  #Recursion step, taking moves from previous rps
    print(moves, "-----> Moves from n-1. Length is: ", len(moves))
    for x in moves:
        print(x, "------ X")
        for y in rps:
            print(y, "--------------Y", len(rps))
            newMove = x + y
            print(newMove, "----------- Adding this move to big list")
            list.append(newMove)

    return list

    #loop through the big list 

    #each loop outputs a possible option for rps
    


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')