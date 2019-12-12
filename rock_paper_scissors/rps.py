#!/usr/bin/python

import sys




def rock_paper_scissors(n):
  plays = ['rock', 'paper', 'scissors']
  single = []
  total = []

  def check_cycles(play, play2):
      single.append(play)
      single.append(play2)
      total.append(single)
      return total

  for i in range(len(plays)):
    for j in range(len(plays)):
      if not plays[i]:
        return total
      else:
        if len(single) <= n:
          check_cycles(plays[i], plays[j])

  print(single) 
  print(play)
  # def check_cycles(i):
  #   for p in range(len(plays)): 
  #       oneResult.append(plays[i])
  #       oneResult.append(plays[p])
  #       totalResults.append(oneResult)

  # for i in range(len(plays)):
  #   check_cycles(i)

    #  n is length of inner list
    #  show all combinations of each play
    #  add them all to a list, checking to see if it doesn't exist

rock_paper_scissors(2)



# if __name__ == "__main__":
#   if len(sys.argv) > 1:
#     num_plays = int(sys.argv[1])
#     print(rock_paper_scissors(num_plays))
#   else:
#     print('Usage: rps.py [num_plays]')