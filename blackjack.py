def blackjack(num1,num2,num3):
    for11 = False
    if sum((num1,num2,num3)) <= 21:
        print(sum((num1,num2,num3)))
    elif sum((num1,num2,num3)) > 21 and 11 in (num1,num2,num3):
        print(sum((num1,num2,num3))-10)
    else:
        print('BUST')
blackjack(5,6,7)

