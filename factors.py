def factors(n):
  factor = 2
  while n>1:
    div, mod = divmod(n, factor)
    if (mod == 0):
      yield factor
      n = div
    else:
      factor = factor+1

