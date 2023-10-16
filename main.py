import json
import pandas as pd
import matplotlib.pyplot as plt


with open('financial_data.json', 'r') as f:
    data = json.load(f)


sales_df = pd.DataFrame(data['sales_data'])
expenses_df = pd.DataFrame(data['expenses_data'])


total_revenue = sales_df['revenue'].sum()


total_expenses = expenses_df['expenses'].sum()


profit = total_revenue - total_expenses

plt.figure(figsize=(10, 6))
plt.plot(sales_df['date'], sales_df['revenue'], label='Revenue', marker='o')
plt.plot(expenses_df['date'], expenses_df['expenses'], label='Expenses', marker='o')
plt.xlabel('Date')
plt.ylabel('Amount')
plt.title('Financial Data Analysis')
plt.legend()
plt.show()

print(f'Total Revenue: ${total_revenue}')
print(f'Total Expenses: ${total_expenses}')
print(f'Profit: ${profit}')
