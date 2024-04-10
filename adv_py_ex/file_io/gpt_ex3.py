def validate_email(email):
    if '@' not in email:
        raise ValueError('The email doesn\'t contain an @ sign!')
    split_email = email[email.index('@') + 1:]
    print(split_email)
    split_domain = split_email[split_email.index('.'):]
    print(split_domain)
    if len(split_domain) <= 3:
        raise ValueError('Domain must be at least 3 chars!')
    if split_email[0] == '.':
        raise ValueError('Period can\'t start the domain')
    if split_email[-1] == '.':
        raise ValueError('Period can\'t be the last char of the email')


try:
    validate_email('mayfieldgabrielj@gmail.com.')
    print('Email is valid!!!')
except ValueError as e:
    print(f'Invalid email: {e}')
