xa, ya, xb, yb, xc, yc = map(int, raw_input().split(' '))
print abs(xa*yb + xb*yc + xc*ya - ya*xb - yb*xc - yc*xa) / 2.
