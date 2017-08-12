# A function for counting the digits of a number
def sum_of_digits(number):
    number = abs(number)
    sum = 0

    while number:
        sum += number % 10
        number = number // 10

    print(sum)

sum_of_digits(-123)


# Create list with the digits of a number
def to_digits(number):
    number = number
    list = []

    while True:
        list.append(number % 10)
        number = number // 10

        if number == 0:
            break

    list.reverse()
    print(list)

to_digits(3566)


# Create number from array
def to_number(digits):
    number = ''

    for digit in digits:
        number += str(digit)

    print(number)

to_number([21, 3, 2])


# Count the vowels in a string
def count_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    count = 0

    for letter in string:

        if letter.lower() in vowels:
            count += 1

    print(count)

count_vowels('Theistareykjarbunga')


# Count the consonants in a string
def count_consonants(string):
    constants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't',
                 'v', 'w', 'x', 'z']
    count = 0

    for letter in string:
        if letter.lower() in constants:
            count += 1

    print(count)

count_constants('Theistareykjarbunga')


# Check if a given number is prime
def prime_number(number):
    if number < 2:
        return False

    for x in range(2, number):
        if (number % x == 0):
            return False

    return True

prime_number(8)

# Sum of the factorials of the digits in the number
def fact_digits(n):
    pass
    # sum = 0
    # while n:
    #     factorial = n % 10
    #     factorialSum = 0
        #
        # JS
        # function sFact(num) {
        #     var rval=1;
        #     for (var i = 2; i <= num; i++)
        #         rval = rval * i;
        #     return rval;
        #
        # }
        #
        # n //= 10
    #
    # print(sum)
#
# fact_digits(4)


# fibonacci sequince
def fibonacci(number):
    pass


# Check if a given string is palindrome
def palindrome(string):
    pass


# Dictionary with all characters from a string
def char_histogram(string):
    pass
