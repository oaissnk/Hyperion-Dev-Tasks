# Constants
COST_PER_NIGHT = 100  
DAILY_RATE = 30

# Function definitions

def get_city():
    city = input("Enter city: ")
    if not city:
        raise ValueError("City is required")
    return city.title()

def get_nights():
    while True:
        num_nights = input("Enter number of nights: ")
        if num_nights.isdigit():
            return int(num_nights)
        else:
            print("Please enter a valid number.")
            
def get_rental_days():
    while True:
        days = input("Enter rental days: ") 
        if days.isdigit():
            return int(days)
        else:
            print("Please enter a valid number.")
            
def hotel_cost(nights):
    return nights * COST_PER_NIGHT
    
def plane_cost(city):
  if city == "London":
    cost = 400
  elif city == "Birmingham":
    cost = 300
  elif city == "Newcastle":
    cost = 330
  elif city == "Manchester":
    cost = 350

    return cost

def rental_cost(days):
    return days * DAILY_RATE
    
def holiday_cost():
    city = get_city()
    nights = get_nights()
    days = get_rental_days()
    
    # Calculate costs
    total = hotel_cost(nights) + plane_cost(city) + rental_cost(days)
    
    return total

# Main
trip_cost = holiday_cost()
print(f"Total cost: {trip_cost}")


