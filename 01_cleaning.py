import pandas as pd
df=pd.read_csv(r"C:\Users\monic\Downloads\Telco-Customer-Churn.csv")
print(df.head())
print(df.shape)
print(df.columns)
print("\nDataset Information:")
df.info()
print("\nTotal Charges - First 20 Values:")
print(df["TotalCharges"].head(20))
print("\nTotal Charges - Data Type:")
print(df["TotalCharges"].dtype)
print("\nBlank Total Charges:")
print((df["TotalCharges"].str.strip() == "").sum())
print("\nCustomers with Blank Total Charges:")
blank_mask = df["TotalCharges"].str.strip() == ""
print(df.loc[blank_mask, ["customerID", "tenure", "TotalCharges", "Churn"]])
df["TotalCharges"] = df["TotalCharges"].str.strip()
df["TotalCharges"] = pd.to_numeric(
    df["TotalCharges"],
    errors="coerce"
    )
print("\nTotalCharges Data Type:")
print(df["TotalCharges"].dtype)
print("\nMissing TotalCharges:")
print(df["TotalCharges"].isna().sum())
print("\nDuplicate Rows:")
print(df.duplicated().sum())
print("\nMissing Values in Each Column:")
print(df.isna().sum())
print("\nUnique Customer IDs:")
print(df["customerID"].nunique())
print("\nTotal Customer Records:")
print(len(df))
print("\nDuplicate Customer IDs:")
print(df["customerID"].duplicated().sum())
print("\nNumerical Columns Summary:")
print(df.describe())
print("\nCustomer Churn Distribution:")
print(df["Churn"].value_counts())
print("\nCustomer Churn Percentage:")
print(df["Churn"].value_counts(normalize=True) * 100)
total_customers = len(df)
churned_customers = (df["Churn"] == "Yes").sum()
churn_rate = (churned_customers / total_customers) * 100
print("\nTotal Customers:", total_customers)
print("Churned Customers:", churned_customers)
print("Churn Rate:", round(churn_rate, 2), "%")
print("\nContract Type vs Churn:")
print(pd.crosstab(df["Contract"], df["Churn"]))
contract_churn = pd.crosstab(
    df["Contract"],
    df["Churn"],
    normalize="index"
) * 100
print("\nChurn Percentage by Contract:")
print(contract_churn.round(2))
print("\nAverage Tenure by Churn Status:")
print(
    df.groupby("Churn")["tenure"].mean().round(2)
)
print("\nAverage Monthly Charges by Churn Status:")
print(
    df.groupby("Churn")["MonthlyCharges"].mean().round(2)
)
print("\nInternet Service vs Churn:")
print(
    pd.crosstab(
        df["InternetService"],
        df["Churn"]
    )
)
print("\nChurn Percentage by Internet Service:")
internet_churn = pd.crosstab(
    df["InternetService"],
    df["Churn"],
    normalize="index"
) * 100
print(internet_churn.round(2))
print("\nPayment Method vs Churn:")
print(
    pd.crosstab(
        df["PaymentMethod"],
        df["Churn"]
    )
)
print("\nChurn Percentage by Payment Method:")
payment_churn = pd.crosstab(
    df["PaymentMethod"],
    df["Churn"],
    normalize="index"
) * 100
print(payment_churn.round(2))
print("\nSenior Citizen Status vs Churn:")
print(
    pd.crosstab(
        df["SeniorCitizen"],
        df["Churn"]
    )
)
print("\nChurn Percentage by Senior Citizen Status:")
senior_churn = pd.crosstab(
    df["SeniorCitizen"],
    df["Churn"],
    normalize="index"
) * 100
print(senior_churn.round(2))
print("\nPartner Status vs Churn:")
print(
    pd.crosstab(
        df["Partner"],
        df["Churn"]
    )
)
print("\nChurn Percentage by Partner Status:")
partner_churn = pd.crosstab(
    df["Partner"],
    df["Churn"],
    normalize="index"
) * 100
print(partner_churn.round(2))
print("\nDependents Status vs Churn:")
print(
    pd.crosstab(
        df["Dependents"],
        df["Churn"]
    )
)
print("\nChurn Percentage by Dependents Status:")
dependents_churn = pd.crosstab(
    df["Dependents"],
    df["Churn"],
    normalize="index"
) * 100
print(dependents_churn.round(2))
print("\nOnline Security vs Churn:")
print(
    pd.crosstab(
        df["OnlineSecurity"],
        df["Churn"]
    )
)
print("\nChurn Percentage by Online Security:")
security_churn = pd.crosstab(
    df["OnlineSecurity"],
    df["Churn"],
    normalize="index"
) * 100
print(security_churn.round(2))
print("\nTech Support vs Churn:")
print(
    pd.crosstab(
        df["TechSupport"],
        df["Churn"]
    )
)
print("\nChurn Percentage by Tech Support:")
tech_support_churn = pd.crosstab(
    df["TechSupport"],
    df["Churn"],
    normalize="index"
) * 100
print(tech_support_churn.round(2))
print("\nOnline Backup vs Churn:")
print(
    pd.crosstab(
        df["OnlineBackup"],
        df["Churn"]
    )
)
print("\nChurn Percentage by Online Backup:")
backup_churn = pd.crosstab(
    df["OnlineBackup"],
    df["Churn"],
    normalize="index"
) * 100
print(backup_churn.round(2))
print("\nDevice Protection vs Churn:")
print(
    pd.crosstab(
        df["DeviceProtection"],
        df["Churn"]
    )
)
print("\nChurn Percentage by Device Protection:")
device_churn = pd.crosstab(
    df["DeviceProtection"],
    df["Churn"],
    normalize="index"
) * 100
print(device_churn.round(2))
print("\nStreaming TV vs Churn:")
print(
    pd.crosstab(
        df["StreamingTV"],
        df["Churn"]
    )
)
print("\nChurn Percentage by Streaming TV:")
streaming_tv_churn = pd.crosstab(
    df["StreamingTV"],
    df["Churn"],
    normalize="index"
) * 100
print(streaming_tv_churn.round(2))
print("\nStreaming Movies vs Churn:")
print(
    pd.crosstab(
        df["StreamingMovies"],
        df["Churn"]
    )
)
print("\nChurn Percentage by Streaming Movies:")
streaming_movies_churn = pd.crosstab(
    df["StreamingMovies"],
    df["Churn"],
    normalize="index"
) * 100
print(streaming_movies_churn.round(2))
print("\nPhone Service vs Churn:")
print(
    pd.crosstab(
        df["PhoneService"],
        df["Churn"]
    )
)
print("\nChurn Percentage by Phone Service:")
phone_churn = pd.crosstab(
    df["PhoneService"],
    df["Churn"],
    normalize="index"
) * 100
print(phone_churn.round(2))
print("\nMultiple Lines vs Churn:")
print(
    pd.crosstab(
        df["MultipleLines"],
        df["Churn"]
    )
)
print("\nChurn Percentage by Multiple Lines:")
multiple_lines_churn = pd.crosstab(
    df["MultipleLines"],
    df["Churn"],
    normalize="index"
) * 100
print(multiple_lines_churn.round(2))
print("\nPaperless Billing vs Churn:")
print(
    pd.crosstab(
        df["PaperlessBilling"],
        df["Churn"]
    )
)
print("\nChurn Percentage by Paperless Billing:")
paperless_churn = pd.crosstab(
    df["PaperlessBilling"],
    df["Churn"],
    normalize="index"
) * 100
print(paperless_churn.round(2))
df["TenureGroup"] = pd.cut(
    df["tenure"],
    bins=[-1, 12, 24, 48, 60, 72],
    labels=[
        "0-12 months",
        "13-24 months",
        "25-48 months",
        "49-60 months",
        "61-72 months"
    ]
)
print("\nTenure Group vs Churn:")
print(
    pd.crosstab(
        df["TenureGroup"],
        df["Churn"]
    )
)
print("\nChurn Percentage by Tenure Group:")
tenure_churn = pd.crosstab(
    df["TenureGroup"],
    df["Churn"],
    normalize="index"
) * 100
print(tenure_churn.round(2))
print("\nAverage Total Charges by Churn:")
print(
    df.groupby("Churn")["TotalCharges"]
    .mean()
    .round(2)
)
print("\nFinal Dataset Shape:")
print(df.shape)
print("\nMissing Values:")
print(df.isna().sum())
print("\nDuplicate Rows:")
print(df.duplicated().sum())



