def dirReduc(a):
    s = ['']
    for c, i in enumerate(a):
        if i == "SOUTH" and s[-1] == "NORTH":
            s.pop(-1)
        elif i == "NORTH" and s[-1] == "SOUTH":
            s.pop(-1)
        elif i == "EAST" and s[-1] == "WEST":
            s.pop(-1)
        elif i == "WEST" and s[-1] == "EAST":
            s.pop(-1)
        else:
            s.append(i)
    return s[1:]
