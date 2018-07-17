def less_num(num1,num2):
    if num1%2 ==0 and num2%2 == 0:
        return  min(num1,num2)
    else:
        return  max(num1,num2)
print(less_num(2,5))