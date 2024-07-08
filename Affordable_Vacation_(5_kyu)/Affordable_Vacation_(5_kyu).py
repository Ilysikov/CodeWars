def find_min_cost(money, days, cost):
    cost = tuple(cost)
    hol = sum(cost[:days])
    mon = hol
    for c, l in enumerate(cost[days:]):
        hol = hol - cost[c] + l
        mon = hol if hol < mon else mon
    if mon <= money:
        return f"money: {mon}"
    else:
        amount, ind, quan = 0, 0, 0
        for c, i in enumerate(cost):
            if amount + i > money:
                break
            amount += i
            quan = c + 1
        hol = quan
        for sub in cost[quan:]:
            while amount + sub > money and ind < len(cost):
                amount = amount - cost[ind]
                amount = 0 if amount < 0 else amount
                ind += 1
                quan -= 1
                quan = 0 if quan < 0 else quan
            if amount + sub <= money:
                amount = amount + sub
                quan = quan + 1
            hol = quan if quan > hol else hol
        return f"days: {hol}"
