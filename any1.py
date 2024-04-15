current_pizza, replace_amount = map(int, input().split())

def get_plus_pizza(current_pizza_coupon):
    plus_pizza = current_pizza_coupon // replace_amount
    if plus_pizza == 0:
        return 0

    return plus_pizza + get_plus_pizza(plus_pizza + current_pizza_coupon % replace_amount)



print(current_pizza + get_plus_pizza(current_pizza))