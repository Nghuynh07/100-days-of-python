# num_char = len(input("Hello there mate!"));
# new_num_char = str(num_char)
# print(type(new_num_char))
# print(num_char)


# 🚨 Don't change the code below 👇
# height = input("enter your height in m: ")
# weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# print(int(float(weight) / (float(height) * float(height))))

#        //= floor
# score = 0
# height = 1.85
# isWinning = True

# print(f"your scored is {score} and your height is {height} and you are not {isWinning}")
# age = input("What is your current age?")
# days = 365
# weeks = 52
# months = 12
# total = 90
# age_in_int = int(age)
# remaining_years = total - age_in_int

# days_left = remaining_years * days
# weeks_left = remaining_years * weeks
# months_left = remaining_years * months

# print(f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left.")

#print greeting 

print("Welcome to the tip calculator")
#What was the total bill?
total_bill = input("What was the total bill?")
#What percentage tip would you like to give? 10, 12, 15?
percentage_to_tip = input("What percentage tip would you like to give? 10, 12, or 15?")
#How many people to split the bill?
how_many_people_to_split = input("How many people to split the bill?")
#Each person should pay:

total_per_person = round((int(total_bill) * (1 + (int(percentage_to_tip)/100))) / int(how_many_people_to_split),2)

print(f"Each person should pay: ${total_per_person}")


##What did I learned today? I learned about float/int/round // as flooring numbers, I also learned about f-string