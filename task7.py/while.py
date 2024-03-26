menu = '''

Hello, this is an averaging machine. It will take numbers as input and calculate a running average for you.

'''

print(menu)

count = 0
numbers = []

while True:

  number = input("Enter a number (or '-1' to quit): ")

  if number == '-1':
    print("We're finished!")
    break

  try:
    number = int(number)
  except ValueError: 
    print("Invalid input. Please enter a valid number or '-1' to quit.")
    continue

  if number != -1:
    count += number
    numbers.append(number)

    average = count / len(numbers)
    print(f"Current average: {average}")







   




   