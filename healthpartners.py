import requests
import pandas as pd
import re
import re # For custom snake_case function

# Define snake_case function
def to_snake_case(name):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

# Dataset URL
url = "https://data.cms.gov/provider-data/api/1/metastore/schemas/dataset/items"
# Download the dataset
response = requests.get(url)

if response.status_code == 200:
    from io import StringIO
    data = pd.read_csv(StringIO(response.text))
    print("Original column names:", data.columns.tolist())

    # Convert column names to snake_case
    data.columns = [to_snake_case(col) for col in data.columns]
    print("Converted column names:", data.columns.tolist())
else:
    print(f"Failed to download dataset. Status code: {response.status_code}")
