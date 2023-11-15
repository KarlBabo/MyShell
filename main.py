from subprocess import run as r
from subprocess import PIPE as p
from sys import argv as a

'''
Yes I'm in a war...
maybe code is very sucks
'''

def s(x):
  '''
  use subprocess shell (run) like os shell (system)
  '''
  return r(x, shell=True stdout=p)

def p(x):
  '''
  just math function
  '''
  return x != 'exit' # x ≠ string 'exit'
           
def main():
  if len(a) == 2:
    with open(a[1], 'r') as f:
      for line in f.readlines():
        s(line)
  else:
    a = None
    while p(a):
      a = input('> ')
      if p(a): s(a)

if __name__ == "__main__": main()