# coding: utf-8

def main():
  N = input()
  ms = raw_input()
  print sum([80 - m for m in map(int, ms.split(' ')) if m < 80])

if __name__ == '__main__':
  main()
