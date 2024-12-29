import requests
import pandas as pd
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup

# Step 1: Download data
url = 'https://en.wikipedia.org/wiki/List_of_current_United_States_senators'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Debug: Print the HTML content to check if the request was successful
#print(soup.prettify())

# Step 2: Parse data
# Inspect the page to find the correct table class or structure
table = soup.find('table', {'class': 'wikitable sortable'})
if table is None:
    raise ValueError("Could not find the table with class 'wikitable sortable'")

rows = table.find_all('tr')

data = []
for row in rows[1:]:
    cols = row.find_all('td')
    if len(cols) > 0:
        name = cols[0].text.strip()
        start_date = cols[3]['data-sort-value']  # Extract the date from the data-sort-value attribute
        data.append((name, start_date))

# Step 3: Analyze data
df = pd.DataFrame(data, columns=['Name', 'Start Date'])
df['Start Date'] = pd.to_datetime(df['Start Date'], format='%Y/%m/%d', errors='coerce')
df['Years in Office'] = (pd.Timestamp.now() - df['Start Date']).dt.days / 365.25

# Step 4: Create histogram
plt.hist(df['Years in Office'].dropna(), bins=range(0, 50, 2), edgecolor='black')
plt.title('Histogram of US Senators\' Years in Office')
plt.xlabel('Years in Office')
plt.ylabel('Number of Senators')
plt.show()
