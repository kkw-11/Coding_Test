def solution(price, money, count):
    answer = 0
    total = 0
    for i in range(1,count+1):
        total += price*i
    if total - money >=0:
        return total - money
    else:
        return 0