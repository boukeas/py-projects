def dec2bin(dec):
  ''' convert decimal to binary
      dec: the integer to be converted to binary
      returns: a string of binary digits
  '''
  bin_list = []
  while dec:
    digit = str(dec%2)
    bin_list.append(digit)
    dec = dec//2
  return "".join(reversed(bin_list))

def bin2dec(bin):
  ''' convert binary to decimal
      bin: a string of binary digits
      returns: the corresponding integer in decimal
  '''
  dec = 0
  weight = 1
  for digit in reversed(bin):
    dec += int(digit) * weight
    weight *= 2
  return dec
