sum = 0
count = 0

while True:
    user_input = input("Please enter each of your grades to calculate your average. When you are done, enter 'q': ")
    if user_input == 'q':
        break
    if user_input.isdigit():
        sum += float(user_input)
        count += 1
    else:
        print("Hmm that wasn't a number. Try again.")
if count > 1:
    print(f"Your grade point average is {sum/count}")
    