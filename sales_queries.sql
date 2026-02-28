-- Total Sales
SELECT SUM(Sales) AS Total_Sales FROM sales_data;

-- Sales by Product
SELECT Product, SUM(Sales) AS Total_Sales
FROM sales_data
GROUP BY Product;

-- Sales by Region
SELECT Region, SUM(Sales) AS Total_Sales
FROM sales_data
GROUP BY Region;

-- Daily Sales Trend
SELECT Date, SUM(Sales) AS Daily_Sales
FROM sales_data
GROUP BY Date
ORDER BY Date;
