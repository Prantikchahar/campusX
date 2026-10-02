### Q5:- Write a program to find the simple interest when the value of principle,rate of interest and time period is provided by the user.

# solution=====>>>

# Taking inputs from the user
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the annual rate of interest (in %): "))
time = float(input("Enter the time period (in years): "))

# Calculating simple interest
simple_interest = (principal * rate * time) / 100

# Displaying the result
print(f"\nThe calculated Simple Interest is: {simple_interest:.2f}")
