import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
letter_dict = {row.letter: row.code for (index, row) in data.iterrows()}

while True:
    name = input("Enter the Word : ").upper()
    try:
        res = [letter_dict[letter] for letter in name]
    except KeyError:
        print("Sorry! Only Letters in the Alphabet are allowed.")
    else:
        print(res)
        break
