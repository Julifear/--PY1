import string
from random import sample


def get_random_password(length=8) -> str:
    available_elements = string.ascii_lowercase + string.ascii_uppercase + string.digits
    result = ''.join(sample(available_elements, length))
    return result


print(get_random_password())