import requests
from bs4 import BeautifulSoup
import pandas as pd

#stock codes that we are targetting
STOCKS = ['F', 'GLAD', 'HRZN', 'AGNC', 'PSEC', 'KMI']

# this is where we will save all the stocks we are looping through
stock_matrix = [['Stock', 'StockPriceClose', 'Div%']]

# looping through each stock name
for stock_name in STOCKS:
    URL = f'https://www.marketwatch.com/investing/stock/{stock_name}'

    response = requests.get(URL)
    webpage = response.text
    soup = BeautifulSoup(webpage, 'html.parser')

    need = []

    for li_tag in soup.find_all('ul', class_='list list--kv list--col50'):
        for span_tag in li_tag.find_all('li', class_='kv__item'):
            value = span_tag.find('span', class_='primary').text
            need.append(value)

    div_yield = need[10]

    want = []

    for td in soup.find_all('tr', class_='table__row'):
        value = td.find('td', class_='table__cell u-semi')
        want.append(value)

    current_price = want[7].text

    # make a list of the complete data you've gathered
    row_of_data = [stock_name, current_price, div_yield]
    # append it to our matrix
    stock_matrix.append(row_of_data)

# Once the matrix is done, we will turn it into a dataframe
# I already put the column names in the matrix when I first made the assignment, so I will make those the column names instead...
# if you dont do this it will say 0, 1, 2 etc on the top of each column
df = pd.DataFrame(stock_matrix[1:], columns=stock_matrix[0])

# save the dataframe as a csv file to your computer
# index=false to not save the indicies of each row... if you erase this,it will say 0, 1, 2 etc on the beginning of each row
# the file name is stocks.csv, change it to whatever and where ever you want it to go.
df.to_csv('stocks.csv', index=False)

