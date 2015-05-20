# coding: utf-8

def main():
  N = input()
  ans = map(int, raw_input())
  points = [0] * 4
  for i in range(4):
    points[i] = len([a for a in ans if a == i + 1])
  print max(points), min(points)

if __name__ == '__main__':
  main()
