# 그리디 - 거스름돈 문제
coins = [500, 100, 50, 10]

def min_coin_count(money, coins):
    count = 0
    for coin in coins:
        count += (money // coin)
        money %= coin
    return count

print(min_coin_count(4720, coins)) # 31



