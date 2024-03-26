swimming = int(input("Please enter your swimming time in minutes: "))
cycling = int(input("Please enter your cycling time in minutes: "))
running = int(input("Please enter your running time in minutes: "))
total_time = swimming + cycling + running
print(total_time)

if(total_time <= 100):
    print ("Provincial Colours")
elif(total_time >= 101)  and (total_time <= 105):
    print ("Provincial Half Colours")
elif(total_time >= 106)  and (total_time <= 110):
    print ("Provincial Scroll")
else:print ("No award")

#had to set up the varibles with an input of whole integers as its in minutes
#i shortened the 3 inputs into 1 variable to keep it neat 
# did an if/elif/else conditional to print the correct reward to total time
# had to use and statement when 2 conditions had to be met 