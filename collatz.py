# https://en.wikipedia.org/wiki/Collatz_conjecture
# https://xkcd.com/710/

def is_odd(n):
  return n%2

def print_collatz(n):
  print(n, end=" ")
  while n > 1:
    if is_odd(n):
      n = 3*n + 1
    else:
      n = n // 2
    print(n, end=" ")
  print()

def collatz(n):
  yield n
  while n > 1:
    if is_odd(n):
      n = 3*n + 1
    else:
      n = n // 2
    yield n

n = 7
for a in collatz(n):
  print(a, end=' ')
print()

