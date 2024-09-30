import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the CSV file
df = pd.read_csv('source/IG-DividendTransactionHistory.csv', encoding='UTF-8-SIG')

df['Date'] = pd.to_datetime(df['TextDate'], format='%d/%m/%y')

# Extract quarter from the date
df['Quarter'] = df['Date'].dt.to_period('Q')

# Group by quarter and sum the PL Amount
quarterly_dividends = df.groupby('Quarter')['PL Amount'].sum().reset_index()

# Set up the plot style
plt.figure(figsize=(14, 7))
sns.set_style("whitegrid")

# Create the bar plot
ax = sns.barplot(x='Quarter', y='PL Amount', data=quarterly_dividends)

# Customize the plot
plt.title('Total Dividends by Quarter', fontsize=16)
plt.xlabel('Quarter', fontsize=12)
plt.ylabel('Total Dividends (AUD)', fontsize=12)
plt.xticks(rotation=45, ha='right')

# Add value labels on top of each bar
for i, v in enumerate(quarterly_dividends['PL Amount']):
    ax.text(i, v, f'${v:.2f}', ha='center', va='bottom')

# Adjust layout and display the plot
plt.tight_layout()
plt.show()

print("Quarterly dividends data:")
print(quarterly_dividends)
print("\
Graph generated successfully.")