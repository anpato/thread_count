from os import sep
from string import daily_sales


def replaceChar(char, seperator, str):
    return str.replace(char, seperator)


special_char = "#"
daily_sales_replaced = replaceChar(';,;', special_char, daily_sales)

daily_transactions = daily_sales_replaced.split(",")

daily_transactions_clean = list()

transaction_dict = {
    "customers": list(),
    "sales": list(),
    "thread_sold": list()
}

for transaction in daily_transactions:
    transaction_items = transaction.split(special_char)
    for i, t in enumerate(transaction_items):
        transaction_items[i] = t.strip()
    daily_transactions_clean.append(transaction_items)

for transaction in daily_transactions_clean:
    transaction_dict["customers"].append(transaction[0])
    transaction_dict["sales"].append(transaction[1])
    start_index = 2
    end_index = 0
    for t in transaction:
        if "&" in t:
            transaction_dict["thread_sold"].append(t)
            end_index = transaction.index(t)
        elif "/"in t:
            end_index = transaction.index(t)-1
            transaction_dict["thread_sold"].append(transaction[end_index])
total_sales = 0

for price in transaction_dict['sales']:
    price_stripped = price.strip("$")
    total_sales += float(price_stripped)

thread_sold_split = list()

for color in transaction_dict["thread_sold"]:
    if "&" in color:
        thread_sold_split = [*thread_sold_split, * color.split("&")]
    else:
        thread_sold_split.append(color)

colors = list()


def color_count(colors):
    has_color_dict = {}
    for color in colors:
        if has_color_dict.get(color):
            has_color_dict[color] += 1
        else:
            has_color_dict.setdefault(color, 1)
    return has_color_dict


color_lookup = color_count(thread_sold_split)


def get_color_count(color, c_dict):
    return c_dict[color]


for color in thread_sold_split:
    print("{} was sold {} times today.".format(
        color.title(), color_lookup[color]))
