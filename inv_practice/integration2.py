import requests
import json

with open("updated_requests_responses.json", "r") as file:
    records = json.load(file)

#print(records)
#response_id_map = {}


def re_send_requests_and_update_responses(records):
    updated_records = []
    for record in records:
        request_info = record['request']
        method = request_info['method']
        url = request_info['url']
        headers = request_info['headers']
        body = request_info['body']

        old_response_info = record['response']
        old_response_id = old_response_info['id']
        response = None

        try:
            if method == "GET":
                response = requests.get(url, headers)
            elif method == "POST":
                response = requests.post(url, headers=headers, json=body)
            new_status_code = response.status_code
            new_data = response.json()
            if new_status_code == old_response_info['status_code']:
                print(f"Status code for request to {url} is unchanged: {new_status_code}")
            else:
                print(
                    f"Status code for request to {url} changed from {old_response_info['status_code']} to {new_status_code}")

            new_response_info={
                'id':old_response_id,
                'status_code':new_status_code,
                'data':new_data
            }

            updated_record={
                'request': request_info,
                'response': new_response_info
            }
            updated_records.append(updated_record)

        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except Exception as err:
            print(f"Other error occurred: {err}")
        return updated_records

updated_records=re_send_requests_and_update_responses(records)
print(records)
print(updated_records)
print(updated_records==records)

# with open("update_map_new.json","w+") as file:
#     json.dump(updated_records,file,indent=4)

print("Updated records have been saved to 'update_map_new.json'.")

