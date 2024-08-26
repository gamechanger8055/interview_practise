import requests





BASE_URL = 'http://127.0.0.1:5000'

def get_users():
    response=requests.get(f'{BASE_URL}/users')
    if response.status_code==200:
        return response.json()
    raise ValueError("not found")

def get_user(user_id):
    response = requests.get(f'{BASE_URL}/users/{user_id}')
    if response.status_code == 200:
        return response.json()
    return

def add_user(name):
    #headers = {'Content-Type': 'application/json'}
    response=requests.post(f'{BASE_URL}/users',json={"name":name})
    if response.status_code==201:
        return response.json()
    return

def update_user(user_id,name):
    response=requests.put(f'{BASE_URL}/users/{user_id}',json={"name":name})
    if response.status_code==200:
        return response.json()
    return

def delete_user(user_id):
    response = requests.delete(f'{BASE_URL}/users/{user_id}')
    return response.status_code == 204

if __name__ == '__main__':
    print("All users:", get_users())
    print("Add user:", add_user("Charlie"))
    print("Get user 3:", get_user(3))
    print("Update user 3:", update_user(3, "Charles"))
    print("Delete user 3:", delete_user(3))
    print("All users after deletion:", get_users())