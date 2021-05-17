import os

print("Welcome to secret auction")

bid_entry = {}
continue_bidding = True


def find_highest_bidder(bidding_record):
    highest_bid = 0
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {bidder} with a bid of ${highest_bid}")


while continue_bidding:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    bid_entry[name] = bid
    choice = input("Are there any other bidders? Type 'yes' or 'no'")

    if choice == "no":
        continue_bidding = False
        find_highest_bidder(bid_entry)
    elif choice == "yes":
        # clear screan
        os.system('cls')
