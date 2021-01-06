
row = 2981
col = 3075

number = 20151125

c = 1
r = 1

while True:

  if r == 1:
    r = c + 1
    c = 1
  
  else:
    r -= 1
    c += 1

  number *= 252533
  number %= 33554393

  if (r, c) == (row, col):
    break

print(number)
