def reverse_string(string):
    """Reverse string and returns string."""
    reversed_string = ''.join(list(reversed(string)))
    return reversed_string


def get_average(nums:list):
    """Calculate avarage of the list of numbers."""
    sum_num = 0
    for t in nums:
        sum_num = sum_num + t           
    avg = sum_num / len(nums)
    return avg


def price_of_the_item (monthly_payment, payment_time):
    """Calculate price of the item based on monthly payment amount and payment time."""
    price = monthly_payment * payment_time
    return price


def sum_of_even_numbers (list_of_numbers:list):
    sum = 0
    for i in list_of_numbers:
        if i % 2 == 0:
            sum = sum + i
    return(sum)

