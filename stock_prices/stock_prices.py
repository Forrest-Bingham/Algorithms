#!/usr/bin/python

import argparse
prices = [1050, 270, 1540, 3800, 2]
def find_max_profit(prices):
    current_min_price = 1000000000
    current_max_profit = -1000000000
    sale = 0
    for x in range(0,len(prices)):
        print(x, "---- Round in loop -----------")
        print(prices[x], "-- prices[x]")
        print(current_min_price)
        if prices[x] <= current_min_price:
            current_min_price = prices[x]
            print(current_min_price, "<-- NEW MIN PRICE")
        print(x, "next x should be x+1")
        for y in range(x+1, len(prices)):
            print("Buying stock for:", prices[x], "Selling for:", prices[y])
            sale = prices[y] - prices[x]
            y += 1
            if sale >= current_max_profit:
                current_max_profit = sale
                print("New MAX PROFIT", current_max_profit)

    return current_max_profit

    # if current_max_profit > 0:
    #     return current_max_profit
    # else: 
    #     return("There is no profit to be gained with these numbers")  
        

print(find_max_profit(prices))
if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))