def isbn10_check(isbn):
  checksum = 0
  weight = 10
  for digit in isbn[:-1]:
    checksum += weight * int(digit)
    weight -= 1
  if isbn[-1] == 'X':
    checksum += 10
  else:
    checksum += int(isbn[-1])
  return checksum % 11 == 0  

def isbn10_generate(isbn):
  checksum = 0
  weight = 10
  for digit in isbn[:-1]:
    checksum += weight * int(digit)
    weight -= 1
  print(checksum)
  over = checksum % 11
  if over == 0:
    return 0
  elif over == 1:
    return 'X'
  else:
    return 11-over

def isbn13_check(isbn):
  checksum = 0
  weight = 1
  for digit in isbn:
    checksum += weight * int(digit)
    weight = 4-weight
  return checksum % 10 == 0  

def isbn13_generate(isbn):
  checksum = 0
  weight = 1
  for digit in isbn[:-1]:
    checksum += weight * int(digit)
    weight = 4-weight
  over = checksum % 10
  if over == 0:
    return 0
  else:
    return 10 - over  
