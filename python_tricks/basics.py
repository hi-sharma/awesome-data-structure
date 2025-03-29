def print_digits(num):
  while num:
    digit = num % 10
    num //= 10
    print(digit)
