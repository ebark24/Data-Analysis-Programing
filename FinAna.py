import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Import the Fin Data and assign it to a data frame
df = pd.read_csv('financials.csv')

# Reduce the data table to the most important parts
basic_df = df[['Symbol', 'Name', 'Sector', 'Price','Price/Earnings', 'Dividend Yield', 'Earnings/Share']]

#Sort the Data Based on Divedend Yield
div_df = basic_df.sort_values(by='Dividend Yield', ascending=False)

#Print Data with an explination beforehand
print("One of the most common ways for people to invest their money is through the stock market. There are a couple of different ways that people can make a return on their investment, one is by having the value of the stock increase, but another way is through dividends which the company pays to the investors if the company does well. With this data table I wanted to find some of the companies with the highest dividend yields which would be a good investment. Press enter to look at some of the companies with the top dividend yields.")
input()
print(div_df.head())
input("Press Enter to Continue")

#Introduce the next Concept
print("As an investor you want the value of your stock to increase so that when you sell it later you can get the most return. One of the best ways to see if the value of a stock will increase is by looking at the price/earning ratio to see how the earnings that the company made compared to the price of the stock. I wanted to create a graph that shows which industries had the highest price/earnings to determine which industries are experiencing the most growth right now. Press Enter to view the graph.")
input()
# Group the Stocks by thier sector and then find the average of the P/E and then sort them by the highest
sector_pe_df = df.groupby('Sector')['Price/Earnings'].mean().sort_values(ascending=False)

# Plot a graph based on the Previous Data Frame that was made
sector_pe_df.plot(kind='bar', color='skyblue', figsize=(10, 6))

plt.title('Average P/E Ratio by Sector')
plt.xlabel('Sector')
plt.ylabel('Average P/E Ratio')
plt.xticks(rotation=45, ha='right')

plt.tight_layout()
plt.show()
input("Press Enter to Continue")

#Introduce the idea for the next data table that builds on the previous graph
print("Looking at the top 2 sectors from this graph we can see that Information Technology and Energy are two of the biggest growing industries. Let's look at the top 5 Companies in these sectors based on their P/E ratio. These are some good investment options.")
input("Press Enter to Continue")

# Filter the Data to only include the Top 2 Sectors from the previous section
E_IT_companies = df[df['Sector'].isin(['Information Technology', 'Energy'])]
E_IT_companies = E_IT_companies[['Symbol', 'Name', 'Sector', 'Price','Price/Earnings']]

# Top 5 based on P/E ratio using the filtered Data frame 
top_E_IT = E_IT_companies.nlargest(5, 'Price/Earnings')  
print(top_E_IT)


