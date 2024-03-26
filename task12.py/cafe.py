menu = ['sandwich', 'pizza', 'burger', 'fries']
stock = {'sandwich':10, 'pizza':12, 'burger':21, 'fries':35}   
price = {'sandwich': 5, 'pizza': 8, 'burger': 10, 'fries': 3}

total_stock_value = 0
for food_item in menu:
  quantity = stock[food_item]
  item_price = price[food_item]
  total_stock_value += quantity * item_price
  
print(total_stock_value)











