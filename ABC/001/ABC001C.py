
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
  if Dis <= 2: W = 0
  elif Dis <= 15: W = 1
  elif Dis <= 33: W = 2
  elif Dis <= 54: W = 3
  elif Dis <= 79: W = 4
  elif Dis <= 107: W = 5
  elif Dis <= 138: W = 6
  elif Dis <= 171: W = 7
  elif Dis <= 207: W = 8
  elif Dis <= 244: W = 9
  elif Dis <= 284: W = 10
  elif Dis <= 326: W = 11
  else: W = 12

  if W == 0:
    Dir = 'C'
  else:
    Deg = Deg / 10.
    if Deg < 11.25 or Deg >= 348.75: Dir = 'N'
    elif Deg < 33.75: Dir = 'NNE'
    elif Deg < 56.25: Dir = 'NE'
    elif Deg < 78.75: Dir = 'ENE'
    elif Deg < 101.25: Dir = 'E'
    elif Deg < 123.75: Dir = 'ESE'
    elif Deg < 146.25: Dir = 'SE'
    elif Deg < 168.75: Dir = 'SSE'
    elif Deg < 191.25: Dir = 'S'
    elif Deg < 213.75: Dir = 'SSW'
    elif Deg < 236.25: Dir = 'SW'
    elif Deg < 258.75: Dir = 'WSW'
    elif Deg < 281.25: Dir = 'W'
    elif Deg < 303.75: Dir = 'WNW'
    elif Deg < 326.25: Dir = 'NW'
    else: Dir = 'NNW'

  print Dir, W

def main():
  Deg, Dis = map(int, raw_input().split(' '))
  Dis = int(round(Dis * 10/ 60., 0))
  if Dis <= 2: W = 0
  elif Dis <= 15: W = 1
  elif Dis <= 33: W = 2
  elif Dis <= 54: W = 3
  elif Dis <= 79: W = 4
  elif Dis <= 107: W = 5
  elif Dis <= 138: W = 6
  elif Dis <= 171: W = 7
  elif Dis <= 207: W = 8
  elif Dis <= 244: W = 9
  elif Dis <= 284: W = 10
  elif Dis <= 326: W = 11
  else: W = 12

  if W == 0:
    Dir = 'C'
  else:
    Deg = Deg / 10.
    if Deg < 11.25 or Deg >= 348.75: Dir = 'N'
    elif Deg < 33.75: Dir = 'NNE'
    elif Deg < 56.25: Dir = 'NE'
    elif Deg < 78.75: Dir = 'ENE'
    elif Deg < 101.25: Dir = 'E'
    elif Deg < 123.75: Dir = 'ESE'
    elif Deg < 146.25: Dir = 'SE'
    elif Deg < 168.75: Dir = 'SSE'
    elif Deg < 191.25: Dir = 'S'
    elif Deg < 213.75: Dir = 'SSW'
    elif Deg < 236.25: Dir = 'SW'
    elif Deg < 258.75: Dir = 'WSW'
    elif Deg < 281.25: Dir = 'W'
    elif Deg < 303.75: Dir = 'WNW'
    elif Deg < 326.25: Dir = 'NW'
    else: Dir = 'NNW'

  print Dir, W

if __name__ == '__main__':
  import doctest
  doctest.testmod()
