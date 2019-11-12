days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

def dayofweek(day, month, year):
  
  if month > 2:
    month = month - 2
  else:
    month = month + 10
    year = year - 1

  y = year % 100
  c = year // 100

  return (day + (13*month-1)//5 + y + y//4 + c//4 - 2*c) % 7
