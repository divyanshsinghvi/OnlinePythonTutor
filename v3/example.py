# use lists
x = None
for i in range(6, 0, -1):
  x = [i, x]

  # use tuples
y = None
for i in range(6, 0, -1):
    y = (i, y)

x[1][0]=y[1][1] # courtesy of John DeNero!