import matplotlib.pyplot as plt
churn_counts = df["Churn"].value_counts().reindex(["No", "Yes"])
churn_percentages = churn_counts / len(df) * 100
plt.figure(figsize=(7, 5))
bars = plt.bar(churn_counts.index, churn_counts.values)
plt.title("Customer Churn Distribution")
plt.xlabel("Customer Churn")
plt.ylabel("Number of Customers")
for i, bar in enumerate(bars):
    height = bar.get_height()
    percentage = churn_percentages.iloc[i]

    plt.text(
        bar.get_x() + bar.get_width() / 2,
        height,
        f"{int(height):,}\n({percentage:.2f}%)",
        ha="center",
        va="bottom"
    )
plt.tight_layout()
plt.show()

# SECOND CHART
# Churn Rate by Contract Type
contract_churn = pd.crosstab(
    df["Contract"],
    df["Churn"],
    normalize="index"
) * 100

churn_rates = contract_churn["Yes"].sort_values(
    ascending=False
)

plt.figure(figsize=(8, 5))
bars = plt.bar(churn_rates.index, churn_rates.values)

plt.title("Churn Rate by Contract Type")
plt.xlabel("Contract Type")
plt.ylabel("Churn Rate (%)")
plt.ylim(0, 50)

for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        height,
        f"{height:.2f}%",
        ha="center",
        va="bottom"
    )

