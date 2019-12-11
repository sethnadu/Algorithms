#!/usr/bin/python

import argparse
import time
def find_max_profit(prices):
  firstTime = time.time()
  largest_margin = int()
  margin = int()
  for i in range(len(prices)):
    for j in range(i):
      diff = prices[i] - prices[j]
      if diff > largest_margin:
        largest_margin = diff
      else: 
        margin = diff
  # print("Largest Margin: ", largest_margin)
  endTime = time.time()
  print("TIme: ", endTime - firstTime, " seconds")
  if largest_margin == 0:
    print("Profit :", margin)
    return margin
  else:
    print("Profit :", largest_margin)
    return largest_margin
 
# find_max_profit([1050, 270, 1540, 3800, 2])
# find_max_profit([10, 7, 5, 8, 11, 9])

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))