import requests
import json

# Load request and response data from a JSON file
with open('api_responses.json', 'r') as file:
    records = json.load(file)

# Map to maintain old response IDs to new response IDs
response_id_map = {}

# Function to re-send requests and update responses
def re_send_requests_and_update_responses(records):
    updated_records = []

    for record in records:
        request_info = record['request']
        old_response_info = record['response']
        old_response_id = old_response_info['id']

        method = request_info['method']
        url = request_info['url']
        headers = request_info['headers']
        body = request_info['body']
        response=None

        try:
            # Make the request
            if method == 'GET':
                response = requests.get(url, headers=headers)
            elif method == 'POST':
                response = requests.post(url, headers=headers, json=body)
            # Add more methods if needed (PUT, DELETE, etc.)

            new_status_code = response.status_code
            new_data = response.json()

            # Compare the status codes
            if new_status_code == old_response_info['status_code']:
                print(f"Status code for request to {url} is unchanged: {new_status_code}")
            else:
                print(f"Status code for request to {url} changed from {old_response_info['status_code']} to {new_status_code}")

            # Update response info
            new_response_info = {
                'id': response_id_map.get(old_response_id, old_response_id + 1000),  # Example ID mapping logic
                'status_code': new_status_code,
                'data': new_data
            }

            # Update the map
            response_id_map[old_response_id] = new_response_info['id']

            # Update the record
            updated_record = {
                'request': request_info,
                'response': new_response_info
            }
            updated_records.append(updated_record)

        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except Exception as err:
            print(f"Other error occurred: {err}")

    return updated_records

# Re-send requests and get updated records
updated_records = re_send_requests_and_update_responses(records)

# Save updated records back to a JSON file
with open('updated_requests_responses.json', 'w') as file:
    json.dump(updated_records, file, indent=4)

print("Updated records have been saved to 'updated_requests_responses.json'.")


