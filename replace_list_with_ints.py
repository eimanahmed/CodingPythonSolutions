#Replace all the numbers spelled out with their integer values
my_list = [1, 2, "three", 4, 5, 6, "seven", "eight", "nine", 10]

for index in range(0, len(my_list)):
    if not (str(my_list[index]).isdigit()):
        current_word = my_list[index]
        match current_word:
            case "three":
                my_list[index] = 3
            case "seven":
                my_list[index] = 7
            case "eight":
                my_list[index] = 8
            case "nine":
                my_list[index] = 9

print(my_list)