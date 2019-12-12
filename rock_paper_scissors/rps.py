#!/usr/bin/python

import sys




def rock_paper_scissors(n):
  plays = [['rock'], ['paper'], ['scissors']]
  total = []

  def check_cycles(n, constantArray = []):
    # Break Case
    if n is 0:
      # Return with all information from check_cycles appended to total array
      return total.append(constantArray)
      
    # Loop through plays
    for i in plays:
      print("add :", constantArray, i)
      # Constant Array becomes first i in list, dosen't change as i loops through plays, concating both arrays
      # Recurison until n hits break case above
      check_cycles(n - 1, constantArray + i)
    return total

  # variable is empty array

  check_cycles(n)
  print("Total :", total)
  return total
   

rock_paper_scissors(2)



# if __name__ == "__main__":
#   if len(sys.argv) > 1:
#     num_plays = int(sys.argv[1])
#     print(rock_paper_scissors(num_plays))
#   else:
#     print('Usage: rps.py [num_plays]')