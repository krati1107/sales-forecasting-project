import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv('../data/sales_data.csv')

# Convert Date column
df['Date'] = pd.to_datetime(df['Date'])

# Sort values
df = df.sort_values('Date')

# Total sales
print("Total Sales:", df['Sales'].sum())

# Sales by product
product_sales = df.groupby('Product')['Sales'].sum()
print("\nSales by Product:\n", product_sales)

# Sales by region
region_sales = df.groupby('Region')['Sales'].sum()
print("\nSales by Region:\n", region_sales)

# Time series plot
df.set_index('Date', inplace=True)
df['Sales'].plot(title="Sales Trend")
plt.show()

# Simple Forecast (Moving Average)
df['Forecast'] = df['Sales'].rolling(window=3).mean()

df[['Sales', 'Forecast']].plot(title="Sales Forecast")
plt.show()
