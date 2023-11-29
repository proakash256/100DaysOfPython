def generate_password():
    import random
    import string

    letters = list(string.ascii_letters)
    numbers = list(string.digits)
    symbols = list(string.punctuation)

    password_list = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_list.extend([random.choice(numbers) for _ in range(random.randint(2, 4))])
    password_list.extend([random.choice(symbols) for _ in range(random.randint(2, 4))])

    random.shuffle(password_list)

    password = "".join(password_list)

    return password
