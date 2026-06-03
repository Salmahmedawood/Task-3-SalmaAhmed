import pandas as pd
import matplotlib.pyplot as plt

# Read thedataset
df= pd.read_excel("Cleaned_Data.xlsx")
print(df.head())

# Dataset info
print(df.info())

# count columns
print("Number of columns:", len(df.columns))

# Descriptive statistics
columns = ["Quantity", "UnitPrice", "TotalPrice", "ItemsInCart"]
for col in columns:
    print("\nColumn:", col)
    print("Mean:", df[col].mean())
    print("Median:", df[col].median())
    print("Count:", df[col].count())
    print("Minimum:", df[col].min())
    print("Maximum:", df[col].max())

# Date Conversion
df["Date"] = pd.to_datetime(df["Date"])

# Month extraction
df["Month"] = df["Date"].dt.month_name()
df["Month_Number"] = df["Date"].dt.month


# Monthly Sales
monthly_sales = df.groupby("Month")["TotalPrice"].sum().reset_index().sort_values("Month_Number")
print("\nMonthly Sales:")
print(monthly_sales)

## HIGHEST SALES MONTH ##
print(monthly_sales.sort_values(ascending=False).head(1))  


# PRODUCT PERFORMANCE ANALYSIS
product_sales = df.groupby("Product")["TotalPrice"].sum()
product_sales = product_sales.sort_values(ascending=False)
print(product_sales.head(5))




# OUTLIER DETECTION - USING IQR METHOD [IQR = Q3 - Q1] & [Upper Limit = Q3 + 1.5*IQR] & [Lower Limit = Q1 - 1.5*IQR]
Q1 = df["TotalPrice"].quantile(0.25)
Q3 = df["TotalPrice"].quantile(0.75)
IQR = Q3 - Q1
upper_limit = Q3 + (1.5 * IQR)
lower_limit = Q1 - (1.5 * IQR)
print("Upper Limit:", upper_limit)
print("Lower Limit:", lower_limit)

outliers = df[(df["TotalPrice"] > upper_limit) | (df["TotalPrice"] < lower_limit)]
print("Outliers:", outliers)

print("\nNumber of outliers:", len(outliers)) # 8 outliers detected 

# VISUALIZATION - SALES CHART
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.show()

# SAVE RESULTS TO EXCEL
monthly_sales.to_excel("Monthly_Sales.xlsx")
outliers.to_excel("Outliers.xlsx")

print("Analysis completed and results saved to Excel files.")

