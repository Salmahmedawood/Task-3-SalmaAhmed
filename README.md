# SQL Data Analysis Project

## Overview

This project demonstrates the use of SQL to analyze a sales dataset and extract meaningful business insights.

## Objectives

- Use SQL queries to explore and analyze data.
- Practice filtering, sorting, grouping, and aggregation.
- Generate insights from transactional sales data.

## Tools Used

- SQLite
- VS Code
- Python

## Dataset

The dataset contains sales transaction records including:

- Product information
- Quantity purchased
- Unit price
- Total price
- Order date
- Payment method

## SQL Concepts Demonstrated

### SELECT
Retrieve records from the dataset.

### WHERE
Filter records based on conditions.

### ORDER BY
Sort records in ascending and descending order.

### GROUP BY
Group records for summarized analysis.

### Aggregation Functions

- COUNT()
- SUM()
- AVG()

## Queries Performed

### Total Orders

```sql
SELECT COUNT(*) AS TotalOrders
FROM sales_data;
```

### Average Order Value

```sql
SELECT AVG(TotalPrice) AS AverageOrderValue
FROM sales_data;
```

### Total Revenue

```sql
SELECT SUM(TotalPrice) AS TotalRevenue
FROM sales_data;
```

### Revenue by Product

```sql
SELECT Product,
       SUM(TotalPrice) AS Revenue
FROM sales_data
GROUP BY Product
ORDER BY Revenue DESC;
```

## Key Insights

- Identified the highest revenue-generating products.
- Calculated total sales revenue.
- Determined average customer order value.
- Analyzed purchasing patterns using SQL aggregations.

