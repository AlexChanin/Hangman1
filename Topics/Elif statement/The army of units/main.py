units_amount = int(input())
if units_amount < 1:
    print('no army')
elif 1 <= units_amount <= 9:
    print('few')
elif 10 <= units_amount <= 49:
    print('pack')
elif 50 <= units_amount <= 499:
    print('horde')
elif 500 <= units_amount <= 999:
    print('swarm')
elif units_amount >= 1000:
    print('legion')
else:
    print("You've inserted a not correct number")
