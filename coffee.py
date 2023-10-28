x=50
while x>0:
    print(f"Нужная сумма: {x}")
    coin = int(input("Вставьте монету: "))
    if coin==50 or coin==20 or coin==10 or coin==5:
        x=x-coin
print(f"Ваша сдача: {-1*x}")