plt.tight_layout()
plt.show()


# Chart 3: Churn Rate by Tenure Group

tenure_churn = pd.crosstab(
    df["TenureGroup"],
    df["Churn"],
    normalize="index"
) * 100

tenure_churn_rate = tenure_churn["Yes"]

plt.figure(figsize=(9, 5))

bars = plt.bar(
    tenure_churn_rate.index.astype(str),
    tenure_churn_rate.values
)

plt.title("Customer Churn Rate by Tenure Group")
plt.xlabel("Customer Tenure")
plt.ylabel("Churn Rate (%)")
plt.ylim(0, 55)

for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        height,
        f"{height:.2f}%",
        ha="center",
        va="bottom"
    )
plt.tight_layout()
plt.show()


# Chart 4: Churn Rate by Payment Method
payment_churn = pd.crosstab(
    df["PaymentMethod"],
    df["Churn"],
    normalize="index"
) * 100

payment_churn_rate = payment_churn["Yes"].sort_values(
    ascending=False
)

plt.figure(figsize=(10, 5))

bars = plt.bar(
    payment_churn_rate.index,
    payment_churn_rate.values
)

plt.title("Customer Churn Rate by Payment Method")
plt.xlabel("Payment Method")
plt.ylabel("Churn Rate (%)")
plt.ylim(0, 55)

plt.xticks(rotation=15, ha="right")

for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        height,
        f"{height:.2f}%",
        ha="center",
        va="bottom"
    )

plt.tight_layout()
plt.show()


# Chart 5: Churn Rate by Internet Service

internet_churn = pd.crosstab(
    df["InternetService"],
    df["Churn"],
    normalize="index"
) * 100

internet_churn_rate = internet_churn["Yes"].sort_values(
    ascending=False
)

plt.figure(figsize=(8, 5))

bars = plt.bar(
    internet_churn_rate.index,
    internet_churn_rate.values
)

plt.title("Customer Churn Rate by Internet Service")
plt.xlabel("Internet Service")
plt.ylabel("Churn Rate (%)")
plt.ylim(0, 50)

for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        height,
        f"{height:.2f}%",
        ha="center",
        va="bottom"
    )

plt.tight_layout()
plt.show()


# Chart 6: Average Monthly Charges by Churn Status

monthly_charges = df.groupby("Churn")["MonthlyCharges"].mean()
monthly_charges = monthly_charges.reindex(["No", "Yes"])

plt.figure(figsize=(7, 5))

bars = plt.bar(
    monthly_charges.index,
    monthly_charges.values
)

plt.title("Average Monthly Charges by Churn Status")
plt.xlabel("Customer Churn")
plt.ylabel("Average Monthly Charges")

for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        height,
        f"{height:.2f}",
        ha="center",
        va="bottom"
    )

plt.tight_layout()
plt.show()

print("CSV rows:", len(df))
print("Blank TotalCharges:", df["TotalCharges"].isna().sum())
print("Unique customers:", df["customerID"].nunique())

# Create a separate copy for MySQL import
df_mysql = df.copy()

# Temporarily replace missing TotalCharges with 0
df_mysql["TotalCharges"] = df_mysql["TotalCharges"].fillna(0)

# Save as a new CSV file
df_mysql.to_csv(
    r"C:\Users\monic\Downloads\Telco_Customer_Churn_MySQL.csv",
    index=False
)

print("Rows prepared:", len(df_mysql))
print("File created successfully")

