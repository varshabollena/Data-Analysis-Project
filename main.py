import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data/sales_data.csv")

print("===== SALES ANALYSIS =====")

# Total Revenue
total_revenue = df["Total_Sales"].sum()
print("Total Revenue:", total_revenue)

# Best selling product
best_product = df.groupby("Product")["Quantity"].sum().idxmax()
print("Best Selling Product:", best_product)


# -------- BAR CHART : SALES BY PRODUCT --------
product_sales = df.groupby("Product")["Total_Sales"].sum()

plt.figure()
product_sales.plot(kind="bar")

plt.title("Sales by Product")
plt.xlabel("Product")
plt.ylabel("Total Sales")

plt.savefig("visualizations/sales_by_product.png")
plt.show()


# -------- PIE CHART : SALES BY REGION --------
region_sales = df.groupby("Region")["Total_Sales"].sum()

plt.figure()
region_sales.plot(kind="pie", autopct="%1.1f%%")

plt.title("Sales Distribution by Region")
plt.ylabel("")

plt.savefig("visualizations/sales_by_region.png")
plt.show()