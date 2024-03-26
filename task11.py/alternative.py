text = input("Enter a string: ")

result = ""
for i, char in enumerate(text):
  if i % 2 == 0:
    result += char.upper()
  else:
    result += char.lower()

print(result)


input_str = input("Enter a string: ")

words = input_str.split()
output_str = ""
for i in range(len(words)):
    if i % 2 == 0:
        output_str += words[i].lower() + " "
    else: 
        output_str += words[i].upper() + " "

print(output_str)


# there is a way I can use the join method but would have to use to store every second word in a list and then join them together. Which doesn't seem effective for this task. Let me know what you think please :)

''' Unfortunately, your solution does not meet the requirements for this task. The second part of the task requires you to write a code that will alternate words like " THIS is AN example".

Currently, your code only prints out alternating letters. You can achieve the objective of the second part by applying the same idea as you did in the first part to words instead of characters and using the join() function as well. 

This is the feedback I got for my task submission but my code does change every alternate word to uppercase so I am really confused...can you please try the programme again'''