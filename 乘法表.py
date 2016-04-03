for i in range(1,10):
    for j in range(1, 10):
        if j>=i:
          formula = '{0:1}x{1:1}={2:<2}'.format(i, j, i*j)
          print(formula, end=' ')
        else:
          print(end='       ')
    print()