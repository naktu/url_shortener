import random

from string import ascii_letters, digits


def code_generator(size=7, chars=ascii_letters+digits):
    return ''.join(random.choice(chars) for _ in range(size))


def create_short_code(instance, size=7):
    new_code = code_generator(size=size)
    s_class = instance.__class__
    qs_exists = s_class.objects.filter(short_code=new_code).exists()
    if qs_exists:
        return create_short_code(instance, size=size)
    return new_code
