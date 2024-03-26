# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

print("Welcome to the error program")
print("\n")

    # Variables declaring the user's age, casting the str to an int, and printing the result
age_Str = "24 years old" 
age_num = age_Str.split(' ')[0]
age = int(age_num) 
print("I'm " + str(age) + " years old.")

    # Variables declaring additional years and printing the total years of age
years_from_now = "3"
years_from_now = int(years_from_now)    
total_years = age + years_from_now

print("The total number of years: " + str(total_years))

# Variable to calculate the total amount of months from the total amount of years and printing the result
total_months = (total_years * 12) + 6
print("In " + str(years_from_now) + " years and 6 months, I'll be " + str(total_months) + " months old")

#HINT, 330 months is the correct answer

