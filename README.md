# Customer-Churn-Analysis
Customer Churn Analysis using Python, Pandas, and Power BI to identify churn patterns, analyze customer behavior, and support data-driven customer retention strategies.


## Project Overview

An end-to-end data analytics project using Python, Pandas, and Power BI to analyze customer churn, identify patterns in customer behavior, and support data-driven retention strategies.

## Dashboard Preview

<img width="605" height="337" alt="image" src="https://github.com/user-attachments/assets/d84936ce-54a1-4d86-af6c-af3866599c74" />


## Business Problem

Customer churn occurs when customers stop using a company's services. Understanding why customers leave helps businesses identify retention risks and improve customer relationships.

This project explores the following questions:

1. What is the overall customer churn rate?
2. Which contract types and payment methods are associated with higher churn?
3. How do internet service type and customer tenure relate to churn?
4. How do online security and monthly charges differ between customers who churn and those who stay?
5. Which customer segments may benefit from targeted retention strategies?

## Dataset

- **Source:** IBM Telco Customer Churn dataset.
- **Data type:** Customer-level telecommunications dataset.
- **Key fields:** Customer ID, gender, senior citizen status, partner status, tenure, contract type, internet service, payment method, monthly charges, total charges, and churn status.

## Tools & Technologies

- **Python:** Data analysis and preparation.
- **Pandas:** Data cleaning, transformation, and exploratory analysis.
- **Matplotlib:** Charts for churn distribution, contract type, tenure, payment method, internet service, and monthly charges
- **SQL:** Customer data queries, churn analysis, and customer segment comparisons.
- **Power BI:** Interactive dashboard development and KPI visualization.

## Project Workflow

1. **Data inspection:** Examined the dataset structure, columns, and data types.
2. **Data cleaning:** Converted `TotalCharges` to a numeric data type and inspected missing values.
3. **Feature preparation:** Created tenure groups (0-12, 13-24, 25-48, 49-60, 61-72 months) to compare churn across customer lifetimes.
4. **Exploratory data analysis:** Analyzed churn across customer tenure, contract type, payment method, internet service, and partner status.
5. **KPI analysis:** Calculated overall churn and compared churn rates across customer segments.
6. **Dashboard development:** Created a Power BI dashboard to communicate key metrics and customer churn patterns.

## Key Performance Indicators

| Metric | Result |
|---|---:|
| Overall customer churn rate | 26.54% |
| Churn rate: Month-to-month contracts | 42.71% |
| Churn rate: Two-year contracts | 2.83% |
| Churn rate: Fiber optic customers | 41.89% |
| Churn rate: Electronic check users | 45.29% |
| Churn rate: Senior citizens | 41.68% |
| Average tenure: Churned customers | 17.98 months |
| Average tenure: Retained customers | 37.57 months |


## Key Findings

- **Contract type:** Month-to-month customers churn at 42.71%, compared with 11.27% for one-year and 2.83% for two-year contracts.
- **Payment method:** Electronic check users churn at 45.29%, against 15% to 19% for every other payment method.
- **Internet service:** Fiber optic customers churn at 41.89%, compared with 18.96% for DSL.
- **Online security:** Customers without online security churn at 41.77%, compared with 14.61% for those with it.
- **Customer tenure:** Churn is highest in the first 12 months (47.44%) and falls to 6.61% after 61 months. Churned customers had an average tenure of 17.98 months, versus 37.57 months for retained customers.
- **Monthly charges:** Churned customers pay more on average ($74.44 a month versus $61.27 for retained customers).
- **Senior citizens:** Senior citizens churn at 41.68%, against the overall rate of 26.54%.
- **Partner status:** Customers without a partner churn at 32.96%, compared with 19.66% for customers with a partner.


## Business Recommendations

Based on the findings above, these actions could help reduce churn:

1. **Move customers off month-to-month plans.** Month-to-month churn is 42.71% versus 2.83% on two-year contracts, so explore incentives for longer-term plans.
2. **Focus onboarding on the first year.** Churn reaches 47.44% in the first 12 months, so early engagement and onboarding could have the biggest effect.
3. **Investigate fiber optic service.** At 41.89% churn, review service quality, pricing, and support for these customers.
4. **Improve the electronic check experience.** At 45.29% churn, look for friction in the payment process and encourage automatic payment methods, which churn at about 15% to 17%.
5. **Promote online security.** Customers without it churn at 41.77% versus 14.61% with it, so consider including it in bundles or onboarding.
6. **Support senior customers.** With 41.68% churn, evaluate targeted retention support for this segment.
7. **Track churn regularly.** Monitor churn KPIs over time to measure whether these actions work.




## Author

**Monica Subramaniam**

[LinkedIn Profile](https://www.linkedin.com/in/monica-subramaniam-2a3006398)

**Project focus:** Customer Analytics | Churn Analysis | Python | Pandas | Power BI
