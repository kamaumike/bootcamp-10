def fizz_buzz(number):
  """Returns 'Fizz' if a number is divisible by 3, 'Buzz' if a number is divisible by 5
  'FizzBuzz' if a number is divisible by both 3 and 5
  otherwise it returns the number itself
  """
  if number %  3 == 0 and number % 5 == 0:
    return "FizzBuzz";
  elif number %  3 == 0:
    return "Fizz";
  elif number %  5 == 0:
    return "Buzz";
  else:
    return number;  

print(fizz_buzz(20))
