# Mail Merge

## Introduction

The invitation generator is a Python program that prepares personalized invitations using a predefined format. It reads a list of names from a file, replaces a placeholder in a template letter with each name, and saves the personalized letters in a designated folder.

## Constants

The program uses the following constant:

- `PLACEHOLDER`: A string representing the placeholder in the template letter that will be replaced with each name.

## File Input

The program reads the list of names from the file `invited_names.txt` located in the `Input/Names` directory. Each name should be on a separate line.

## Template Letter

The program uses a template letter located in the file `starting_letter.txt` in the `Input/Letters` directory. The template letter contains the placeholder `[name]`, which will be replaced with each name from the list.

## Generating Invitations

The program performs the following steps to generate the personalized invitations:

1. It reads the list of names from the `invited_names.txt` file.
2. It reads the content of the template letter from the `starting_letter.txt` file.
3. For each name in the list:
   - It removes any leading or trailing whitespace from the name.
   - It creates a new letter by replacing the `[name]` placeholder in the template letter with the actual name.
   - It saves the new letter in a separate file named `letter_for_[name]` in the `Output/ReadyToSend` directory.
4. Once all invitations are generated and saved, it displays the message "Task Completed Successfully!!" to indicate that the process is finished.

## Conclusion

The invitation generator program automates the process of creating personalized invitations using a predefined format. By providing a list of names and a template letter, it generates individualized invitations by replacing a placeholder with each name. The program saves the generated invitations in a designated folder for easy access and distribution.