def is_regex_same_as_input(regex, char):
    if len(regex) == 0:
        print(True)
    elif len(char) == 0:
        print(False)
    else:
        if regex == '.':
            print(True)
        elif regex == char:
            print(True)
        else:
            print(False)


compare_characters = input()
if '|' in compare_characters:
    compare_characters = compare_characters.split('|')
else:
    print("You are missing delimiter |")
    quit()

is_regex_same_as_input(compare_characters[0], compare_characters[1])
