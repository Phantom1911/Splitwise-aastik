def divide_amount_in_equal_share(total_amount, divider):
    share = []
    while divider > 0:
        share_amount = round(total_amount/divider, 2)   # round to 2 places
        total_amount -= share_amount   # 1000 -250 = 750
        share.append(share_amount)
        divider -= 1
    return share


def divide_amount_by_percent_share(total_amount, percent_share):
    share = []
    for percent in percent_share:
        share_amount = round((percent/100) * total_amount, 2)
        share.append(share_amount)
    return share


def divide_amount_by_exact_share(total_amount, exact_share):
    share = []
    for exact in exact_share:
        share.append(exact)
    return share

