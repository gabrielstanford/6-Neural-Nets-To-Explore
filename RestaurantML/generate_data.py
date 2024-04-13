import csv
import random
from datetime import datetime, timedelta

# Function to generate random date and time in March 2024
def generate_datetime():
    start_date = datetime(2024, 3, 1)
    end_date = datetime(2024, 3, 31)
    delta = end_date - start_date
    random_date = start_date + timedelta(days=random.randint(0, delta.days))
    random_time = random_time = random.randint(11, 21), random.randint(0, 59)
    return random_date.strftime('%Y-%m-%d'), f"{random_time[0]}:{random_time[1]}"

# Function to generate random day of week
def generate_day_of_week(date):
    return datetime.strptime(date, '%Y-%m-%d').strftime('%A')

# Function to generate random item sold
def generate_item():
    items = ['Burger', 'Pizza', 'Salad', 'Pasta', 'Sandwich', 'Steak', 'Soup', 'Sushi', 'Tacos', 'Ramen']
    return random.choice(items)

# Function to generate random price in the range of $10-$50
def generate_price():
    return round(random.uniform(10, 50), 2)

# Function to generate random tip (15-25% of item price)
def generate_tip(price):
    return round(random.uniform(0.15, 0.25) * price, 2)

# Function to generate random cost to produce the item
def generate_cost():
    return round(random.uniform(3, 15), 2)

# Function to generate random server name
def generate_server():
    servers = ['Alice', 'Bob', 'Charlie', 'David', 'Emma', 'Frank', 'Grace', 'Henry', 'Ivy', 'Jack']
    return random.choice(servers)

# Generate 10,000 rows of data
data = []
for _ in range(10000):
    date, time = generate_datetime()
    day_of_week = generate_day_of_week(date)
    item = generate_item()
    price = generate_price()
    tip = generate_tip(price)
    cost = generate_cost()
    server = generate_server()
    data.append([date, time, day_of_week, item, price, tip, cost, server])

# Write data to a .csv file
with open('restaurant_orders.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Date', 'Time', 'Day of Week', 'Item', 'Price', 'Tip', 'Cost', 'Server'])
    writer.writerows(data)

print("Dataset generated successfully!")