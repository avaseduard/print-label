import requests
import csv
from io import StringIO

# Find item's nanme by searching the code
def search_by_cod(cod):
   # Download the data csv file
   url = 'https://www.sierra.ro/feed_emag/feed_emag.txt'
   response = requests.get(url)
   # Parse the CSV data
   if response.status_code == 200:
       csv_data = StringIO(response.text)
       reader = csv.DictReader(csv_data)      
       # Search for 'nume' by 'cod'
       for row in reader:
           if row['cod'] == cod:
               return row['nume']
       return f'No match found for cod: {cod}'
   else:
       return f'Failed to retrieve data. Status code: {response.status_code}'