



def stairCase(n):
  spaces = n - 1
  for i in range(1, n):
      a = ' ' * spaces
      a = a + ('#' * i)
      spaces = spaces -1
      print (a)



# stairCase(6)


import sys


def sum_from_stdin():
    # for line in sys.stdin:
    #     print line
    size = sys.stdin.readline()

    # print size
    sum = 0
    for i in range(0, int(size)):
        sum += int(sys.stdin.readline())

    print (sum)


sum_from_stdin()
