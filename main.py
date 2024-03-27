
import clear

from art import logo

print(logo)

bids = {}
biding_finished = False
while not biding_finished:
    name = str(input("What is your name? "))
    bid_price = int(input("What is your bid price? $"))
    bids[name] = bid_price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no' ")
    if should_continue == "no":
        biding_finished = True

    elif should_continue == "yes":
        clear()

highest = 0
winner = ""
for i in bids:
    bid_amount = bids[i]
    if bid_amount > highest:
        highest = bid_amount
        winner = i

print(f"The winner is {winner} with a bid of ${highest}")