import os
import pandas as pd
import matplotlib.pyplot as plt



# Dynamically set the file path relative to the script's location
file_path = os.path.join(os.path.dirname(__file__), "LoanDataset - LoansDatasest.csv")

# Load the dataset
df = pd.read_csv(file_path)

# Clean the data
df['Current_loan_status'] = df['Current_loan_status'].str.strip()
df['loan_intent'] = df['loan_intent'].str.strip()

# Calculate default rate by loan intent
default_rate = df.groupby('loan_intent')['Current_loan_status'].apply(lambda x: (x == 'DEFAULT').mean()).reset_index() # Calculate the mean default rate
default_rate.columns = ['Loan Intent', 'Default Rate']

# Extract data for plotting
loan_intents = default_rate['Loan Intent'] # Extract loan intents
default_rates = default_rate['Default Rate'] # Extract default rates

# Define different shades of pink for the bars
pink_shades = ['#FFC0CB', '#FFB6C1', '#FF69B4', '#FF1493', '#FF85B2', '#FF6EB4']

# Plot: Default Rate by Loan Intent (Bar Chart)
plt.figure(figsize=(10, 6))
bars = plt.bar(loan_intents, default_rates, color=pink_shades[:len(loan_intents)], alpha=0.8)  # Assign shades of pink

# Add numbers on top of the bars
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2, height + 0.01, f"{height:.2f}", ha='center', fontsize=10, color='black')

# Customize the chart
plt.title('Default Rate by Loan Intent', fontsize=16)
plt.xlabel('Loan Intent', fontsize=12)
plt.ylabel('Default Rate', fontsize=12)
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)  # Add horizontal grid lines for better readability
plt.tight_layout()
plt.show()

# Clean the interest rate column
df['loan_int_rate'] = pd.to_numeric(df['loan_int_rate'], errors='coerce')

# Calculate the average loan interest rate by customer age
avg_interest_by_age = df.groupby('customer_age')['loan_int_rate'].mean().reset_index()

# Plot: Histogram of Loan Interest Rates by Customer Age
plt.figure(figsize=(10, 6))

# Plot the histogram
plt.hist(avg_interest_by_age['loan_int_rate'], bins=10, color='#FF69B4', edgecolor='black', alpha=0.8, align='mid') 

# Customize the chart
plt.title('Distribution of Average Loan Interest Rates by Customer Age', fontsize=16) 
plt.xlabel('Average Interest Rate (%)', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)  # Add horizontal grid lines for better readability
plt.tight_layout() # Adjust layout to fit labels
plt.show()

# Calculate the proportion of loans by current loan status
loan_status_counts = df['Current_loan_status'].value_counts()

# Plot: Proportion of Loans by Current Loan Status (Pie Chart)
plt.figure(figsize=(8, 8))
loan_status_counts.plot.pie(
    autopct='%1.1f%%', 
    startangle=90, 
    colors=['#FFB6C1', '#FF69B4', '#FFC0CB', '#FF1493'],  # Different shades of pink
    labels=loan_status_counts.index, 
    explode=(0.1, 0)  # Slightly explode the "DEFAULT" slice for emphasis
)
plt.title('Proportion of Loans by Current Loan Status', fontsize=16)
plt.ylabel('')  # Remove the y-axis label for a cleaner look
plt.show()