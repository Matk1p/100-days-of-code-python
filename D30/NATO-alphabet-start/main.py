import pandas

nato_data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (index, row) in nato_data.iterrows()}

input_invalid = True


def get_user_input():
    user_input = input("Enter a word: ").upper()
    try:
        phonetic_list = [nato_dict[letter] for letter in user_input]
    except KeyError:
        print("Only letters from the alphabet please")
        get_user_input()
    else:
        print(phonetic_list)


get_user_input()
