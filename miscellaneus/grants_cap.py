def find_grants_cap(grants, new_budget):
    # bud = 190, even_bud = new_bud/n = 38
    # 2, 100, 50, 120, 1000   leftover = 1082

    # 1 -. start with cap = even bud:
    # 2, 38, 38, 38, 38       leftover = -36
    # 0, 62, 12, 82, 962      sum = 1118

    # 2-. if leftover is negative (most cases) divide past leftover (roundup) into n and sum it to cap
    # leftover/n = 7.2 round up (8)
    # new cap = 38 + 8 = 46
    # 2, 46, 46, 46, 46       leftover = - 4
    # 0, 54, 4, 74, 954       sum = 1086

    # repeat step 2
    # new cap = 46 + 1 = 47
    # 2, 47, 47, 47, 47       leftover = 0
    # 0, 53, 3, 73, 953       sum = 1082

    leftover = new_budget - sum(grants)
    print('Initial Leftover: ' + str(leftover))
    if leftover < 0:
        return neg_leftover(grants, new_budget)
    else:
        return None


def neg_leftover(grants, new_budget):
    even_bud = new_budget / float(len(grants))
    cap = even_bud
    _grants = apply_cap_mask(grants, cap)
    n = len(grants)
    leftover = sum(_grants) - new_budget

    while leftover < 0:
        cap = cap + get_leftover_mean(leftover, n)
        _grants = apply_cap_mask(grants, cap)
        leftover = sum(_grants) - new_budget

    return round(cap, 2)

def get_leftover_mean(leftover, n):
    return abs(leftover) / float(n)


def apply_cap_mask(grants, cap):
    new_grants = []
    for n in grants:
        new_n = n if n < cap else cap
        new_grants.append(new_n)
    return new_grants

find_grants_cap([21,100,50,120,130,110], 140)