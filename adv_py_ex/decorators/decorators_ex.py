# Create an @authenticated decorator that only allows the function to run is user1 has 'valid' set to True:
user1 = {
    'name': 'Sorna',
    # changing this will either run or not run the message_friends function.
    'valid': True
}


def authenticated(fn):
    def wrapper(*args, **kwargs):
        if args[0]['valid']:
            fn(*args, **kwargs)
        else:
            print('invalid user')
    return wrapper


@authenticated
def message_friends(user, emoji = ':)'):
    print(f'message has been sent', emoji)


message_friends(user1, ':((')
