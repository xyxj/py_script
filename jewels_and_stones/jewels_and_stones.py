J = "aA"
S = "aAAbbbb"


def jewels_and_stones():
    count = 0
    for x in J:
        count += S.count(x)
    return count


print jewels_and_stones()
