def print_price_list(name):
    print('Prices:')
    for key, value in name.items():
        print(f'{key}: ${value:.2f}')

def print_month_earnings(name):
    print('Earned amount:')
    for key, value in name.items():
        print(f'{key}: ${value:.2f}')

    total_data['Total income'] = sum(name.values())
    print(f"\nIncome: ${total_data['Total income']:.2f}")

def get_expenses(name):
    name['Staff expenses'] = int(input('Enter staff expenses:\n'))
    name['Other expenses'] = int(input('Enter other expenses:\n'))
    total_data['Total expenses'] = sum(name.values())

base_price_list = {'Bubblegum' : 2,
               'Toffee' : 0.2,
               'Ice cream' : 5,
               'Milk chocolate' : 4,
               'Doughnut' : 2.5,
               'Pancake' : 3.2}

month_earnings = {'Bubblegum' : 202,
               'Toffee' : 118,
               'Ice cream' : 2250,
               'Milk chocolate' : 1680,
               'Doughnut' : 1075,
               'Pancake' : 80}

month_expenses = {'Staff expenses' : int,
               'Other expenses' : int }

total_data = {}

# print_price_list(base_price_list)
print_month_earnings(month_earnings)
get_expenses(month_expenses)
net_income = total_data['Total income'] - total_data['Total expenses']
print(f'Net income: ${net_income:.2f}')