N = input()
cards = map(int, raw_input().split(' '))

score = [0, 0]

for i in range(N):
  c = max(cards)
  score[i%2] += c
  cards.remove(c)

print score[0]
