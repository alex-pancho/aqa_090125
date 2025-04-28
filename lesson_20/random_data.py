import random
import string

def generate_random_categories(num=5):
    """Generate random categories."""
    return [(random_string(10),) for _ in range(num)]

def generate_random_products(num=10, category_ids=[]):
    """Generate random products with random categories."""
    return [
        (random_string(10), random_string(20), random_price(), random.choice(category_ids))
        for _ in range(num)
    ]

def random_string(length=10):
    """Generate a random string."""
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))

def random_price(min_price=1.0, max_price=1000.0):
    """Generate a random price."""
    return round(random.uniform(min_price, max_price), 2)
