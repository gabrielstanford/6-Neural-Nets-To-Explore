import csv
import random
import datetime

# Define menu items
menu_items = [
    {"item": "Filet Mignon", "price": 45},
    {"item": "Lobster Thermidor", "price": 55},
    {"item": "Truffle Risotto", "price": 35},
    {"item": "Salmon en Papillote", "price": 30},
    {"item": "Duck Confit", "price": 40},
    {"item": "Foie Gras", "price": 50},
    {"item": "Creme Brulee", "price": 15},
    {"item": "Chocolate Souffle", "price": 20}
]

# Define days of the week
days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# Generate 10,000 rows of sales data
rows = []
for _ in range(10000):
    # Randomly select menu item
    item = random.choice(menu_items)
    
    # Generate random date and time
    date = datetime.datetime(2024, random.randint(1, 12), random.randint(1, 28))
    day_of_week = days_of_week[date.weekday()]
    time = datetime.time(random.randint(17, 21), random.randint(0, 59))
    
    # Generate price of item and waiter's tip
    price = item["price"]
    tip = round(random.uniform(0.1, 0.3) * price, 2)
    
    # Append to rows
    rows.append([date.strftime('%Y-%m-%d'), day_of_week, time.strftime('%H:%M'), item["item"], price, tip])

# Write data to CSV file
with open('restaurant_sales_data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Date', 'Day of Week', 'Time', 'Item', 'Price', 'Tip'])
    writer.writerows(rows)

print("Dataset generated successfully.")
