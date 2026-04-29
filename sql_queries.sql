-- ================================================================
--   E-COMMERCE DELIVERY DELAY ANALYSIS
--   SQL Queries — Exact queries used in this project
--   Dataset : ecommerce_orders (5,000 rows)
--   Period  : Jan – Dec 2023
--   Tool    : MySQL 8.0+
-- ================================================================


-- ────────────────────────────────────────────────────────────────
-- STEP 1 : DATA PREPARATION
--          Create Delivery_Days and Delivery_Status columns
-- ────────────────────────────────────────────────────────────────

ALTER TABLE ecommerce_orders
    ADD COLUMN Delivery_Days   INT,
    ADD COLUMN Delivery_Status VARCHAR(10);

UPDATE ecommerce_orders
SET
    Delivery_Days   = DATEDIFF(Delivery_Date, Order_Date),
    Delivery_Status = CASE
                          WHEN DATEDIFF(Delivery_Date, Order_Date) > 5
                          THEN 'Delayed'
                          ELSE 'On-Time'
                      END;

-- Verify the update
SELECT Delivery_Days, Delivery_Status, COUNT(*) AS Count
FROM ecommerce_orders
GROUP BY Delivery_Days, Delivery_Status
ORDER BY Delivery_Days;


-- ================================================================
-- QUERY 1 : OVERALL DELAY PERCENTAGE
-- ================================================================

SELECT
    COUNT(*)                                                          AS Total_Orders,
    SUM(CASE WHEN Delivery_Status = 'Delayed' THEN 1 ELSE 0 END)     AS Delayed_Orders,
    SUM(CASE WHEN Delivery_Status = 'On-Time' THEN 1 ELSE 0 END)     AS OnTime_Orders,
    ROUND(
        100.0 * SUM(CASE WHEN Delivery_Status = 'Delayed' THEN 1 ELSE 0 END)
        / COUNT(*), 2
    )                                                                 AS Delay_Pct
FROM ecommerce_orders;

/*
ACTUAL RESULT:
Total_Orders | Delayed_Orders | OnTime_Orders | Delay_Pct
5000         | 2476           | 2524          | 49.52%
*/


-- ================================================================
-- QUERY 2 : DELAY % BY REGION
-- ================================================================

SELECT
    Region,
    COUNT(*)                                                          AS Total_Orders,
    SUM(CASE WHEN Delivery_Status = 'Delayed' THEN 1 ELSE 0 END)     AS Delayed_Orders,
    ROUND(
        100.0 * SUM(CASE WHEN Delivery_Status = 'Delayed' THEN 1 ELSE 0 END)
        / COUNT(*), 2
    )                                                                 AS Delay_Pct
FROM ecommerce_orders
GROUP BY Region
ORDER BY Delay_Pct DESC;

/*
ACTUAL RESULT:
Region | Total_Orders | Delayed_Orders | Delay_Pct
North  | 1313         | 732            | 55.75%
East   | 1292         | 659            | 51.01%
South  | 1220         | 581            | 47.62%
West   | 1175         | 504            | 42.89%
*/


-- ================================================================
-- QUERY 3 : DELAY % BY COURIER PARTNER
-- ================================================================

SELECT
    Courier_Partner,
    COUNT(*)                                                          AS Total_Orders,
    SUM(CASE WHEN Delivery_Status = 'Delayed' THEN 1 ELSE 0 END)     AS Delayed_Orders,
    ROUND(
        100.0 * SUM(CASE WHEN Delivery_Status = 'Delayed' THEN 1 ELSE 0 END)
        / COUNT(*), 2
    )                                                                 AS Delay_Pct
FROM ecommerce_orders
GROUP BY Courier_Partner
ORDER BY Delay_Pct DESC;

/*
ACTUAL RESULT:
Courier_Partner | Total_Orders | Delayed_Orders | Delay_Pct
India Post      | 984          | 564            | 57.32%
DTDC            | 1114         | 581            | 52.15%
Blue Dart       | 934          | 445            | 47.64%
Delhivery       | 1067         | 492            | 46.11%
Ecom Express    | 901          | 394            | 43.73%
*/


-- ================================================================
-- QUERY 4 : MONTHLY DELAY TREND
-- ================================================================

SELECT
    MONTH(Order_Date)                                                 AS Month_Num,
    MONTHNAME(Order_Date)                                             AS Month_Name,
    COUNT(*)                                                          AS Total_Orders,
    SUM(CASE WHEN Delivery_Status = 'Delayed' THEN 1 ELSE 0 END)     AS Delayed_Orders,
    ROUND(
        100.0 * SUM(CASE WHEN Delivery_Status = 'Delayed' THEN 1 ELSE 0 END)
        / COUNT(*), 2
    )                                                                 AS Delay_Pct
FROM ecommerce_orders
GROUP BY MONTH(Order_Date), MONTHNAME(Order_Date)
ORDER BY Month_Num;

/*
ACTUAL RESULT:
Month | Month_Name | Total_Orders | Delayed_Orders | Delay_Pct
1     | January    | 432          | 257            | 59.49%   ← HIGHEST SPIKE
2     | February   | 422          | 186            | 44.08%
3     | March      | 430          | 220            | 51.16%
4     | April      | 409          | 192            | 46.94%
5     | May        | 442          | 195            | 44.12%
6     | June       | 395          | 182            | 46.08%
7     | July       | 413          | 222            | 53.75%
8     | August     | 414          | 188            | 45.41%
9     | September  | 366          | 206            | 56.28%   ← SECOND SPIKE
10    | October    | 455          | 231            | 50.77%
11    | November   | 364          | 171            | 46.98%
12    | December   | 458          | 226            | 49.34%
*/


-- ================================================================
-- QUERY 5 : DELAY % BY CITY (Top Contributors)
-- ================================================================

SELECT
    Region,
    City,
    COUNT(*)                                                          AS Total_Orders,
    SUM(CASE WHEN Delivery_Status = 'Delayed' THEN 1 ELSE 0 END)     AS Delayed_Orders,
    ROUND(
        100.0 * SUM(CASE WHEN Delivery_Status = 'Delayed' THEN 1 ELSE 0 END)
        / COUNT(*), 2
    )                                                                 AS Delay_Pct
FROM ecommerce_orders
GROUP BY Region, City
ORDER BY Delayed_Orders DESC;

/*
ACTUAL RESULT:
Region | City        | Total_Orders | Delayed_Orders | Delay_Pct
North  | Lucknow     | 686          | 371            | 54.08%
North  | Delhi       | 627          | 361            | 57.58%
East   | Kolkata     | 661          | 330            | 49.92%
East   | Bhubaneswar | 631          | 329            | 52.14%
South  | Chennai     | 622          | 291            | 46.78%
South  | Bangalore   | 598          | 290            | 48.49%
West   | Mumbai      | 584          | 252            | 43.15%
West   | Pune        | 591          | 252            | 42.64%
*/

-- ================================================================
-- END OF SQL QUERIES FILE
-- ================================================================
