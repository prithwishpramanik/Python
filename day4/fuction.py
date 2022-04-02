def is_even(num):
    """checks if agiven number is odd or even 
        input any valid +ve integers
        outut-odd/even"""

    if num %2 == 0:
        return "even"
    else:
        return "odd"
for i in range(1,11):
        print(is_even(i))

