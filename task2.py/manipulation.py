str_manip = input("Enter a sentence: ")

str_length = len(str_manip)
print(str_length)

last_letter = str_manip[-1]
print(last_letter)

at_sentence = str_manip.replace(f"{last_letter}", "@")
print(at_sentence)

last_three_reversed = str_manip[ : -4 : -1]
print(last_three_reversed)

last_two = str_manip[-2 : ]
#print(last_two)

first_three = str_manip[ : 3]
#print(first_three)

print(f"{first_three}" + f"{last_two}")