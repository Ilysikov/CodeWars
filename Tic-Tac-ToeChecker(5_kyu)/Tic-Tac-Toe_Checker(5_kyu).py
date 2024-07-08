def is_solved(board):
    x = []
    t = []
    o = 0
    for h in board:
        if 0 in h:
            o = -1
        for k, i in enumerate(h):
            if i == 1:
                x.append(k)
            elif i == 2:
                t.append(k)

    for u in x:
        if x.count(u) >= len(board):
            o = 1
    for e in t:
        if t.count(e) >= len(board):
            o = 2
    for i in (-1, 0, 1):
        l = 0
        y = 0
        for q, w in enumerate(x):
            l += q
            y = 0
            while l + 1 < len(x) and x[l] - x[l + 1] == i:
                l += 1
                y += 1
                if y == len(board) - 1:
                    o = 1
    for i in (-1, 0, 1):
        l = 0
        y = 0
        for q, w in enumerate(t):
            l += q
            y = 0
            while l + 1 < len(t) and t[l] - t[l + 1] == i:
                l += 1
                y += 1
                if y == len(board) - 1:
                    o = 2

    return o
