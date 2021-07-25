def calc_tax(u_income, percent):
    print(f'The tax for {u_income} is {percent}%. '
          f'That is {int(round(((percent / 100) * u_income), 0))} dollars!')


user_income = int(input())
if 0 < user_income <= 15527:
    calc_tax(user_income, 0)
elif 15528 <= user_income <= 42707:
    calc_tax(user_income, 15)
elif 42708 <= user_income <= 132406:
    calc_tax(user_income, 25)
elif user_income >= 132407:
    calc_tax(user_income, 28)
else:
    print('Wrong input data')
