import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")
plt.rcParams['figure.figsize'] = (10, 6)

# Load the dataset
df = pd.read_csv("sales_data_project.csv")

print("\nSample Data:")
print(df.head())

print("Dataset Info:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())

print(df.describe())

# Remove duplicates
df.drop_duplicates(inplace=True)

print("\nMissing Values after removing duplicates:")
print(df.isnull().sum())

print(df['Region'].unique())
print(df['Product'].unique())

print(df['Region'].value_counts())
print(df['Product'].value_counts())

# Total Revenue by Region
region_revenue = df.groupby("Region")["Total Revenue"].sum().sort_values(ascending=False)
print("\nTotal Revenue by Region:")
print(region_revenue)

plt.figure(figsize=(8,5))
sns.barplot(x=region_revenue.index, y=region_revenue.values, palette="viridis")
plt.title("Total Revenue by Region")
plt.xlabel("Region")
plt.ylabel("Total Revenue")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Revenue Trend over Time
df["Date"] = pd.to_datetime(df["Date"])
df['YearMonth'] = df["Date"].dt.to_period("M")

monthly_revenue = df.groupby("YearMonth")["Total Revenue"].sum()
monthly_revenue = monthly_revenue.sort_index()
print("\nMonthly Total Revenue:")
print(monthly_revenue)

monthly_revenue.plot(kind='line', figsize=(10,5), marker='o')
plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Total Revenue")
plt.grid(True)
plt.tight_layout()
plt.show()

# Top 10 Products by Revenue
top_products = df.groupby("Product")["Total Revenue"].sum().sort_values(ascending=False).head(10)
print("\nTop 10 Products by Revenue:")
print(top_products)

plt.figure(figsize=(10,5))
sns.barplot(x=top_products.values, y=top_products.index, palette="mako")
plt.title("Top 10 Products by Total Revenue")
plt.xlabel("Total Revenue")
plt.ylabel("Product Name")
plt.tight_layout()
plt.show()

pivot_table = df.pivot_table(values="Total Revenue", index="Product", columns="Region", aggfunc="sum")
sns.heatmap(pivot_table, cmap="YlGnBu")
plt.title("Revenue by Product and Region")
plt.tight_layout()
plt.show()

df.to_csv("cleaned_sales_data.csv", index=False)

# Insights:
#- The East region generated the highest revenue, followed by West, South and North.
#- Product Laptop was the top sellers.

