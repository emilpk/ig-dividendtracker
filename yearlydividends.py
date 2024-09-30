import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the CSV file
df = pd.read_csv('source/IG-DividendTransactionHistory.csv', encoding='UTF-8-SIG')

# Convert TextDate to datetime
df['Date'] = pd.to_datetime(df['TextDate'], format='%d/%m/%y')

# Extract year
df['Year'] = df['Date'].dt.year

# Group by year and sum the PL Amount
yearly_dividends = df.groupby('Year')['PL Amount'].sum().reset_index()

# Set up the plot style
plt.figure(figsize=(12, 6))
sns.set_style("whitegrid")

# Create the bar plot
ax = sns.barplot(x='Year', y='PL Amount', data=yearly_dividends)

# Customize the plot
plt.title('Total Dividends by Year', fontsize=16)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Total Dividends (AUD)', fontsize=12)

# Add value labels on top of each bar
for i, v in enumerate(yearly_dividends['PL Amount']):
    ax.text(i, v, f'${v:.2f}', ha='center', va='bottom')

# Adjust layout and display the plot
plt.tight_layout()
plt.show()

print("Yearly dividends data:")
print(yearly_dividends)
print("\
Graph generated successfully.")