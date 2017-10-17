def factorial(n):
  '''Finds a factorial of given number'''
  print("factorial of ", n)
  while (n > 1):
    t = n * factorial(n - 1)
    print("returning ", t)
    return t
  print("returning ", 1)
  return 1

print(factorial(4))


