sum = 0
count = 0

while True:
    user_input = input("Please enter each of your grades to calculate your average. When you are done, enter 'q'")
    if user_input == 'q':
        break
    sum += int(user_input)
    count += 1

print(sum/count)
    