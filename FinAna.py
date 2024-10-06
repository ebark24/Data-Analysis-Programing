import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('financials.csv')

basic_df = df[['Symbol', 'Name', 'Sector', 'Price','Price/Earnings', 'Dividend Yield', 'Earnings/Share']]

div_df = basic_df.sort_values(by='Dividend Yield', ascending=False)

print(div_df.head())

sector_pe_df = df.groupby('Sector')['Price/Earnings'].mean().sort_values(ascending=False)

sector_pe_df.plot(kind='bar', color='skyblue', figsize=(10, 6))

plt.title('Average P/E Ratio by Sector')
plt.xlabel('Sector')
plt.ylabel('Average P/E Ratio')
plt.xticks(rotation=45, ha='right')

plt.tight_layout()
plt.show()