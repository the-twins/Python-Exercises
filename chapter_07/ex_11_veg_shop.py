def print_menu():
    """Print the menu."""
    print("Choose your category to enter the pounds (q to quit):")
    print("a) Artichoke $2.05")
    print("b) Beet      $1.15")
    print("c) Carrot    $1.09")
    
    
ARTICHOKE = 2.05
BEET = 1.15
CARROT = 1.09
DISCOUNT = 0.05
OVER = 100
RATE1 = 6.5
RATE2 = 14.0
RATE3 = 0.5
BREAK1 = 5
BREAK2 = 20
MIN_PRICE = 0.01
artichoke = 0.0
beet = 0.0
carrot = 0.0
cost_a = 0 
cost_b = 0
cost_c = 0
delivery = 0
discount = 0
while True:
    print_menu()
    order = input()
    match order:
        case 'a':
            print("Enter weight in pounds:")
            artichoke += float(input())
        case 'b':
            print("Enter weight in pounds:")
            beet += float(input())
        case 'c':
            print("Enter weight in pounds:")
            carrot += float(input())
        case 'q':
            break
        case _:  # This is the default case
            print(f'Unknown category: {order}. Try again:')
            continue
all_pound = artichoke + beet + carrot
if(all_pound < MIN_PRICE):
    print("Order is cancelled. Bye!")
else:
    cost_a = artichoke * ARTICHOKE
    cost_b = beet * BEET
    cost_c = carrot * CARROT
    all_cost = cost_a + cost_b + cost_c
    if(all_cost >= OVER):
        discount = all_cost * DISCOUNT
    if(all_pound <= BREAK1):
        delivery = RATE1
    elif(all_pound <= BREAK2):
        delivery = RATE2
    else:
        delivery = RATE2 + ((int(all_pound - BREAK2)) * RATE3)
    print("Item        Amount      Price      Total")
    print("---------------------------------------------")
    print("Artichokes  ", artichoke, "     ", ARTICHOKE, "     ", round(cost_a, 2))
    print("Beets       ", beet, "     ", BEET, "     ", round(cost_b, 2))
    print("Carrots     ", carrot, "     ", CARROT, "     ", round(cost_c, 2))
    print("---------------------------------------------")
    print("            ", all_pound, "               ", all_cost)
    print("*********************************************")
    print("                         Discount: $", round(discount, 2))
    print("              Total with discount: $", round((all_cost - discount), 2))
    print("---------------------------------------------")
    print("                         Shipment: $", delivery)
    print("                      Grand total: $", round((all_cost + delivery - discount), 2))
