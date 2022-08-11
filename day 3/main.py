# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))
# bill = 0;
# if height >= 120:
#     print("You can use the roller coaster")
#     age = int(input("What is your age? "))
#     if age < 12:
#         bill = 5
#         print("Child tickets are $5.")
#     elif age > 18:
#         bill = 12
#         print("Adult tickets are $12")
#     elif age >=45 and age <=55:
#         print("Your ride is free!")
#     else:
#         bill = 7
#         print("Youth tickets are $7")
        
#     wants_photo = input("Do you want a photo take ? Y or N.")
#     if wants_photo == 'Y':
#         bill+=3
    
#     print(f"Your final bill is ${bill}")
    
# else:
#     print("You are not allowed to ride because you too short")


# 🚨 Don't change the code below 👇
# print("Welcome to the Love Calculator!")
# name1 = input("What is your name? \n")
# name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# total = 0
# true_count = 0
# love_count = 0
# lower_case_name2 = name2.lower()
# lower_case_name1 = name1.lower()


# true_count+=lower_case_name1.count("t")
# true_count+=lower_case_name1.count("r")
# true_count+=lower_case_name1.count("u")
# true_count+=lower_case_name1.count("e")
# true_count+=lower_case_name2.count("t")
# true_count+=lower_case_name2.count("r")
# true_count+=lower_case_name2.count("u")
# true_count+=lower_case_name2.count("e")

# love_count+=lower_case_name1.count("l")
# love_count+=lower_case_name1.count("o")
# love_count+=lower_case_name1.count("v")
# love_count+=lower_case_name1.count("e")
# love_count+=lower_case_name2.count("l")
# love_count+=lower_case_name2.count("o")
# love_count+=lower_case_name2.count("v")
# love_count+=lower_case_name2.count("e")

# total = int(str(true_count) + str(love_count))

# if total < 10:
#     print(f"Your score is {total}, you go together like coke and mentos.")
# elif total > 90:
#     print(f"Your score is {total}, you go together like coke and mentos.")
# elif total > 39 and total < 51:
#     print(f"Your score is {total},you are alright together")
# else:
#     print(f"Your score is {total}")

print("Welcome to the Treasure Island. Your mission is to find the treasure.")
two_paths = input("There are two paths in front of you. Which path will you take? Left or Right?").lower().capitalize()


if two_paths == "Left":
    print("Game over")
else:
    print("You went left. Now you safe, but now you need to decide which route to take.")
    two_routes = input("Would you rather 'Swim' or 'Wait'?").lower()
    if two_routes == 'wait':
        print("You are safe, but you must choose which color door to go through. Blue or Red door?")
        two_doors = input("Blue or Red door?").lower()
        if two_doors == "red":
            print("Game over. You went to a fire door")
        else:
            print("You passed the game. The blue door gave you some cold, but you survived!")
    else:
        print("You decided to swim, but a shark was waiting for you to jump in. Game is over!")
