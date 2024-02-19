import random
user_input = int(input("Choose an option one through ten to get a problem you want to run. "))

if user_input == 1:
    for count in range(1, 1001):
        print(count)
elif user_input == 2:
    for count in range(1, 1001):
        if count % 2 != 0:
            print(count)
elif user_input == 3:
    for count in range(1, 1001):
        if count % 3 == 0:
            print(count)
elif user_input == 4:
    for count in range(1, 1001):
        if count % 3 == 0 or count % 5 == 0:
            print(count)
elif user_input == 5:
    user_number = int(input("Enter a number greater than 200. "))
    while user_number < 200:
        user_number = int(input("Please enter a number greater than 200! "))
    for count in range(1, user_number):
        if count % 11 == 0 or count % 13 == 0:
            print(count)
elif user_input == 6:
        string = "Hello World!"
        for count in range(0, len(string)):
            print(string[count])
elif user_input == 7:
    string = "Hello World! How are you doing?"
    for count in range(0, len(string), 2):
        print(string[count])
elif user_input == 8:
    one_rolls = 0
    two_rolls = 0
    three_rolls = 0
    four_rolls = 0
    five_rolls = 0
    six_rolls = 0
    for e in range(1000):
        dice_roll = random.randint(1,6)
        if dice_roll == 1:
            one_rolls = one_rolls + 1
        elif dice_roll == 2:
            two_rolls = two_rolls + 1
        elif dice_roll == 3:
            three_rolls = three_rolls + 1
        elif dice_roll == 4:
            four_rolls = four_rolls + 1
        elif dice_roll == 5:
            five_rolls = five_rolls + 1
        elif dice_roll == 6:
            six_rolls = six_rolls + 1

    print(f"Total one rolls: {one_rolls}")
    print(f"Total two rolls: {two_rolls}")
    print(f"Total three rolls: {three_rolls}")
    print(f"Total four rolls: {four_rolls}")
    print(f"Total five rolls: {five_rolls}")
    print(f"Total six rolls: {six_rolls}")
elif user_input == 9:
        user_number = int(input("Please put a number "))
        if user_number <= 1:
            print(f"{user_number} is not a prime number. ")
        elif user_number == 2:
            print(f"{user_number} is a prime number. ")
        elif user_number > 1:
            for prime in range(2, user_number):
                if user_number % prime == 0:
                    print(f"{user_number} is not a prime number.")
                    break
                else:
                    print(f"{user_number} is a prime number.")
                    break
elif user_input == 10:
    for index in range(1, 1001):
        if index <= 1:
            continue
        elif index == 2:
            print(index)
        else:
            is_prime = True
            for prime in range(2, index):   
                if index % prime == 0:
                    is_prime = False
                    break
            if is_prime == True:
                print(index)
                
                    
        
            
        

    

