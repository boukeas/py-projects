'''def sieve(n):
  primes = []
  candidates = list(range(2,n))  
  candidate = candidates.pop(0)
  while candidate < n//2:
    primes.append(candidate)
    for multiple in range(2*candidate, n, candidate):
      if multiple in candidates:
      	candidates.remove(multiple)
    candidate = candidates.pop(0)
  primes.append(candidate)
  primes.extend(candidates)
  return primes
'''

def sieve(n):
  candidates = list(range(0,n))
  flags = n*[True]

  candidate = 2
  while candidate < n//2:
    if flags[candidate]:
      for multiple in range(2*candidate, n, candidate):
        flags[multiple] = False
    candidate += 1

  return [prime for prime in range(2,n) if flags[prime]]

