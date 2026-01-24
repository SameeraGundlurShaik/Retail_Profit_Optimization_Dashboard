CREATE DATABASE IF NOT EXISTS retail_db;
USE retail_db;
USE retail_db;
SELECT COUNT(*) AS total_rows FROM clean_orders;
SELECT 
  Product_Name,
  SUM(Sales) AS total_sales,
  SUM(Profit) AS total_profit
FROM clean_orders
GROUP BY Product_Name
ORDER BY total_profit ASC
LIMIT 5;
SELECT 
  Category,
  Sub_Category,
  SUM(Sales) AS total_sales,
  SUM(Profit) AS total_profit
FROM clean_orders
GROUP BY Category, Sub_Category
ORDER BY total_profit ASC;
SELECT 
  discount_bucket,
  COUNT(*) AS total_orders,
  SUM(Sales) AS total_sales,
  SUM(Profit) AS total_profit
FROM clean_orders
GROUP BY discount_bucket
ORDER BY total_profit ASC;
SELECT 
  Product_Name,
  Sales,
  Discount,
  Profit,
  discount_bucket
FROM clean_orders
WHERE discount_bucket = 'High (>20%)'
ORDER BY Profit ASC;
SELECT 
  Category,
  SUM(Sales) AS total_sales,
  SUM(Profit) AS total_profit
FROM clean_orders
GROUP BY Category
ORDER BY total_profit DESC;
SELECT 
  Region,
  SUM(Sales) AS total_sales,
  SUM(Profit) AS total_profit
FROM clean_orders
GROUP BY Region
ORDER BY total_profit DESC;
SELECT 
  order_year,
  order_month,
  order_month_name,
  SUM(Sales) AS total_sales,
  SUM(Profit) AS total_profit
FROM clean_orders
GROUP BY order_year, order_month, order_month_name
ORDER BY order_year, order_month;
SELECT 
  Product_Name,
  SUM(Sales) AS total_sales,
  SUM(Profit) AS total_profit
FROM clean_orders
GROUP BY Product_Name
ORDER BY total_profit DESC
LIMIT 5;

