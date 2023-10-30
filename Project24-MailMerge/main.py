PLACEHOLDER = "[name]"

# for each name in invited_names.txt
with open("Input/Names/invited_names.txt") as name_file:
    names = name_file.readlines()

# Replace the [name] placeholder with the actual name.
with open("Input/Letters/starting_letter.txt") as letter_file:
    letter_content = letter_file.read()
    for name in names:
        name = name.strip()
        new_letter_content = letter_content.replace(PLACEHOLDER, name)

# Save the letters in the folder "ReadyToSend".
        with open(f"Output/ReadyToSend/letter_for_{name}", mode="w") as final_letter:
            final_letter.write(new_letter_content)
print("Task Completely Successfully!!")
