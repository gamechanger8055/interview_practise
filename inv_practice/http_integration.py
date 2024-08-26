import json
import requests
from requests.status_codes import codes
from requests.exceptions import HTTPError

def get_and_post_example():
    url = 'https://api.example.com/data'
    headers={
    'Authorization': 'Bearer YOUR_ACCESS_TOKEN'
    }
    params={
        "page":1,
        "limit":20,
        "offset":20
    }
    try:
        responses=requests.get(url,params=params,headers=headers)
        responses.raise_for_status()
        data=responses.json()
        print(data)
    except HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"Other error occurred: {err}")

    payload={
        'name':'john doe',
        'email':'abc@gmail.com'
    }
    payload_json=json.dumps(payload)
    headers={
        'Content-Type': 'application/json'
    }

    response=requests.post(url,json=payload_json,headers=headers)
    if response.status_code==201:
        data=response.json()
        print(data)
    else:
        print(f"Request failed with status code {response.status_code}")


GET_URL = 'https://jsonplaceholder.typicode.com/users'
POST_URL = 'https://jsonplaceholder.typicode.com/posts'

get_url="https://jsonmock.hackerrank.com/api/moviesdata/search"

def fetch_users():
    all_data=[]
    params={"Title":"man"}
    try:
        response=requests.get(get_url,params)
        response.raise_for_status()
        users=response.json()
        total_pages=users['total_pages']
        for i in range(1,total_pages+1):
            params = {
                "page": i,
                "limit": 10,
                "Title":"man"
            }
            response = requests.get(get_url,params)
            response.raise_for_status()
            data = response.json()
            print(data)

    except HTTPError as httperror:
        print(f"HTTP error occurred: {httperror}")

def create_posts(user_id,title,body):
    payload={
        'userId':user_id,
        'title':title,
        'body':body
    }
    try:
        response=requests.post(POST_URL,json=payload)
        response.raise_for_status()
        print(response.json())
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"Other error occurred: {err}")

#fetch_users()
user_id = 1
title = "My New Post"
body = "This is the body of my new post."
create_posts(user_id, title, body)


def download_image(url,filename):
    response=requests.get(url)
    if response.status_code==200:
        with open(filename,"wb") as file:
            file.write(response.content)

def download_images(url,filename):
    response=requests.get(url,stream=True)
    if response.status_code==200:
        with open(filename,"wb") as file:
            for chunk in response.iter_content():
                file.write(chunk)

def file_to_json():
    with open("text.txt","r") as file:
        data=file.read()
        json_data=json.loads(data)
        print(json_data)

def binary_to_image(binary_file,output_file):
    try:
        with open(binary_file,"rb") as bin_file:
            data=bin_file.read()
            #print(data)
        with open(output_file,"wb") as image_file:
            image_file.write(data)
    except FileNotFoundError:
        print(f"File not found: {binary_file}")


image_url = "https://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/asteroid_blend.png"
output_filename = "downloading_image.jpeg"
download_images(image_url, output_filename)
file_to_json()
binary_path="test.bin"
image_path="abc.jpeg"
binary_to_image(binary_path,image_path)