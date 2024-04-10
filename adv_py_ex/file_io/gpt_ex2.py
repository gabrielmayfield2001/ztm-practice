def valid_email(email):
    count_of_at = str(email).count('@')
    if count_of_at != 1:
        raise ValueError('Email must contain an \'@\' symbol!')

    split_email = email[email.index('@') + 1:]
    split_domain = split_email[split_email.index('.'):]
    domain_length = len(split_email)
    if domain_length <= 3:
        raise ValueError('Email domain must be 3 chars or more!')
    if '.' not in split_email:
        raise ValueError(
            'Must contain a dot in the middle of domain in email.')
    print(split_email)
    print(split_domain)
    if split_email[0] == '.':
        raise ValueError('The first char in domain can\'t be a period.')
    if split_domain[-1] == '.':
        raise ValueError('Last char of the email can\'t be a period.')

    return True


test = valid_email('mayfieldgabrielj@gmail.com')

print(test)
