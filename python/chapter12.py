import requests
import json

url = 'https://coderbyte.com/api/challenges/json/age-counting'
response = requests.get(url)

data = json.loads(response.content)['data']
age_data = data.split(',')

count = 0
for age in age_data:
    try:
        age_value = int(age.split('=')[1])
        if age_value >= 50:
            count += 1
    except ValueError:
        # Ignore non-numeric values in the age data
        pass

print(count)
####