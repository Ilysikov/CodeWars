def alphanumeric(password):
    g = 0
    c = 0
    for i in password.lower():
        if i in 'qwertyuiopasdfghjklzxcvbnm':
            g += 1
        elif i in '01234456789':
            c += 1
    return True if g + c == len(password) and password != '' else False
