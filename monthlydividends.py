import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the CSV file
df = pd.read_csv('source/IG-DividendTransactionHistory.csv', encoding='UTF-8-SIG')

# Convert TextDate to datetime
df['Date'] = pd.to_datetime(df['TextDate'], format='%d/%m/%y')

# Extract month and year
df['Month-Year'] = df['Date'].dt.to_period('M')

# Group by month-year and sum the PL Amount
monthly_dividends = df.groupby('Month-Year')['PL Amount'].sum().reset_index()

# Sort the dataframe by Month-Year
monthly_dividends = monthly_dividends.sort_values('Month-Year')

# Set up the plot style
plt.figure(figsize=(12, 6))
sns.set_style("whitegrid")

# Create the bar plot
ax = sns.barplot(x='Month-Year', y='PL Amount', data=monthly_dividends)

# Customize the plot
plt.title('Total Dividends by Month', fontsize=16)
plt.xlabel('Month-Year', fontsize=12)
plt.ylabel('Total Dividends (AUD)', fontsize=12)
plt.xticks(rotation=45, ha='right')

# Add value labels on top of each bar
for i, v in enumerate(monthly_dividends['PL Amount']):
    ax.text(i, v, f'${v:.2f}', ha='center', va='bottom')

# Adjust layout and display the plot
plt.tight_layout()
plt.show()

print("Graph generated successfully.")