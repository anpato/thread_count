from os import sep
from string import daily_sales


def replaceChar(char, seperator, str):
    return str.replace(char, seperator)


special_char = "&"
daily_sales_replaced = replaceChar(';,;', special_char, daily_sales)
# print(daily_sales_replaced)

daily_transactions = daily_sales_replaced.split(",")
# print(daily_transactions)

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

# print(daily_transactions_clean)

for transaction in daily_transactions_clean:
    transaction_dict["customers"].append(transaction[0])
    transaction_dict["sales"].append(transaction[1])
    start_index = 2
    end_index = 0
    for t in transaction:
        if "/" in t:
            end_index = transaction.index(t)
    colors = transaction[start_index:end_index]
    transaction_dict["thread_sold"].append(colors)

# print(transaction_dict)
total_sales = 0

for price in transaction_dict['sales']:
    price_stripped = price.strip("$")
    total_sales += float(price_stripped)
