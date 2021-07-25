user_money = int(input())
if user_money < 23:
    print('None')
elif 23 <= user_money < 46:
    print('1 chicken')
elif 46 <= user_money < 678:
    print(f"{user_money // 23} chickens")
elif 678 <= user_money < 1296:
    print('1 goat')
elif 1296 <= user_money < 2592:
    print('1 pig')
elif 2592 <= user_money < 3848:
    print('2 pigs')
elif 3848 <= user_money < 6769:
    print('1 cow')
else:
    print(f"{user_money // 6769} sheep")
