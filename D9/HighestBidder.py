import os
import highestBidderArt

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

def add_to_dictionary(bidder, bid):
    new_bidder = {
        bidder : bid,
    }
    return new_bidder

def max_bid(bid, current_max):
    if current_max >= bid: return current_max
    else: return bid
    


def start():
    bidder_name = input("What is your name?\n> ")
    bid_amount_str = input("What's your bid amount? (include $ sign)\n> ")
    # amount_list = list(bid_amount_str)

    temp_amt = ""
    for i in range(1, len(bid_amount_str)):
        temp_amt += bid_amount_str[i]

    bid = int(temp_amt)
    return add_to_dictionary(bidder_name, bid)
    

print(highestBidderArt.logo)
dict_list = []
dict_list.append(start())

while input("Is there another bidder?\n > ").lower() == "yes":
    clearConsole()
    dict_list.append(start())

max = 0
max_bidder = ""
for i in range(len(dict_list)):
    for bidder in dict_list[i]:
        current_max = max_bid(dict_list[i][bidder], max)
        if max < current_max:
            max = current_max
            max_bidder = bidder


print(f"The highest bid was {max} which was placed by {max_bidder}")