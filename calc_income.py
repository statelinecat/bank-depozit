def bank(a, years, rate):
  for i in range(years):
    a += a * (rate / 100)
  return a

