CREATE DATABASE customer_churn_project;
USE customer_churn_project;
SELECT customerID, tenure, TotalCharges, Churn
FROM telco_churn_final
WHERE TotalCharges = 0
  AND tenure = 0
  AND Churn = 'No';
  
  SET SQL_SAFE_UPDATES = 0;
UPDATE telco_churn_final
SET TotalCharges = NULL
WHERE customerID IN (
    SELECT customerID
    FROM (
        SELECT customerID
        FROM telco_churn_final
        WHERE TotalCharges = 0
          AND tenure = 0
          AND Churn = 'No'
    ) AS missing_records
);
SET SQL_SAFE_UPDATES = 1;
SELECT
    COUNT(*) AS total_rows,
    SUM(TotalCharges IS NULL) AS missing_total_charges,
    COUNT(DISTINCT customerID) AS unique_customers
FROM telco_churn_final;

SELECT
    Churn,
    COUNT(*) AS customer_count
FROM telco_churn_final
GROUP BY Churn;

SELECT
    Churn,
    COUNT(*) AS customer_count,
    ROUND(
        COUNT(*) * 100.0 / (SELECT COUNT(*) FROM telco_churn_final),
        2
    ) AS percentage
FROM telco_churn_final
GROUP BY Churn;

SELECT
    Contract,
    COUNT(*) AS total_customers,
    SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END)
        AS churned_customers,
    ROUND(
        SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END)
        * 100.0 / COUNT(*),
        2
    ) AS churn_rate
FROM telco_churn_final
GROUP BY Contract
ORDER BY churn_rate DESC;

SELECT
    CASE
        WHEN tenure <= 12 THEN '0-12 months'
        WHEN tenure <= 24 THEN '13-24 months'
        WHEN tenure <= 48 THEN '25-48 months'
        WHEN tenure <= 60 THEN '49-60 months'
        ELSE '61-72 months'
    END AS tenure_group,
    COUNT(*) AS total_customers,
    SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END)
        AS churned_customers,
    ROUND(
        SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END)
        * 100.0 / COUNT(*),
        2
    ) AS churn_rate
FROM telco_churn_final
GROUP BY tenure_group
ORDER BY MIN(tenure);

SELECT
    PaymentMethod,
    COUNT(*) AS total_customers,
    SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END)
        AS churned_customers,
    ROUND(
        SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END)
        * 100.0 / COUNT(*),
        2
    ) AS churn_rate
FROM telco_churn_final
GROUP BY PaymentMethod
ORDER BY churn_rate DESC;

SELECT
    InternetService,
    COUNT(*) AS total_customers,
    SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END)
        AS churned_customers,
    ROUND(
        SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END)
        * 100.0 / COUNT(*),
        2
    ) AS churn_rate
FROM telco_churn_final
GROUP BY InternetService
ORDER BY churn_rate DESC;

SELECT
    Churn,
    COUNT(*) AS customer_count,
    ROUND(AVG(MonthlyCharges), 2) AS avg_monthly_charges
FROM telco_churn_final
GROUP BY Churn;

SELECT
    SeniorCitizen,
    COUNT(*) AS total_customers,
    SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END)
        AS churned_customers,
    ROUND(
        SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END)
        * 100.0 / COUNT(*),
        2
    ) AS churn_rate
FROM telco_churn_final
GROUP BY SeniorCitizen
ORDER BY SeniorCitizen;

SELECT
    OnlineSecurity,
    COUNT(*) AS total_customers,
    SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END)
        AS churned_customers,
    ROUND(
        SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END)
        * 100.0 / COUNT(*),
        2
    ) AS churn_rate
FROM telco_churn_final
GROUP BY OnlineSecurity
ORDER BY churn_rate DESC;

SELECT
    TechSupport,
    COUNT(*) AS total_customers,
    SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END)
        AS churned_customers,
    ROUND(
        SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END)
        * 100.0 / COUNT(*),
        2
    ) AS churn_rate
FROM telco_churn_final
GROUP BY TechSupport
ORDER BY churn_rate DESC;

SELECT
    Contract,
    InternetService,
    COUNT(*) AS total_customers,
    SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END)
        AS churned_customers,
    ROUND(
        SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END)
        * 100.0 / COUNT(*),
        2
    ) AS churn_rate
FROM telco_churn_final
GROUP BY Contract, InternetService
HAVING COUNT(*) >= 50
ORDER BY churn_rate DESC;
