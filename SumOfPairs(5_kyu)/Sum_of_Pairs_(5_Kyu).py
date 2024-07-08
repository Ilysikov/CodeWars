def sum_pairs(i, s):
    d = []
    for v in i:
        if v not in d or (v + v == s and d.count(v) < 2):
            d.append(v)
            for k, r in enumerate(d):
                for f in d[k + 1:]:
                    if r + f == s:
                        return [r, f]
