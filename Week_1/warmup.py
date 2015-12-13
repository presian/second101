from sys import argv


def factorial(n):
    result = 1
    for number in range(1, n + 1):
        result = result * number
    return result


def fibonacci(n):
    if(n == 1):
        return [1]
    elif(n == 2):
        return [1, 1]
    else:
        return [sum(fibonacci(x - 1)[-2:]) if x > 2 else 1 for x in range(1, n + 1)]


def sum_of_digits(number):
    number = abs(number)
    return sum(number_as_digit(number))


def fact_digits(number):
    return sum([factorial(x) for x in number_as_digit(number)])


def palindrome(obj):
    return obj == obj[::-1]


def to_digits(n):
    return number_as_digit(n)[::-1]


def to_number(digits):
    return int(str.join('', digits))


def fib_number(n):
    return to_number([str(x) for x in fibonacci(n)])


def count_vowels(string):
    vowels = 'aeiouy'
    return sum([(1 if x.lower() in vowels else 0) for x in string])


def number_as_digit(number):
    result = []
    while number > 0:
        result.append(number % 10)
        number = number // 10
    return result


def main(functionData):
    parameterOne = ''
    if functionData[1] == 'number':
        parameterOne = int(argv[2])
    elif functionData[1] == 'list':
        parameterOne = argv[2:]
    else:
        parameterOne = argv[2]
    print(functionData[0](parameterOne))

if __name__ == '__main__':
    functions = {
        'factorial': [factorial, 'number'],
        'fibonacci': [fibonacci, 'number'],
        'sum_of_digits': [sum_of_digits,  'number'],
        'fact_digits': [fact_digits,  'number'],
        'palindrome': [palindrome,  'string'],
        'to_digits': [to_digits, 'number'],
        'to_number': [to_number, 'list'],
        'fib_number': [fib_number, 'number'],
        'count_vowels': [count_vowels, 'string'],
    }
    main(functions[argv[1]])
