# Will create 4 separate input functions then invoke them all in a print command with the proper spacing and text between

name = input("Please enter your name: ")

age = input("Please enter your age: ")

house_number = input("Please enter your house number: ")

street_name = input("Please enter your street name: ")

sentence = "This is " + name + ". He is " + age + " years old and lives at house number " + house_number + " on " + street_name + "."

print(sentence)