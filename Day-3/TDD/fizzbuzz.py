def fizzbuzz(number):
    """Returns 'Fizz' if divisible by 3, 
    'Buzz' if divisible by 5 and 
    'FizzBuzz' if divisible by both 3 and 5
    """

    if number % 15 == 0:
        return 'FizzBuzz'
    elif number % 5 == 0:
        return 'Buzz'
    elif number % 3 == 0:
        return 'Fizz'
    else:
        return number


