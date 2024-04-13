import requests
import json
from pathlib import Path

# Define the path to the configuration file
config_file_path = Path("/home/david/output.json")

# Read the zone ID from the configuration file
with config_file_path.open('r') as file:
    zone_id = file.read().strip()

# Define the API endpoint for Cloudflare lists
url = f"https://api.cloudflare.com/client/v4/zones/{zone_id}/rules/lists"

# Define the headers with secure token handling
headers = {
    "Authorization": "Bearer eXnsJS-v5FvKgoR4rYpOtz7mEAMVmmZ6XYCcG3sP",
    "Content-Type": "application/json"
}

# Make the API call
response = requests.get(url, headers=headers)

# Get the JSON data from the response
data = response.json()

# Define the output directory
output_dir = Path("/home/david/Projects")

# Ensure the output directory exists
output_dir.mkdir(parents=True, exist_ok=True)

# Find the highest numbered existing file
existing_files = list(output_dir.glob("output*.json"))
if existing_files:
    highest_num = max(int(f.stem[6:]) for f in existing_files)
else:
    highest_num = 0

# Define the output file name
output_file = output_dir / f"output{highest_num + 1}.json"

# Open the output file for writing
with output_file.open('w') as f:
    # Write the JSON data to the file in a pretty format
    json.dump(data, f, indent=4)
