import string
import CypherArt

def encode(message, key):
    for i in range(len(message)):
        value_of_char = ord(message[i])
        value_of_char += key
        message[i] = chr(value_of_char)

    return message

def decode(message, key):
    for i in range(len(message)):
        value_of_char = ord(message[i])
        value_of_char -= key
        message[i] = chr(value_of_char)

    return message

def if_encode():
    message = input("What would you like to encode?\n> ").lower()
    encoded_value = int(input("Encoding Key\n> ")) % 26

    msg_list = []
    for i in range(len(message)):
        msg_list.append(message[i])

    encoded_msg = encode(msg_list, encoded_value)
    print("Your encoded message is: " + ''.join([str(i) for i in encoded_msg]))

def if_decode():
    message = input("What would you like to decode?\n> ").lower()
    encoded_value = int(input("Decoding Key\n> ")) % 26

    msg_list = []
    for i in range(len(message)):
        msg_list.append(message[i])

    decoded_msg = decode(msg_list, encoded_value)
    print("Your decoded message is: " + ''.join([str(i) for i in decoded_msg]))

# essentially the main function
print(CypherArt.logo)
restart = True
while restart:
    choice = input('Would you like to encode or decode a message? Type "encode" or "decode"\n> ').lower()
    if choice == "encode":
        if_encode()
    elif choice == "decode":
        if_decode()
    else:
        print("Your input is invalid")

    if input('Would you like to run the program again?\nType "Yes" to restart and "No" to end the program\n> ').lower() == "no":
        restart = False



