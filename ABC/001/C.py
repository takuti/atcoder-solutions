
def ans(Deg, Dis):
  """
  >>> ans(2750, 628)
  W 5
  >>> ans(161, 8)
  C 0
  >>> ans(3263, 15)
  NNW 1
  >>> ans(1462, 1959)
  SE 12
  >>> ans (1687, 1029)
  SSE 8
  >>> ans(2587, 644)
  WSW 5
  >>> ans(113, 201)
  NNE 3
  >>> ans(2048, 16)
  SSW 1
  """

  Dis = int(round(Dis * 10/ 60., 0))
  Dis_th = [2, 15, 33, 54, 79, 107, 138, 171, 207, 244, 284, 326]
  for i in range(13):
    if i == 12:
      W = 12
    elif Dis <= Dis_th[i]:
      W = i
      break

  if W == 0:
    Dir = 'C'

  else:
    Deg = Deg / 10.
    directions = ['N', 'NNE', 'NE', 'ENE', 'E', 'ESE', 'SE', 'SSE', 'S', 'SSW', 'SW', 'WSW', 'W', 'WNW', 'NW', 'NNW', 'N']

    step = 22.5
    upper = 11.25
    i = 0
    while upper < 360:
      if Deg < upper: break
      upper += step
      i += 1

    Dir = directions[i]

  print Dir, W

if __name__ == '__main__':
  import doctest
  doctest.testmod()
