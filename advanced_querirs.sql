-- Monthly Revenue + Growth %
WITH monthly AS (
    SELECT 
        strftime('%Y-%m', order_date) AS month,
        SUM(quantity * price) AS revenue
    FROM sales
    GROUP BY month
)
SELECT 
    month,
    revenue,
    LAG(revenue) OVER (ORDER BY month) AS prev_revenue,
    ROUND(
        (revenue - LAG(revenue) OVER (ORDER BY month)) * 100.0 
        / LAG(revenue) OVER (ORDER BY month), 2
    ) AS growth_percent
FROM monthly;

-- Top Products Ranking
SELECT 
    product,
    SUM(quantity * price) AS revenue,
    RANK() OVER (ORDER BY SUM(quantity * price) DESC) AS rank
FROM sales
GROUP BY product;

-- Running Revenue
SELECT 
    order_date,
    SUM(quantity * price) AS daily_revenue,
    SUM(SUM(quantity * price)) OVER (ORDER BY order_date) AS running_total
FROM sales
GROUP BY order_date;

-- Average Order Value
SELECT 
    SUM(quantity * price) * 1.0 / COUNT(DISTINCT order_id) AS AOV
FROM sales;