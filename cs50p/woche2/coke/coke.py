#coke machine
#Amount Due: 50
#Insert Coin: 25
#Amount Due: 25
#Insert Coin: 10
#Amount Due: 15
#Insert Coin: 5
#Amount Due: 10
#Insert Coin: 25
#Change Owed: 15



def main():
    amount_due = 50
    while amount_due > 0:
        print("Amount Due:", amount_due)
        coin = int(input("Insert Coin: "))
        if coin in [25, 10, 5]:
            amount_due -= coin
    print("Change Owed:", -amount_due)

main()



