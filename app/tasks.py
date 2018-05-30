import string

from django.contrib.auth.models import User
from django.utils.crypto import get_random_string

from celery import shared_task

from .models import TypedWord


# @shared_task
# def create_random_user_accounts(total):
#     for i in range(total):
#         username = 'user_{}'.format(
#             get_random_string(10, string.ascii_letters))
#         email = '{}@example.com'.format(username)
#         password = get_random_string(50)
#         User.objects.create_user(
#             username=username, email=email, password=password)
#     return '{} random users created with success!'.format(total)


@shared_task
def random_string(word):
    random_word = print(get_random_string(10, string.ascii_letters))
    print('Hello')
    return random_word


@shared_task
def create_typed_word(word):
    TypedWord.objects.create(typed_word=word)
    return '{}'.format(word)
